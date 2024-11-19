import logging
import sys

from testbase import testbase

def main():
    logging.basicConfig( filename = f"test.log" , format = "%(asctime)s %(name)s: %(levelname)-6s %(message)s",
                         datefmt = "[%Y-%m-%d %H:%M:%S]" , level = logging.INFO )
    logger = logging.getLogger( "t_showfigfonts" )

    working_dir = sys.argv[1]
    res_sample_path = sys.argv[2]

    testbase.do_test( working_dir , res_sample_path , "showfigfonts.bat" , logger )

if __name__ == "__main__":
    main()
