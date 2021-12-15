
def cuenta_caracteres(palabra):
    diccionario = {}
    contador =  0
    letras = ""
    for x in palabra:
        if x in letras:
            contador += 1
            diccionario[x] = contador
        else:
            contador = 1
            diccionario[x] = contador
            letras += x
    return diccionario


def pulsaciones(palabra):
    palabra = palabra.upper()
    dic = {'.': 1, ',': 11, '?': 111, '!': 1111, ':': 11111, 'A': 2, 'B': 22, 'C': 222, 'D': 3, 'E': 33, 'F': 333, 'G': 4,
     'H': 44, 'I': 444, 'J': 5, 'K': 55, 'L': 555, 'M': 6, 'N': 66, 'Ñ': 666, 'O': 6666, 'P': 7, 'Q': 77, 'R': 777,
     'S': 7777, 'T': 8, 'V': 88, 'U': 888, 'W': 9, 'X': 99, 'X': 99, 'Y': 999, 'Z': 9999, ' ': 0}
    dic_palabra = {}
    for letra in palabra:
        for valor, tecla in dic.items():
            if letra==valor:
                dic_palabra[letra] = tecla
    return dic_palabra

def codigo_morse(palabra):
    palabra = palabra.upper()
    dic = {"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---",
           "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.","S":"...","T":"-",
           "U":"..-", "V":"...-", "W":".--","X":"-..-","Y":"-.--","Z":"--..","0":"-----","1":".----","2":"..---",
           "3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----."}
    dic_palabra = {}
    for x in palabra:
        for letra, morse in dic.items():
            if x == letra:
                dic_palabra[x] = morse
    return dic_palabra

def juego_scrabble(palabra):
    palabra = palabra.upper()
    dic = {"A":1,"E":1,"I":1,"L":1,"N":1,"O":1,"R":1,"S":1,"T":1,"U":1,"D":2,"G":1,"B":3,"C":3,
           "M":3,"P":3,"F":4,"H":4,"V":4,"W":4,"Y":4,"K":5,"J":8,"X":8,"Q":10,"Z":10}
    puntuacion = 0
    for x in palabra:
        for letra, punto in dic.items():
            if x == letra:
                 puntuacion += punto
    return puntuacion


