def imprimir(maximo, atual):
    # condição de parada!
    if atual >= maximo:
        return
    print(atual)
    imprimir(maximo, atual + 1)

imprimir(10, 1)

def imprimir(maximo, atual):
    # condição de parada! 
    if atual < maximo:
        print(atual)
        imprimir(maximo, atual + 1)

imprimir(10, 1)