def permutation(data):
    if len(data) == 0:
        return []
 
    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(data) == 1:
        return [data] 
    l = [] 
    #place the elements in the first position and using recursive function for the remaining list
    for i in range(len(data)):
        m = data[i]

        remain = data[:i] + data[i+1:]
 
        for p in permutation(remain):
            l.append([m] + p)
    return l
 