from funciones import validar_contraseña
from datos import passwords

if __name__ == '__main__':
    contador = 0
    while True:
        for x in passwords:
            lista_split = x.split(" ")
            if validar_contraseña(lista_split[0],lista_split[1],lista_split[2]):
                contador +=1
        print(contador,"contraseñas son correctas")
        break