
def ask_month(message):
    while True:
        try:
            month = int(input(message))
            if month > 0 and month <= 12:
                return month
            else:
                raise ValueError
        except ValueError:
            print("[ERRO] Valor recebido inválido. ")
        except BaseException as error:
            print(f"[ERRO] Ocorreu um erro: {error}")


def main():
    months = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

    month = ask_month("Digite o número do mês: ")

    print(f"Mês: {months[month-1]}")

main()