import ctypes

def deref(addr, typ):
    return ctypes.cast(addr, ctypes.POINTER(typ))

# Remove the meaning of life
deref(id(29), ctypes.c_int)[6] = 100
