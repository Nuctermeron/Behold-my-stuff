def attraction(a,b):
    s= 1
    if b == 0:
        return 1
    else:
        for i in range(b):
            s = s*a
        return s

print(attraction(5,2))