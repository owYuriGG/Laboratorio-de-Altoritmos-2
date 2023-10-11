def get_year(message):
    while True:
        try:
            year = int(input(message))
            return year
        except ValueError:
            print("[ERRO] Valor recebido inválido. ")
        except BaseException as error:
            print(f"[ERRO] Ocorreu um erro: {error}")

def verify_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"O ano {year} é bissexto.")
    else:
        print(f"O ano {year} não é bissexto.")

def main():
    year = get_year("Digite o ano: ")
    verify_year(year)

main()
