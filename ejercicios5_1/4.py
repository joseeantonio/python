from funciones_5_1 import contrasena_aleatoria, validar_contra

if __name__ == '__main__':
    contador = 0
    while True:
        contraseña = contrasena_aleatoria()
        if validar_contra(contraseña)==False:
            contador+=1
        else:
            print(f"Ha tardado {contador} veces en ser valida")
            break