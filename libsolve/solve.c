#include <math.h>
#include <stdlib.h>
#include <lapacke.h>

#include "solve.h"

void solve(double* A, double* b, int n) {
    int info;
    int *ipiv;
    ipiv = (int*) malloc(n*sizeof(int));
    info = LAPACKE_dgesv( LAPACK_ROW_MAJOR, n, 1, A, n, ipiv,
                                    b, 1 );
    free(ipiv);
}
