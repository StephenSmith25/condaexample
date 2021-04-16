#
# - Defines macros for dealing with precompiled header files on platforms that
#   support them

# A switch to turn them on and off
#
option ( USE_PRECOMPILED_HEADERS
         "If true, will use precompiled headers on those platforms that support it." ON )

# Instructs the MSVC toolset to use the precompiled header PRECOMPILED_HEADER
# for each source file given in the collection named by SOURCE_VARIABLE_NAME.
function ( enable_precompiled_headers PRECOMPILED_HEADER SOURCE_VARIABLE_NAME )
  if(USE_PRECOMPILED_HEADERS)
      if(MSVC)
        set(files ${${SOURCE_VARIABLE_NAME}})

        # Generate precompiled header translation unit if it is not already present
        get_filename_component(pch_basename ${PRECOMPILED_HEADER} NAME_WE)
        set(pch_abs ${CMAKE_CURRENT_SOURCE_DIR}/${PRECOMPILED_HEADER})
        set(pch_unity ${CMAKE_CURRENT_BINARY_DIR}/${pch_basename}.cpp)
        if ( NOT EXISTS ${pch_unity} )
          file ( WRITE ${pch_unity} "// Precompiled header unity generated by CMake\n")
          file (APPEND ${pch_unity} "#include <${pch_abs}>\n")
        endif()

        # Set this file as source for precompiled header
        set_source_files_properties(${pch_unity}  PROPERTIES COMPILE_FLAGS "/Yc\"${pch_abs}\"")

        # Update properties of source files to use the precompiled header.
        # Additionally, force the inclusion of the precompiled header at beginning of each source file.
        foreach(source_file ${files} )
          set_source_files_properties( ${source_file} PROPERTIES
          COMPILE_FLAGS "/Yu\"${pch_abs}\" /FI\"${pch_abs}\"" )
        endforeach(source_file)

        # Finally, update the source file collection to contain the precompiled header translation unit
        set(${SOURCE_VARIABLE_NAME} ${pch_unity} ${${SOURCE_VARIABLE_NAME}} PARENT_SCOPE)
      endif(MSVC)
  endif(USE_PRECOMPILED_HEADERS)
endfunction(enable_precompiled_headers)