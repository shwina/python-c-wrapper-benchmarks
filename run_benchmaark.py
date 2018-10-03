import timeit
import textwrap
import numpy as np

SIZES = [2, 32, 128, 512]

def run_cffi_benchmarks():

    for N in SIZES:
        setup = """
        N = {}
        import numpy as np

        from _libsolve_cffi import ffi, lib

        A = np.random.rand(N, N)
        b = np.random.rand(N)

        pA = ffi.cast("void *", A.ctypes.data)
        pb = ffi.cast("void *", b.ctypes.data)
        """.format(N)
        setup = textwrap.dedent(setup)

        print(timeit.timeit('lib.solve(pA, pb, N)', setup=setup, number=100))

run_cffi_benchmarks()
