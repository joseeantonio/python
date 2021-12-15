from funciones_5_1 import validar_contra


if __name__ == '__main__':
    while True:
        try:
            contra = input("Introduce una contraseña")
            if validar_contra(contra):
                print("La contraseña es valida.")
                break
            print("La contraseña no es valida")
        except ValueError:
            print("Una contraseña por favor.")