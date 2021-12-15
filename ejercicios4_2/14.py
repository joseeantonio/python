from funciones_4_2 import fecha_siguiente
from funciones_4_2 import validar_fecha


if __name__ == '__main__':
    while True:
        try:
            dia = int(input("Introduce el dia: "))
            mes = int(input("Introduce el mes: "))
            anio = int(input("Introduce el año: "))
            if validar_fecha(dia,mes,anio)==True:
                dia_sig, mes_sig, anio_sig = fecha_siguiente(dia,mes,anio) 
                print(f"{dia_sig}/{mes_sig}/{anio_sig}")
                break
            print("La fecha no es valida.")
        except ValueError:
            print("Introduce un numero por favor.")