# Escreva um programa em Python que verifique se uma chave existe ou não em um dicionário. Se a chave existir no
# dicionário, imprima Verdadeiro. Caso contrário, imprima Falso.

def verify(dict):
    verify_key = str(input("Qual chave você quer verificar a existencia? "))
    if verify_key in dict:
        return True
    else:
        return False


def main():
    dict = {
        'teste' : 'teste',
        'teste2' : 'teste2'
    }
    print(verify(dict))

main()