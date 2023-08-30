# chave é o nome do item, o valor da chave é a quantia de itens, usar loop while para poder usar e parar a lista
# print('detergente' in shop_list) ---> retorna true se tiver na lista, ou false se nao tiver
# se o item que ele tentar ja estiver na lista, aumentar a quantia deste item.

import os

def clear():
    os.system("cls")

def menu():
    print(" ---- LISTA DE COMPRAS ----")
    print(" 1 - Adicionar Item ")
    print(" 2 - Mostrar lista de compras ")
    print(" 3 - Sair")
    opc = int(input("Selecione uma opção: "))
    clear()
    return opc

def add_item(shop_list):
    item = str(input("Digite o nome do item a ser adicionado na lista: "))
    qtd = int(input("Digite a quantia do item a ser adicionado: "))
    if item in shop_list:        
        shop_list[item] += qtd
        return shop_list
    shop_list[f'{item}'] = qtd
    return shop_list

def main():
    shop_list = {}
    while True:
        opc = menu()
        if opc == 1:
            shop_list = add_item(shop_list)
        elif opc == 2:
            print(f"Sua lista de compras: {shop_list}")
        elif opc == 3:
            break
    print({f'Sua lista de compras: {shop_list}'})

main()
