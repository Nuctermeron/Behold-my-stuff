def factorial(x):
    s= 1
    for i in range(1,x+1):
        s = s*i
    return s


def factorialRec(x):
    if x ==1:
        return x
    else:
        return x * factorialRec(x-1)

print(factorial(5))
print(factorialRec(5))
        
        