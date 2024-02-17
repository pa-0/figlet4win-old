@echo off
setlocal enabledelayedexpansion

set figlet_man_path="%~dp0doc\figlet4win.chm"

if not exist %figlet_man_path% (
    echo Cannot find FIGlet4Win manual file
    exit 1
)

start hh %figlet_man_path%

endlocal
