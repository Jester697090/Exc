isNameGot = 0
name = input("Jak się nazywasz?")

while isNameGot == 0:
    if name == "":
        name = input("Przedstaw się, proszę.")
    else:
        print("Witaj, " + name + "!")
        isNameGot = 1


