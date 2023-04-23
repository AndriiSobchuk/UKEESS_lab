import ctypes
import os

lib_path = '/libfib.so'  # Update the path to the correct location

lib = ctypes.cdll.LoadLibrary(lib_path)

lib.fibonacci.restype = ctypes.c_uint64
lib.fibonacci.argtypes = [ctypes.c_uint64]

n = 10
result = lib.fibonacci(n)
print(f"The {n}th Fibonacci number is {result}")

