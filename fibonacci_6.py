#!python


#0, 1, 1, 2, 3, 4, 8, 13, 21, ...
def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado

if __name__ == '__main__':
    # Listar os primeiros 20 numeros.
    for fib in fibonacci(20):
        print(fib)
        