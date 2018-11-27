from pakiet import trygonometria

x = [0, 30, 45, 60, 90]

for degAngle in x:
    try:
        print("tg(%d) = %.3f" % (degAngle, trygonometria.tangent(degAngle)))
    except TypeError:
        print("tg(%d) = %s" % (degAngle, "-"))

    try:
        print("ctg(%d) = %.3f" % (degAngle, trygonometria.cotangent(degAngle)))
    except TypeError:
        print("ctg(%d) = %s" % (degAngle, "-"))

    print("sin(%d) = %.3f" % (degAngle, trygonometria.sine(degAngle)))
    print("cos(%d) = %.3f" % (degAngle, trygonometria.cosine(degAngle)))

print()  # pusta linijka
print("Działa, KURWA!")