from funciones import *


if __name__ == '__main__':
    print("""ÓRDENES:
- crear
- listar
- entrenamiento duracion
- consulta duracion
- fin
""")
    lista = []
    while True:
        try:
             entrada = input("Introduce una orden: ")
             if entrada=="crear":
                 denominacion = input("Introduce la denominacion: ")
                 descripcion = input("Introduce la descripcion: ")
                 duracion = int(input("Introduce la duracion: "))
                 if duracion%10==0:
                    estrategias = input("Introduce las estrategias separadas por coma: ")
                    l_estrategias = estrategias.split(",")
                    dic = {"denominacion":denominacion,"descripcion":descripcion,"duracion":duracion,"estrategia":l_estrategias}
                    lista.append(dic)
                 else:
                     print("La duracion debe de ser multiplo de 10.")
             elif entrada == "listar":
                 for diccionario in lista:
                     for clave,valor in diccionario.items():
                         if clave=="estrategia":
                             for x in valor:
                                 print("-",x)
                         elif clave=="denominacion":
                             print(valor,(diccionario["duracion"]))
                         elif clave=="descripcion":
                             print(valor)
             elif entrada=="fin":
                 print("Hasta luego.")
                 break
             else:
                 lista_split = entrada.split(" ")
                 if lista_split[0]=="entrenamiento":
                     if int(lista_split[1])>0 and int(lista_split[1])%10==0:
                         print(entrenamiento(lista,int(lista_split[1])))
                     else:
                        print("La duracion es incorrecta.")
                 if lista_split[0] == "consulta":
                     if int(lista_split[1]) >0 and int(lista_split[1])%10==0:
                         print(filtra_ejercicios(lista,int(lista_split[1])))
                     else:
                        print("La duracion es incorrecta.")
        except ValueError:
            print("Entrada no valida.")