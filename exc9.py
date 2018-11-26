import random

def game():
    los = random.randint(1, 9)
    odp = input('Zgadnij liczbę z przedziału od 1 do 9 lub wpisz "exit", żeby wyjść: ')

    try:
        if odp == 'exit':
            return -1

        if int(odp) == los:
            print('Dokładnie.')
            return 1
        elif int(odp) < los:
            print('Za mało.')
        else:
            print('Za dużo.')

        return 0
    except ValueError:
        game()


def main():
    ileZgad = 0

    while(True):
        odp = int(game())

        if odp == -1:
            print('Zakończono grę. Liczba poprawnych typowań: ', ileZgad)
            break
        else:
            ileZgad = ileZgad + odp

main()