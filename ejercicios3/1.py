def AreaTriangulo(base,altura):
    resultado = base*altura/2
    return resultado



if __name__=="__main__":
    print("Vamos a calcular el area del triangulo")
    while True:
        try:
            b = int(input("Introduce la base del triangulo: "))
            a = int(input("Introduce la altura del triangulo: "))
            print("El area del triangulo es",AreaTriangulo(b,a))
            break
        except ValueError:
            print("Introduce un numero por favor.")
