add_test(
    NAME do_preparation
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/preparation.py ${CMAKE_SOURCE_DIR}/fonts ${CMAKE_BINARY_DIR}
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)
add_test(
    NAME showfigfonts_function
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_showfigfonts.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_showfigfonts_res.txt
)
add_test(
    NAME text_rendering
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_textrendering.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_textrendering_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
)
add_test(
    NAME long_text_rendering
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_longtextrendering.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_longtextrendering_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/longtext.txt
)
add_test(
    NAME left_to_right_text
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_lefttorighttext.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_lefttorighttext_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
)
add_test(
    NAME right_to_left_text
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_righttolefttext.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_righttolefttext_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
)
add_test(
    NAME flush_left_justification
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_flushleftjustification.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_flushleftjustification_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
)
add_test(
    NAME flush_right_justification
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_flushrightjustification.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_flushrightjustification_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
)
add_test(
    NAME center_justification
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_centerjustification.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_centerjustification_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
)
add_test(
    NAME kerning_mode
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_kerningmode.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_kerningmode_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
)
add_test(
    NAME full_width_mode
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_fullwidthmode.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_fullwidthmode_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
)
add_test(
    NAME overlap_mode
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_overlapmode.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_overlapmode_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
)
add_test(
    NAME tlf2_font_rendering
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_tlf2fontrendering.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_tlf2fontrendering_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
)
add_test(
    NAME kerning_flush-left_right-to-left_mode
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_kerningflushleftrighttoleftmode.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_kerningflushleftrighttoleftmode_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
)
add_test(
    NAME kerning_centered_right-to-left_mode_slant
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_kerningcenteredrighttoleftmodeslant.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_kerningcenteredrighttoleftmodeslant_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
)
add_test(
    NAME full-width_flush-right_right-to-left_mode
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_fullwidthflushrightrighttoleftmode.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_fullwidthflushrightrighttoleftmode_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
)
add_test(
    NAME overlap_flush-right_mode_big
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_overlapflushrightmodebig.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_overlapflushrightmodebig_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
)
add_test(
    NAME tlf2_kerning_flush-right_mode
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_tlf2kerningflushrightmode.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_tlf2kerningflushrightmode_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
)
add_test(
    NAME tlf2_overlap_centered_mode
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_tlf2overlapcenteredmode.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_tlf2overlapcenteredmode_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
)
add_test(
    NAME tlf2_full-width_flush-left_right-to-left_mode
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_tlf2fullwidthflushleftrighttoleftmode.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_tlf2fullwidthflushleftrighttoleftmode_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
)
add_test(
    NAME paragraph_mode_long_line_output
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_paragraphmodelonglineoutput.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_paragraphmodelonglineoutput_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
)
add_test(
    NAME short_line_output
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_shortlineoutput.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_shortlineoutput_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
)
add_test(
    NAME kerning_paragraph_centered_mode_small
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_kerningparagraphcenteredmodesmall.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_kerningparagraphcenteredmodesmall_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
)
add_test(
    NAME uskata_control_file
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_uskatacontrolfile.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_uskatacontrolfile_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input_uskata.txt
)
add_test(
    NAME jis0201_control_file
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_jis0201controlfile.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_jis0201controlfile_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input_jis0201.txt
)
add_test(
    NAME right-to-left_smushing_with_JavE_font
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/test_righttoleftsmushingwithjavefont.py ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/test_righttoleftsmushingwithjavefont_res.txt ${CMAKE_CURRENT_SOURCE_DIR}/input.txt
)
