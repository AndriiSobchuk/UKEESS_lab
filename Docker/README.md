TASK: Python App - Compiled Library: Create a Docker image for a Python app that uses a C library. The C library needs to be compiled from source, and the Python app needs to be able to access the compiled library.

Description:

Here we have three files: 
- Dockerfile (which contains set of instructions based on image python:3.9. In general we install build dependencies for C library, then coping C source code, C library and python code which we will run inside docker container)
- fib.c (which contains C source code, we are going to call inside python app)
- app.py (which contains python code where we are calling C code (wouldn't work without file libfib.so (created inside docker container) and which we are running inside docker container)
- Docker_multi-stage - is directory that contains all presented above files, but Dockerfile here is based on multi-stage build approach, which will reduce image size
