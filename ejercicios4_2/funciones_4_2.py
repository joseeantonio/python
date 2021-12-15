

def central (n1,n2,n3):
    if n1>=n2 and n1<=n3 or n1<=n2 and n1>=n3:
        return n1
    elif n2>=n1 and n2<=n3 or n2<=n1 and n2>=n3:
        return n2
    else:
        return n3


def raiz_cuadrada(n):
    for x in range(1,n//2):
        if x*x==n:
            return x
        elif x*x>n:
            return x-1


def billete(distancia,dias_estancia):
    if dias_estancia>7 and distancia*2>800:
        return distancia*2*10-(distancia*2*10*30/100)
    else:
        return distancia*2*10


def año_bisiesto(año):
    if año % 4 != 0:
    	return False
    elif año % 4 == 0 and año % 100 != 0:
    	return True
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
    	return False
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
    	return True


def fecha_siguiente(dia,mes,anio):
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12: #controlo meses con 31 dias
        if dia<31:
            dia+=1
        elif dia==31:
            if mes==12:
                dia = 1
                mes = 1
                anio += 1
            else:
                dia = 1
                mes += 1
    elif mes==2: #controlo febrero
        if año_bisiesto(anio):
            if dia<29:
                dia += 1
            else:
                dia = 1
                mes = 3
        else:
            if dia<28:
                dia += 1
            else:
                dia = 1
                mes = 3
    else: #controlo los meses con 30 dias
        if dia<30:
            dia += 1
        else:
            dia = 1
            mes += 1
    return dia,mes,anio


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


def alturas_alumnos(lista):
    uno = []
    dos = []
    tres = []
    cuatro = []
    for x in lista:
        if x >1.70:
            uno.append(x)
        elif x>1.60 and x<=1.70:
            dos.append(x)
        elif x>1.50 and x<=1.60:
            tres.append(x)
        elif x<=1.50:
            cuatro.append(x)
    return len(uno),len(dos),len(tres),len(cuatro)