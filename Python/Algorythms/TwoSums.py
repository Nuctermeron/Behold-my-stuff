def twoSums(numlist, target):
    h = {} #hash
    for i, num in enumerate(numlist):
        n = target - num
        if n not in h:
            h[num] = i
        else:
            return [h[n], i]
        

numlist = [0,1,3,5,6,9]
target = 9

result = twoSums(numlist,target)
print(result)
    