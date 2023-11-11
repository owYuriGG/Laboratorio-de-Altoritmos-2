class NegativeNumberError(Exception):
    pass

def calcular_raiz_quadrada():
    try:
        number = int(input('digita ai: '))
        if number < 0:
            raise NegativeNumberError("A raiz quadrada de números negativos não é real.")
        else:
            print('A raíz quadrada desse número é: ', number ** 0.5)
    except NegativeNumberError as error:
        print(f'[ERRO] {error}')

def main():
    calcular_raiz_quadrada()

main()