def dzielniki(n):
    D = []
    for l in range(1, n + 1):
        if n % l == 0:
            D.append(l)
    return D

def test():
    a = 24
    b = 72
    c = 133

    print(dzielniki(a))
    print(dzielniki(b))
    print(dzielniki(c))

test()