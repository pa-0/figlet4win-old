cmake_minimum_required(VERSION 3.10)
project(figlet4win VERSION 2.2.5 LANGUAGES C)

option(FIGlet_Enable_TLF_FONTS "Enable support for Sam Hocevar's TOIlet fonts" ON)

if(DEFINED DEFAULT_FONT_FILE)
    set(FIGlet_Default_Font_File ${DEFAULT_FONT_FILE})
else()
    set(FIGlet_Default_Font_File "standard")
endif()
if(DEFINED DEFAULT_FONT_DIR)
    set(FIGlet_Default_Font_Dir ${DEFAULT_FONT_DIR})
else()
    set(FIGlet_Default_Font_Dir "fonts")
endif()

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=gnu99 -Wall -Wno-unused-value")

set(FIGLET_SRC_LIST
    figlet.c
    zipio.c
    crc.c
    inflate.c
)

if(${FIGlet_Enable_TLF_FONTS})
    add_definitions(-DTLF_FONTS)
    set(FIGLET_SRC_LIST
        ${FIGLET_SRC_LIST}
        utf8.c
    )
endif()
add_definitions(-DDEFAULTFONTDIR="${FIGlet_Default_Font_Dir}")
add_definitions(-DDEFAULTFONTFILE="${FIGlet_Default_Font_File}")

include_directories(${CMAKE_SOURCE_DIR})
add_subdirectory(fonts)

add_executable(figlet
    ${FIGLET_SRC_LIST}
)
if(${FIGlet_Enable_TLF_FONTS})
    target_link_libraries(figlet
        ws2_32
    )
endif()
add_executable(chkfont
    chkfont.c
)

install(
    TARGETS figlet chkfont
    RUNTIME DESTINATION .
)
install(
    FILES ${FIGLET_FONT_CONTROL_FILES} ${FIGLET_FONT_FILES}
    DESTINATION ${FIGlet_Default_Font_Dir}
)
