# 3.Crie um dicionário vazio filmes = {}. Utilize o nome de um filme como chave. E, como valor, outro dicionário
# contendo o vilão e o ano em que o filme foi lançado. Preencha 5 filmes e exiba de forma amigável.

def add_films(films):
    for i in range(5):
        film = str(input("Digite o nome de um filme: "))
        vilain = str(input("Digite o nome do vilão deste filme: "))
        year = str(input("Digite o ano de lançamento deste filme: "))
        films[film] = {f'Vilão do filme: {vilain}', f'Ano de lançamento: {year}'}
    return films

def main():
    films = {
    }
    films = add_films(films)

    print("----- Lista de Filmes -----")
    for key in films:
        print(f"{key} --> {films[key]}")

main()