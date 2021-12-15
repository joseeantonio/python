
def año_bisiesto(año):
    if año % 4 != 0:
    	return False
    elif año % 4 == 0 and año % 100 != 0:
    	return True
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
    	return False
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
    	return True



def validar_fecha(dia,mes,anio):
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        if not (dia>0 and dia<=31):
            return False
    elif mes==2:
        if año_bisiesto(anio)==True:
            if not (dia>0 and dia<=29):
                return False
        else:
            if not (dia>0 and dia<=28):
                return False
    else:
        if dia<0 or dia>30:
            return False
    if mes<0 or mes>12:
        return False
    return True

            




if __name__ == '__main__':
    while True:
        try:
            dia = int(input("Introduce el dia: "))
            mes = int(input("Introduce el mes: "))
            anio = int(input("Introduce el año: "))
            if validar_fecha(dia,mes,anio)==False:
                print("La fecha no es valida.")
            else:
                print("La fecha es valida")
                break
        except ValueError:
            print("Introduce un numero por favor.")


