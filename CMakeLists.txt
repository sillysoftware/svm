cmake_minimum_required(VERSION 3.10)

project(svm)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra")
set(CMAKE_CXX_STANDARD 17)

set(CMAKE_EXE_LINKER_FLAGS "-L/usr/lib64 -static")

# current vm version and year
# DO NOT CHANGE
# unless you want to :3 this is open source i can't stop you, only guide.
add_compile_definitions(VERSION="0.0.1")
add_compile_definitions(YEAR="2024")

file(GLOB SOURCE_FILES 
    svm/*.c*
)

add_executable(svm ${SOURCE_FILES})
