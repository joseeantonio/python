while True:
    try:
        importe = int(input("Introduce el importe sin IVA de un articulo: "))
        iva = int(input("Introduce el IVA a aplicar: "))
        print("El precio total del producto es:",(iva/100)*importe)
        break
    except ValueError:
        print("Introduce un numero por favor")