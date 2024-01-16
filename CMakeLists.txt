cmake_minimum_required(VERSION 3.10)
project(figlet4win VERSION 2.2.5 LANGUAGES C)

set(CMAKE_C_CLAGS "${CMAKE_C_FLAGS} -g -O2 -Wall -Wno-unused-value")

add_definitions(-DTLF_FONTS -DUNICODE -D_UNICODE)
add_definitions(-DDEFAULTFONTDIR="")
add_definitions(-DDEFAULTFONTFILE="standard")

include_directories(${CMAKE_SOURCE_DIR})
add_executable(figlet
    figlet.c
    zipio.c
    crc.c
    inflate.c
    utf8.c
)
target_link_libraries(figlet
    ws2_32
)
add_executable(chkfont
    chkfont.c
)
