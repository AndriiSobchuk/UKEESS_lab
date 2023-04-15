import ctypes
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
lib_path = os.path.join(dir_path, 'libfib.so')

lib = ctypes.cdll.LoadLibrary(lib_path)

lib.fibonacci.restype = ctypes.c_uint64
lib.fibonacci.argtypes = [ctypes.c_uint64]

n = 10
result = lib.fibonacci(n)
print(f"The {n}th Fibonacci number is {result}")

