def Euclides_a(a, b):
    if a%b != 0:
        while a%b != 0:
            modulo = a%b
            a = b
            b = modulo
        return modulo
    else:
        return b
    

print(Euclides_a(30, 10))
    