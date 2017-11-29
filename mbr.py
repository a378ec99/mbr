import sys
import numpy as np
import scipy.stats as spst
import h5py
import matplotlib
matplotlib.use('Agg')
import pylab as pl
import seaborn as sb




def gaussian_mixture_cdf(x, means, covars, weights):
    """
    """
    quantile = np.sum(weights * spst.norm.cdf(x, means, np.sqrt(covars)))
    return quantile

    
def gaussian_mixture_pdf(x, means, covars, weights):
    """
    """
    y = np.sum(weights * spst.norm.pdf(x, means, np.sqrt(covars)))
    return y

    
def quantile(q_value, index):
    """
    Maps from q-values to quantiles of such q-values in a database.
    
    NOTE Specific to GPL1261, inpiut of q-values obtained from GAGE and a specific list of gene sets with features in this order (genesets.txt).
    """
    f = h5py.File('FitGMM_gage_GPL1261.h5', 'r')
    weights, means, covars = f['weights'], f['means'], f['covars']
    quantile = gaussian_mixture_cdf(q_value, means[index], covars[index], weights[index])
    return quantile


def density(q_value, index):
    """
    Maps from q-values to quantiles of such q-values in a database.

    NOTE Specific to GPL1261, inpiut of q-values obtained from GAGE and a specific list of gene sets with features in this order (genesets.txt).
    """
    f = h5py.File('FitGMM_gage_GPL1261.h5', 'r')
    weights, means, covars = f['weights'], f['means'], f['covars']
    density = gaussian_mixture_pdf(q_value, means[index], covars[index], weights[index])
    return density


def map_all(q_values):
    """
    """
    quantiles = []
    for index, q_value in enumerate(q_values):
        quantiles.append(quantile(q_value, index))
    return quantiles


    

if __name__ == '__main__':

    #string = sys.argv[1]
    #test_values = np.asarray(str([0.01] * 2682).replace('[', '').replace(']', '').split(','), dtype=float)
    #np.savetxt('out.csv', np.atleast_2d(map_all(test_values)), delimiter=',')

    np.random.seed(42)
    
    X = np.linspace(0.0, 0.5, 1000)
    file_name = 'test'
    fig = pl.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    ax.set_xlabel('density')
    ax.set_xlabel('q-value')
    ax.set_title('Densities of selected q-values in GPL1261')
    ax.set_xlim(0.0, 0.5)
    for index in [693, 2006, 2679, 2674]: # np.random.randint(0, 2781, 3) # first two are very commonly significant, the other two not as much.
        Y = np.asarray([density(x, index=index) for x in X])
        ax.plot(X, Y, '-', label=str(index)) # kde_kws={'shade': True}, ax=ax, color='green'
        ax.fill_between(X, Y, alpha=0.2, color='grey')

    pl.legend()
    
    fig.savefig(file_name, dpi=600)
    
    # TODO Check why p = 0.01 gets more significant and look at relative changes!







    
