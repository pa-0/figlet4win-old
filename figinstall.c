#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sys/stat.h>

#include<windows.h>

void show_helpmsg(){
    printf( "Usage: figinstall [ --no-check ] fontfile\n" );
    return;
}

int main( int argc , char** argv ){
    SetConsoleCP( CP_UTF8 );
    SetConsoleOutputCP( CP_UTF8 );

    if ( argc < 2 || argc > 3 )
    {
        show_helpmsg();
        return 1;
    }

    if ( argc == 3 && strcmp( argv[1] , "--no-check" ) != 0 )
    {
        show_helpmsg();
        return 1;
    }

    char app_dir[MAX_PATH];
    if ( !GetModuleFileName( NULL , app_dir , MAX_PATH ) )
    {
        fprintf( stderr , "Fatal: failed to get exe path\n" );
        return 1;
    }
    char* last_dir_sep_pos = NULL;
    if ( ( last_dir_sep_pos = strrchr( app_dir , '\\' ) ) != NULL )
    {
        *++last_dir_sep_pos = '\0';
    }
    else
    {
        strcat( app_dir , "\\" );
    }

    char* new_fontfile = NULL;
    if ( argc == 2 )
    {
        new_fontfile = argv[1];
        printf( "Checking font file format...\n" );
        char* chkfont_cmd = ( char* ) malloc( MAX_PATH * 2 + 1 );
        sprintf( chkfont_cmd , "%s%s %s" , app_dir , "chkfont.exe" , new_fontfile );
        int res = system( chkfont_cmd );
        free( chkfont_cmd );
        if ( res != 0 )
        {
            printf( "Unexcepted format error occured, exiting...\n" );
            return 1;
        }
        printf( "Font file format checked\n" );
    }
    else
    {
        new_fontfile = argv[2];
        printf( "Font file format check skipped\n" );
    }

    char* install_target_path = ( char* ) malloc( MAX_PATH );
    char* new_fontfile_name = NULL;
    if ( ( new_fontfile_name = strrchr( new_fontfile , '\\' ) ) == NULL &&
         ( new_fontfile_name = strrchr( new_fontfile , '/' ) ) == NULL )
    {
        new_fontfile_name = new_fontfile;
    }
    else
    {
        new_fontfile_name++;
    }
    sprintf( install_target_path , "%s%s\\%s" , app_dir , DEFAULTFONTDIR , new_fontfile_name );
    printf( "Installing font file to: %s\n" , install_target_path );
    struct stat buf;
    if ( stat( install_target_path , &buf ) == 0 )
    {
        char c;
        while ( 1 )
        {
            printf( "This font file already exists, overwrite? (y/n): " );
            scanf( "%c" , &c );
            if ( c == 'y' || c == 'Y' )
            {
                break;
            }
            else if ( c == 'n' || c == 'N' )
            {
                printf( "Exiting...\n" );
                free( install_target_path );
                return 0;
            }
        }        
    }
    if ( !CopyFile( new_fontfile , install_target_path , FALSE ) )
    {
        DWORD errcode = GetLastError();
        char* errmsg = NULL;
        DWORD res = FormatMessage(
            FORMAT_MESSAGE_ALLOCATE_BUFFER | FORMAT_MESSAGE_FROM_SYSTEM ,
            NULL ,
            errcode ,
            MAKELANGID( LANG_ENGLISH , SUBLANG_ENGLISH_US ) ,
            ( LPTSTR ) &errmsg ,
            0 ,
            NULL
        );
        if ( res )
        {
            fprintf( stderr , "Install failed: %s" , errmsg );
            if ( res == ERROR_ACCESS_DENIED || res == ERROR_WRITE_PROTECT )
            {
                printf( "Please try to run figinstall under admin privilege\n" );
            }
        }
        else
        {
            fprintf( stderr , "Install failed, system errcode: %ld\n" , errcode );
        }
        free( install_target_path );
        return 1;
    }
    printf( "Font file installed successfully\n" );
    free( install_target_path );
    return 0;
}
