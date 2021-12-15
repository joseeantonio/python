from funciones import eliminar_extremos

if __name__ == '__main__':
    lista = []
    juez = 1
    while True:
       try:
           nota = int(input(f"Introduce nota juez {juez}: "))
           juez += 1
           lista.append(nota)
           if juez==9:
               notas = eliminar_extremos(sorted(lista))
               print(*notas)
               break
       except ValueError:
           print("Introduce una nota valida.")