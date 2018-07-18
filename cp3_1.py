import numpy as np

def kth_smallest(a, k):
    return np.partition(a, k-1)[k-1]


