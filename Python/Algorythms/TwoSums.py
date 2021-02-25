def twoSums(numlist, target):
    h = {} #hash
    for i, num in enumerate(numlist):
        n = target - num
        if n not in h:
            h[num] = i
        else:
            return [h[n], i]
        

numlist = [4,2,3,6]
target = 6

result = twoSums(numlist,target)
print(result)
    