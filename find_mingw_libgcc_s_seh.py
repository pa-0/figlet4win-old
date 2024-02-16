import os

PATH = os.environ["PATH"].split( os.pathsep )
gpp_paths = []
for path in PATH:
    this_gcc_path = os.path.join( path , "gcc.exe" )
    this_gpp_path = os.path.join( path , "g++.exe" )
    this_libgccsseh_path = os.path.join( path , "libgcc_s_seh-1.dll" )
    this_libstdcpp_path = os.path.join( path , "libstdc++-6.dll" )
    if os.path.exists( this_gcc_path ) and os.path.exists( this_gpp_path ):
        if os.path.exists( this_libgccsseh_path ):
            print( this_libgccsseh_path.replace( "\\" , "/" ) , end = "" )
            exit( 0 )

exit( 1 )
