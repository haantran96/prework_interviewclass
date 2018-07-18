import numpy as np
def longest_seq(data):
    longest_sq = max(np.split(data, np.where(np.diff(data) !=1)[0]+1), key = len).tolist()
    return longest_sq