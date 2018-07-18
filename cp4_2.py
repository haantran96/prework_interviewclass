def next_greater(arr):
    result = []
    for i in range(len(arr)):
 
        next_num = -1
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                next_num = arr[j]
                break
             
        result.append(next_num)
    return result