import logging
import os
import subprocess
import sys

def do_test( working_dir: str , res_sample_path: str , cmd: str , logger: logging.Logger ):
    os.chdir( working_dir )
    result = subprocess.run( cmd , shell = True , capture_output = True , text = True , encoding = "utf-8" )
    if result.returncode != 0:
        logger.error( f"subprocess returns none-zero: rc: { result.returncode } stdout: \"{ result.stdout }\" stderr: \"{ result.stderr }\"" )
        logger.info( "stopping this test task" )
        exit( result.returncode )

    with open( res_sample_path , 'r' , encoding = "utf-8" ) as rFile:
        res_sample = rFile.read()

    if res_sample == result.stdout:
        logger.info( "passed" )
        exit( 0 )
    else:
        logger.error( f"failed: stdout: \"{ result.stdout }\"" )
        exit( 1 )
