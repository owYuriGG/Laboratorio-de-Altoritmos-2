def data(library):
    library['name'] = [str(input("Digite seu nome: "))]
    library['age'] = [int(input("Digite sua idade: "))]
    library['sex'] = [str(input("Digite seu sexo: "))]
    library['city'] = [str(input("Digite a cidade em que você mora: "))]
    library['state'] = [str(input("Digite o estado em que você mora: "))]
    return library

def main():
    library = {}
    library = data(library)
    print(library)

main()
