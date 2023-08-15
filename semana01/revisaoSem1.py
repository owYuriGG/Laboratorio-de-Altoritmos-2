#Código para editar listas com números PARES
import os

def limpar():
    os.system("cls")

def menu():
    print("1 - Inserir valor")
    print("2 - Listar valores")
    print("3 - Retirar valores")
    print("4 - Retirar todos os valores")
    print("5 - Mostrar média dos valores")
    print("6 - Sair")
    option = int(input("Digite uma opção: "))
    return option

def insert(list):
    limpar()
    number = int(input("Digite o valor a ser incerido: "))
    if number % 2 != 0:
        print("ERRO!\n")
        return list
    list.append(number)
    limpar()
    print("Pronto!\n")
    return list

def printList(list):
    limpar()
    print(f"{list}\n")

def removeValue(list):
    limpar()
    value = int(input("Digite o valor a ser removido: "))
    count = 0
    for i in list:
        if i == value:
            count += 1
    if count == 0:
        print("ERRO!\n")
        return list
    list.remove(value)
    limpar()
    print("Pronto!\n")
    return list

def removeAllValues(list):
    limpar()
    for i in range(len(list)):
        list.pop()
    limpar()
    print("Pronto!\n")
    return list

def listAvarage(list):
    limpar()
    sum = 0
    for i in list:
        sum += i
    if len(list) == 0:
        print("Pronto!\n")
        return list
    avarage = sum / len(list)
    print(f"A média dos valores na lista é de: {avarage}\n")

def main():
    list= []
    option = 0
    while option != 6:
        option = menu()
        if option  == 1:
            list = insert(list)
        elif option == 2:
            printList(list)
        elif option == 3:
            list = removeValue(list)
        elif option  == 4:
            list = removeAllValues(list)
        elif option == 5:
            listAvarage(list)

main()
