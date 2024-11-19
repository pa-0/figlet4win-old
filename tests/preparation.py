import logging
import os
import shutil
import subprocess
import sys

logging.basicConfig( filename = f"test.log" , format = "%(asctime)s %(name)s: %(levelname)-6s %(message)s",
                         datefmt = "[%Y-%m-%d %H:%M:%S]" , level = logging.INFO )
logger = logging.getLogger( "preparation" )

def get_font_files_and_font_control_files( fontdir: str ):
    for root , ds , fs in os.walk( fontdir ):
        for f in fs:
            if f.endswith( ".flf" ) or f.endswith( ".flc" ):
                filepath = os.path.join( root , f )
                logger.info( f"find font file: { filepath }" )
                yield filepath

def main():
    fontdir_from = sys.argv[1]
    cmake_bin_dir = sys.argv[2]
    figlet_path = os.path.join( cmake_bin_dir , "figlet.exe" )
    result = subprocess.run( f"{ figlet_path } -I2" , shell = True , capture_output = True , text = True , encoding = "utf-8" )
    if result.returncode != 0:
        logger.error( f"subprocess returned none-zero when getting fontdir: rc: { result.returncode } stdout: \"{ result.stdout }\" stderr: \"{ result.stderr }\"" )
        logger.info( "stopping preparation" )
        exit( result.returncode )

    fontdir_to = result.stdout[:-1]
    # erase ending endline
    if not os.path.isabs( fontdir_to ):
        fontdir_to = os.path.join( cmake_bin_dir , fontdir_to )
    if not os.path.exists( fontdir_to ):
        os.makedirs( fontdir_to )
    logger.info( f"font files copy to: { fontdir_to }" )
    font_files = get_font_files_and_font_control_files( fontdir_from )
    for file in font_files:
        file_copy_to = os.path.join( fontdir_to , os.path.basename( file ) )
        shutil.copy( file , file_copy_to )

    fontdir_tests = os.path.join( cmake_bin_dir , "tests" )
    shutil.copy( "./emboss.tlf" , os.path.join( fontdir_tests , "emboss.tlf" ) )
    shutil.copy( "./flowerpower.flf" , os.path.join( fontdir_tests , "flowerpower.flf" ) )

    shutil.copy( "../showfigfonts.bat" , os.path.join( cmake_bin_dir , "showfigfonts.bat" ) )

if __name__ == "__main__":
    main()
