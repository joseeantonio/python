from funciones_4_2 import alturas_alumnos



if __name__ == '__main__':
    l = []
    while True:
        try:
            altura = input("Inyroduce una altura: ")
            if altura == "fin":
                mas_setenta, sesenta, cincuenta , menos_cincuenta = alturas_alumnos(l)
                print(f"""{mas_setenta} alumnos mayores de 1.70 m
                      {sesenta} alumnos entre 1.60 m y 170 m
                      {cincuenta} alumnos entre 1.50 m y 1.60 m
                    {menos_cincuenta} alumnos mas bajos de 1.50 m""")
                break
            altura = float(altura)
            if altura<0:
                print("Mayor que 0 por favor.")
            else:
                l.append(altura)
        except ValueError:
            print("Introduce un numero por favor.")