import logging
import sys

from testbase import testbase

def main():
    logging.basicConfig( filename = f"test.log" , format = "%(asctime)s %(name)s: %(levelname)-6s %(message)s",
                         datefmt = "[%Y-%m-%d %H:%M:%S]" , level = logging.INFO )
    logger = logging.getLogger( "t_kerningcenteredrighttoleftmodeslant" )

    working_dir = sys.argv[1]
    res_sample_path = sys.argv[2]
    input_text_sample = sys.argv[3]

    testbase.do_test( working_dir , res_sample_path , f"figlet.exe -kcR -f slant < { input_text_sample }" , logger )

if __name__ == "__main__":
    main()
