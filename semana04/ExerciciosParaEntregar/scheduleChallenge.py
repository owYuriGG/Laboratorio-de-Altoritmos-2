# Escreva um programa para armazenar uma agenda de telefones em um dicionário. Cada pessoa pode ter um ou
# mais telefones e a chave do dicionário é o nome da pessoa. Seu programa deve ter as seguintes funções:

# createContact – essa função acrescenta um novo nome na agenda, com um ou mais telefones. Ela deve receber
# como argumentos o nome e os telefones.

# includePhone– essa função acrescenta um telefone em um nome existente na agenda. Caso o nome não exista
# na agenda, você deve perguntar se a pessoa deseja incluí-lo. Caso a resposta seja afirmativa, use a função
# anterior para incluir o novo nome.

# deletePhone – essa função exclui um telefone de uma pessoa que já está na agenda. Se a pessoa tiver apenas
# um telefone, ela deve ser excluída da agenda.

# deleteContact – essa função exclui uma pessoa da agenda.
# getPhones – essa função retorna os telefones de uma pessoa na agenda.

import os

def clear():
    os.system("cls")

def menu():
    print("")
    print("----- Agenda Telefônica -----")
    print("")
    print("1 - Criar contato")
    print("2 - Incluir telefone")
    print("3 - Deletar telefone")
    print("4 - Deletar contato")
    print("5 - Mostrar telefones")
    print("6 - Sair")
    print("")
    print("-----------------------------")
    print("")
    opc = int(input("Escolha uma opção: "))
    return opc

def createContact(schedule):
    if name == 'teste':
        name = str(input("Digite o nome do contato: ")).upper()
    if name in schedule:
        clear()
        print(f"Você já tem um contato com o nome '{name}'!")
        return schedule
    number = int(input(f"Digite o telefone do contato '{name}': "))
    schedule[name] = [number]
    choice = str(input(f"Você deseja adicionar mais telefone ao contato '{name}'? (sim/nao): ")).upper()
    if choice == 'SIM':
        while True:
            clear()
            number = int(input(f"Digite o telefone a ser adicionado ao contato '{name}': "))
            if number in schedule[name]:
                print(f"O contato '{name}' já tem esse telefone! ")
                choice = str(input(f"Você deseja adicionar mais telefone ao contato '{name}'? (sim/nao): ")).upper()
                if choice == 'NAO':
                    clear()
                    print(f"Contato '{name}' criado com suesso!")
                    return schedule
                continue
            schedule[name] += [number]
            choice = str(input(f"Você deseja adicionar mais telefone ao contato '{name}'? (sim/nao): ")).upper()
            if choice == 'NAO':
                clear()
                print(f"Contato '{name}' criado com sucesso! ")
                return schedule
    clear()
    print(f"Contato '{name}' criado com sucesso! ")
    return schedule

def includePhone(schedule):
    name = str(input("Digite o nome do contato: ")).upper()
    if name not in schedule:
        choice = str(input(f"Você não tem nenhum contato com o nome '{name}'! Você deseja adiciona-lo? (sim/nao) ")).upper()
        if choice == 'SIM':
            schedule = createContact(schedule)
            return schedule
        elif choice == 'NAO':
            clear()
            print("Operação cancelada!")
            return schedule
    number = int(input("Digite o telefone a ser adicionado: "))
    if number in schedule[name]:
        clear()
        print(f"O contato '{name}' já tem esse telefone! ")
        return schedule
    schedule[name] += [number]
    clear()
    print(f"O Telefone '{number} foi adicionado ao contato '{name}'! ")
    return schedule

def deletePhone(schedule):
    name = str(input("Digite o nome do contato: ")).upper()
    if name not in schedule:
        clear()
        print(f"Você não tem nenhum contato com o nome '{name}'!")
        return schedule
    number = int(input("Digite o telefone do contato a ser removido: "))
    if number not in schedule[name]:
        clear()
        print(f"O contato '{name}' não tem esse telefone! ")
        return schedule
    if name in schedule:
        if len(schedule[name]) == 1:
            del schedule[name]
            clear()
            print(f"Único telefone do contato '{name}'! Deletando...")
            print(f"Contato '{name}' deletado!")
            return schedule
        elif number in schedule[name]:
            schedule[name].remove(number)
            clear()
            print(f"Telefone '{number}' foi removido do contato '{name}'!")
            return schedule

def deleteContact(schedule):
    name = str(input("Digite o nome do contato a ser removido: ")).upper()
    if name not in schedule:
        clear()
        print(f"Você não tem nenhum contato com o nome '{name}'!")
        return schedule
    del schedule[name]
    clear()
    print(f"Contato '{name}' removido!")
    return schedule

def getPhones(schedule):
    name = str(input("Digite o nome do contato: ")).upper()
    if name not in schedule:
        clear()
        print(f"Você não tem nenhum contato com o nome {name}!")
    clear()
    print(f"Telefones de {name}")
    for key in schedule[name]:
        print(f"--> {key} ")

def main():
    schedule = {}
    while True:
        opc = menu()
        if opc == 1:
            schedule = createContact(schedule)
        elif opc == 2:
            schedule = includePhone(schedule)
        elif opc == 3:
            schedule = deletePhone(schedule)
        elif opc == 4:
            schedule = deleteContact(schedule)
        elif opc == 5:
            getPhones(schedule)
        elif opc == 6:
            break

main()
