#!python


#0, 1, 1, 2, 3, 4, 8, 13, 21, ...
def fibonacci(quantidade, sequencia=(0, 1)):
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))
    

if __name__ == '__main__':
    # Listar os primeiros 20 numeros.
    for fib in fibonacci(20):
        print(fib)
        