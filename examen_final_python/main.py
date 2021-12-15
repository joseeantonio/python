from funciones import *

if __name__ == '__main__':
    hoyo_par = {}
    hoyo_golpe = {}
    n_hoyo = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18"]
    while True:
        try:
            entrada = input("Introduce una accion de golf: ")
            lista_split = entrada.split(" ")
            if lista_split[0] in n_hoyo:
                if existe_par(hoyo_par,entrada):
                    if lista_split[1].isdigit()>0:
                        resultados(hoyo_golpe,lista_split[0],lista_split[1])
                        for hoyo,par in hoyo_par.items():
                            if hoyo==lista_split[0]:
                                print(terminologia(lista_split[1],par))
                    else:
                        print("El numero de golpes no es valido")
                else:
                    par = input("Introduce el par: ")
                    if par.isdigit()>0:
                        crear_cambiar(hoyo_par,lista_split[0],par)
                        resultados(hoyo_golpe,lista_split[0],lista_split[1])
                        print(terminologia(lista_split[1],par))
                    else:
                        print("El par no es valido.")
            elif lista_split[0]=="par":
                if lista_split[1] in n_hoyo:
                    if lista_split[2].isdigit()>0:
                        crear_cambiar(hoyo_par, lista_split[1], lista_split[2])
                    else:
                        print("El par no es correcto.")
                else:
                    print("El hoyo debe de estar entre 1 y 18")
            elif entrada == "listado":
                hoyo_par_ordenado = sorted(hoyo_par.items(), key=operator.itemgetter(0))
                print(listado(hoyo_par,hoyo_golpe))
            elif entrada =="resultado":
                print(resultado(hoyo_golpe,hoyo_par))
        except ValueError:
            print("Accion invalida.")