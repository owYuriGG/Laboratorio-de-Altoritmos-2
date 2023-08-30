# Escreva um programa que lê duas notas de vários alunos e armazena tais notas em um dicionário, onde a chave é
# o nome do aluno. A entrada de dados deve terminar quando for lida uma string vazia como nome. Escreva uma
# função que retorna a média do aluno, dado seu nome.

def note_adder(grades):
    name = '.'
    while True:
        name = input("Informe o nome do aluno: ").upper()
        if name == "":
            print("Saindo...")
            return grades
        note1 = int(input("Digite a 1ª nota do aluno: "))
        note2 = int(input("Digite a 2ª nota do aluno: "))
        grades[name] = note1, note2

def avarage(grades):
    name = str(input("Digite o nome do aluno para verificar a média: ")).upper()
    sum = 0
    grades1 = grades[name]
    for object in grades1:
        sum += object
    avarage = sum/2
    print(f"A média deste aluno é de: {avarage}")

def main():
    grades = {}
    grades = note_adder(grades)
    avarage(grades)

main()

