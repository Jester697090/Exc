# Wykomentowanie całego bloku: Ctrl + /
# Odkomentowanie całego bloku: Ctrl + /, gdy jest już wykomentowany.

isArrayGot = False
strArray = input("Podaj liczby naturalne w notacji [,], a zwrócę tylko te parzyste.")

while isArrayGot == False:
    if strArray == "":
        strArray = input("Podaj liczby naturalne w notacji [,], a zwrócę tylko te parzyste.")
    else:
        isArrayGot = True

# Parsowanie inputu
array = []
ts = ""
for c in list(strArray):  # list(s) - zwraca tablicę char-ów ze string-a s
    if ord(c) >= 48 and ord(c) <= 57:  # ord(c) - zwraca nr ASCII znaku c, chr(n) - zwraca znak ASCII o numerze n
        ts = ts + c
        continue
    else:  # w Py else if/elseif to 'elif'
        try:
            array.append(int(ts))
            ts = ""
        except ValueError:
            continue

evenArray = []
for n in array:
    if n % 2 == 0:
        evenArray.append(n)

print(evenArray)