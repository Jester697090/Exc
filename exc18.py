# Operatory logiczne: and, or, not

import random

def krowy_i_byki():
    print('Witaj w grze "Krowy i byki".')
    p = str(random.randint(1000, 9999))

    while(True):
        q = input('Zgadnij 4-cyfrową liczbę lub wpisz "exit", by wyjść.')

        if q == 'exit':
            return

        try:
            if 1000 <= int(q) <= 9999:
                k = len(set(p).intersection(set(q)))  # nie działa dla zdublowanych cyfr, poprawić
                b = 4 - k
                print('Krowy:', k, 'Byki:', b)

                if q == p:
                    print('Zwycięstwo! Liczba to', p, '.')
                    return

            else:
                print('Za mała, bądź za duża liczba.')

        except ValueError:
            print('Niepoprawne dane wejściowe.')

krowy_i_byki()