cmake_minimum_required(VERSION 3.10)
project(flutter_cpp_example)

set(CMAKE_CXX_STANDARD 17)

include_directories(${CMAKE_SOURCE_DIR}/flutter)

# add_executable(flutter_cpp_example main.cpp)
# add_executable(respB_example respB.cpp)
add_executable(respA respA.cpp)

# target_link_libraries(flutter_cpp_example)
target_link_libraries(respA)
