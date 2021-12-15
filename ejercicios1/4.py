while True:
    try:
        g_celius = int(input("Introduzca grados Celsius: "))
        print(g_celius,"grados Celius ,equivale a,",(g_celius*1.8)+32,"grados Fahrenheit")
        break
    except ValueError:
        print("Introduzca un numero por favor") 