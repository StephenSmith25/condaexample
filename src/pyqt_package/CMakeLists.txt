set(SIP_SRC _message_box.sip)
set(SRC_FILES message_box.h)
set(MODULE_SPEC ${CMAKE_CURRENT_LIST_DIR}/${SIP_SRC})
find_package(Python ${MINIMUM_PYTHON_VERSION} REQUIRED
             COMPONENTS Interpreter Development NumPy)
set(PYTHON_EXECUTABLE ${Python_EXECUTABLE})
find_package(PyQt5 REQUIRED)
find_package(SIP REQUIRED)
find_package(Qt5 COMPONENTS Core Gui Widgets)

list(APPEND _sip_include_flags "-I${PYQT5_SIP_DIR}")
set(_pyqt_sip_flags -n PyQt5.sip -t WS_X11 -t Qt_5_12_9)
set(_sip_generated_cpp ${CMAKE_CURRENT_BINARY_DIR}/sip_message_boxpart0.cpp
)
set(_sip_include_deps ${PARSED_HEADER_DEPS})
# We also have to deal with the added complication that sip generates code
# that is not C++-17 compatible as it includes throw specifiers. We deal with
# this by replacing them in the generated code.
set(_sip_sanitizer ${CMAKE_CURRENT_LIST_DIR}/sip-sanitize-module.py)
add_custom_command(
OUTPUT ${_sip_generated_cpp}
COMMAND ${SIP_EXECUTABLE} ARGS ${_sip_include_flags} ${_pyqt_sip_flags} -c
        ${CMAKE_CURRENT_BINARY_DIR} -j1 -w -e ${MODULE_SPEC}
COMMAND ${Python_EXECUTABLE} ${_sip_sanitizer} ARGS ${_sip_generated_cpp}
DEPENDS ${MODULE_SPEC} ${_sip_include_deps}
COMMENT "Generating message_box python bindings with sip"
)

add_library(
    _message_box MODULE ${_sip_generated_cpp} ${_sip_include_deps}
)
target_link_libraries(_message_box
  Qt5::Core
  Qt5::Gui
  Qt5::Widgets
)
target_include_directories(
    _message_box SYSTEM PRIVATE ${CMAKE_CURRENT_LIST_DIR} ${SIP_INCLUDE_DIR}
)

file(COPY ${CMAKE_CURRENT_BINARY_DIR}/lib_message_box.so DESTINATION ${CMAKE_CURRENT_LIST_DIR})
file(RENAME ${CMAKE_CURRENT_LIST_DIR}/lib_message_box.so ${CMAKE_CURRENT_LIST_DIR}/_message_box.so)