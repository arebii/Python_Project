import ctypes
from ctypes import windll
libm = windll.msvcrt
libm.cos.argtypes = [ctypes.c_double]
libm.cos.restype = ctypes.c_double

libm.cosf.argtypes = [ctypes.c_float]
libm.cosf.restype = ctypes.c_float

libm.sin.argtypes = [ctypes.c_double]
libm.sin.restype = ctypes.c_double

libm.ceil.argtypes = [ctypes.c_double]
libm.ceil.restype = ctypes.c_double


def cos_func(arg):
    return libm.cos(arg)

def sin_func(arg):
    return libm.sin(arg)
    
    
def cosf_func(arg):
    return libm.cosf(arg)
    
def ceil_func(arg):
    return libm.ceil(arg)
       
    