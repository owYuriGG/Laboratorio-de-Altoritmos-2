# Utilizando dicionários, crie um programa que simule um caixa eletrônico. O usuário poderá optar pelas seguintes funcionalidades:

# Depositar dinheiro – Usuário pode depositar valor ilimitado, desde que seja positivo;
# Sacar dinheiro – Usuário pode sacar um valor limitado que deve ser validado pelo campo “transaction_limit”;
# Verificar saldo bancário – Usuário pode consultar o saldo atual;
# Histórico de movimentações – Usuário pode consultar todas as movimentações efetuadas;
# Sair – Usuário pode sair do sistema.

import os

def clear():
    os.system("cls")

def menu():
    print("------ Caixa Bancário -------")
    print("1 - Depositar dinheiro")
    print("2 - Sacar dinheiro ")
    print("3 - Verificar saldo bancário")
    print("4 - Histórico de movimentações ")
    print("5 - Sair ")
    while True:
        try:
            opc = int(input("Digite uma opção: "))
            if opc <= 0 or opc >= 6:
                raise ValueError
            return opc
        except ValueError:
            clear()
            print("[ERRO] Valor inválido! ")
            print("------ Caixa Bancário -------")
            print("1 - Depositar dinheiro")
            print("2 - Sacar dinheiro ")
            print("3 - Verificar saldo bancário")
            print("4 - Histórico de movimentações ")
            print("5 - Sair ")
        except BaseException as error:
            clear()
            print(f"[ERRO] Ocorreu um erro: {error}")
            print("------ Caixa Bancário -------")
            print("1 - Depositar dinheiro")
            print("2 - Sacar dinheiro ")
            print("3 - Verificar saldo bancário")
            print("4 - Histórico de movimentações ")
            print("5 - Sair ")

def withdraw(account):
    while True:
        try:
            value = int(input("Digite o valor a ser sacado: "))
            if value <= 0:
                raise ValueError
            if value <= account["transaction_limit"] and value <= account["balance"]:
                account["balance"] -= value
                account["historic"] += [f"Sacados R$ {value}"]
                clear()
                print(f"Você sacou R$ {value} com sucesso! ")
                return account
            else:
                print("O saldo em conta é insuficiente e/ou o valor a ser sacado ultrapassa o limite de transação de sua conta.")
        except ValueError:
            clear()
            print("[ERRO] O valor digitado é inválido!")
        except BaseException as error:
            clear()
            print(f"[ERRO] Um erro ocorreu: {error}")

def deposit(account):
    while True:
        try:
            value = int(input("Digite o valor a ser depositado: "))
            if value <= 0:
                raise ValueError
            account["balance"] += value
            account["historic"] += [f"Depositados R$ {value}"]
            clear()
            print(f"Você depositou R$ {value} com sucesso!")
            return account
        except ValueError:
            clear()
            print("[ERRO] O valor digitado é inválido!")
        except BaseException as error:
            clear()
            print(f"[ERRO] Um erro ocorreu: {error}")

def main():
    account = {
        "balance" : 3000,
        "transaction_limit" : 1000,
        "historic" : ["Depositados R$ 1000", "Sacados R$ 300"]
    }

    while True:
        opc = menu()
        if opc == 1:
            account = deposit(account)
        elif opc == 2:
            account = withdraw(account)
        elif opc == 3:
            clear()
            print(f"Saldo bancário: R$ {account['balance']}")
        elif opc == 4:
            clear()
            print(f"Histórico de transações: {account['historic']}")
        elif opc == 5:
            break

main()
