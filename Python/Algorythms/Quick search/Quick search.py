def quickSort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
        
    greater = []
    lower = []
    
    for item in sequence:
        if item > pivot:
            greater.append(item)
        else:
            lower.append(item)
    return quickSort(lower) + [pivot] +quickSort(greater)



print(quickSort([3,6,1,2,6,7,8,9,2,3,5,4,2]))