while True:
    try:
        h = int(input("Horas de trabajo: "))
        c = int(input("Coste por horas: "))
        break
    except ValueError:
        print("Introduce un numero por favor.")
if h>40:
    total = (h-40)*c*1.5+40*c
else:
    total = h*c
print("Importe total:",total)