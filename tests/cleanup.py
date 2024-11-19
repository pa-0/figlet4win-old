import logging
import os
import shutil
import subprocess
import sys

logging.basicConfig( filename = f"test.log" , format = "%(asctime)s %(name)s: %(levelname)-6s %(message)s",
                         datefmt = "[%Y-%m-%d %H:%M:%S]" , level = logging.INFO )
logger = logging.getLogger( "cleanup" )

def get_font_files_and_font_control_files( fontdir: str ):
    for root , ds , fs in os.walk( fontdir ):
        for f in fs:
            if f.endswith( ".flf" ) or f.endswith( ".flc" ):
                filepath = os.path.join( root , f )
                logger.info( f"find font file: { filepath }" )
                yield filepath

def main():
    fontdir = sys.argv[1]
    cmake_bin_dir = sys.argv[2]
    testdir = os.path.join( cmake_bin_dir , "tests" )

    font_files = get_font_files_and_font_control_files( fontdir )
    for font in font_files:
        os.remove( font )

    os.remove( os.path.join( testdir , "emboss.tlf" ) )
    os.remove( os.path.join( testdir , "flowerpower.flf" ) )

if __name__ == "__main__":
    main()