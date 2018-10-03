from cffi import FFI
ffibuilder = FFI()

# cdef() expects a string listing the C types, functions and
# globals needed from Python. The string follows the C syntax.
ffibuilder.cdef("""
    void solve(double* A, double* b, int n);
""")

# This describes the extension module "_pi_cffi" to produce.
ffibuilder.set_source("_libsolve_cffi",
"""
     #include "libsolve/solve.h"   // the C header of the library
""",
     library_dirs=['./libsolve'],
     runtime_library_dirs=['./libsolve'],
     libraries=['solve'])   # library name, for the linker

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
