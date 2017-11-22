import sys
import scipy as sp
import scipy.stats as spst
import h5py


def gaussian_mixture_cdf(x, means, covars, weights):
    q = sp.sum(weights * spst.norm.cdf(x, means, sp.sqrt(covars)))
    return q


def correct(values, gpl):
    f = h5py.File('FitGMM_gage_GPL1261.h5', 'r')
    W = f['weights']
    M = f['means']
    C = f['covars']
    corrected = []
    for value, means, covars, weights in zip(values, M, C, W):
        corrected.append(gaussian_mixture_cdf(value, means, covars, weights))
    return sp.asarray(corrected)



if __name__ == '__main__':

    # NOTE Specific to GPL1261, q-values, and list of genesets.txt (features must be in this order).

    string = sys.argv[1]
    values = sp.asarray(string.split(','), dtype=float)
    sp.savetxt('out.csv', sp.atleast_2d(correct(values)), delimiter=',')

