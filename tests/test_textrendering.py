import logging
import os
import subprocess
import sys

def get_font_files( fontdir: str ):
    for root , ds , fs in os.walk( fontdir ):
        for f in fs:
            if f.endswith( ".flf" ):
                filepath = os.path.join( root , f )
                yield filepath
                
def main():
    logging.basicConfig( filename = f"test.log" , format = "%(asctime)s %(name)s: %(levelname)-6s %(message)s",
                         datefmt = "[%Y-%m-%d %H:%M:%S]" , level = logging.INFO )
    logger = logging.getLogger( "t_textreandering" )

    working_dir = sys.argv[1]
    res_sample_path = sys.argv[2]
    input_text_sample = sys.argv[3]

    os.chdir( working_dir )
    result = subprocess.run( "figlet.exe -I2" , shell = True , capture_output = True , text = True , encoding = "utf-8" )
    if result.returncode != 0:
        logger.error( f"subprocess returned none-zero when getting fontdir: rc: { result.returncode } stdout: \"{ result.stdout }\" stderr: \"{ result.stderr }\"" )
        logger.info( "stopping test_textrendering" )
        exit( result.returncode )

    fontdir = result.stdout[:-1]
    # erase ending endline
    logger.info( f"figlet font dir: { fontdir }" )
    font_files = get_font_files( fontdir )
    
    res = ""

    for font in font_files:
        result = subprocess.run( f"figlet.exe -f { font } < { input_text_sample }" , shell = True , capture_output = True , text = True )
        if result.returncode != 0:
            logger.error( f"subprocess returned none-zero when rendering: font_file: { font } rc: { result.returncode } stdout: \"{ result.stdout }\" stderr: \"{ result.stderr }\"" )
            logger.info( "stopping test_textrendering" )
        res += result.stdout

    with open( res_sample_path , 'r' ) as rFile:
        res_sample = rFile.read()

    if res_sample == res:
        logger.info( "passed" )
        exit( 0 )
    else:
        logger.error( f"failed: res: \"{ res }\"" )
        print( len( res ) , len( res_sample ) )
        for i in range( 0 , len( res ) ):
            if res[i] != res_sample[i]:
                print( i , ord( res[i] ) , ord( res_sample[i])  )
                exit( 1 )
        exit( 1 )
        
if __name__ == "__main__":
    main()
