def fibonacci(n):  # zwraca n-elementową listę kolejnych liczb z ciągu Fibonacciego
    fib = []
    if n == 0:
        return fib
    elif n == 1:
        fib = [1]
        return fib
    elif n == 2:
        fib = [1, 1]
        return fib
    else:
        fib = [1, 1]
        m = 2

        while(m < n):
            fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
            m += 1

        return fib

a = fibonacci(11)
b = range(1, 14)

c = list(set(a).intersection(set(b)))  # takie samo rozwiązanie jak w exc5.py
print(c)