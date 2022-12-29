import numpy as np

def imstats(a):
    """"
    Returns the statistics of an array.
    Parameters
    ----------
    a: array_like
    Imput data
    Returns
    -------
    d : dictionary
    Number of elements, minimun, maximun, mean, median, standard
    Examples
    --------
    >>> a = np.array([[1, 2], [3, 4]])
    >>> imstats(a)
    """
    x, y = np.shape(a)[0], np.shape(a)[1]
    d = {'npix': x*y, 'min': np.nanmin(a), 'max': np.nanmax(a), 'mean': np.nanmean(a),'median': np.nanmedian(a), 'std': np.nanstd(a)}
    return d