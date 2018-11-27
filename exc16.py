import random

def generator_hasel(n, s):
    # n - ile znaków, s - siła hasła

    if isinstance(n, int) and isinstance(s, int):
        if n < 0:
            print('Ujemna liczba znaków nie jest obsługiwana.')
            return

        h = ''
        c = []

        if s == 1:
            c.extend(range(65, 91))  # wielkie litery
            c.extend(range(97, 123))  # małe litery

            for i in range(n):
                h += chr(c[random.randint(0, len(c) - 1)])

        elif s == 2:
            c.extend(range(48, 58))  # liczby
            c.extend(range(65, 91))  # wielkie litery
            c.extend(range(97, 123))  # małe litery

            for i in range(n):
                h += chr(c[random.randint(0, len(c) - 1)])
        elif s == 3:
            for i in range(n):
                h += chr(random.randint(33, 126))  # liczby, litery i znaki specjalne
        else:
            print('Niepoprawnie wybrano siłę hasła. Dostępne siły: 1, 2, 3.')
            return

        return h

    else:
        print('Niepoprawne dane wejściowe.')
        return

def test():
    for k in range(10):
        print(generator_hasel(10, 3))

test()