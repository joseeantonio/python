
def numeros_perfectos(n):
    lista = []
    for x in range(1,n):
        c = 0
        for y in range(1,x):
            if x%y==0:
                c+=y
        if c==x:
            lista.append(x)
    return lista


def factores(n):
    lista = []
    coma =""
    v = ""
    for x in range(1,n):
        for y in range(1,n):
            if x*y==n:
                v =coma
                v += str(x)
                v += "*"
                v += str(y)
                lista.append(v)
                coma = ", "
    return lista