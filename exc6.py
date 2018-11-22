def palindrom():
    s = input("Wpisz napis, by sprawdzić, czy to palindrom.")

    for i in range(len(s) - 1):
        if i == int(len(s) / 2):
            return True
        if s[i] == s[len(s) - 1 - i]:
            continue
        else:
            return False

print(palindrom())

