def czy_pierwsza(n):
    ileDziel = 0

    for d in range(1, n + 1):
        if n % d == 0:
            ileDziel += 1

    if ileDziel == 2:
        return True
    return False

def main():
    try:
        n = int(input('Podaj liczbę do sprawdzenia, czy jest pierwsza: '))
    except ValueError:
        print('Nieprawidłowe dane. Spróbuj jeszcze raz.')
        main()

    odp = czy_pierwsza(n)

    if odp == True:
        print('Liczba', n, 'jest pierwsza.')  # przy takiej konfiguracji print() nie trzeba dodatkowo "spacjować"
    else:
        print('Liczba', n, 'nie jest pierwsza.')

main()