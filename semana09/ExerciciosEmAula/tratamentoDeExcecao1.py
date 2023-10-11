def division(val1, val2):
    try:
        return val1 / val2
    except ZeroDivisionError:
        print("[ERRO] Você não pode dividir um número por zero.")
    except BaseException as error:
        print(f"[ERRO] Ocorreu um erro: {error}")


def input_int(message, canBeZero = True):
    while True:
        try:
            value = int(input(message))

            if not canBeZero and value == 0:
                raise ValueError

            return value
        except ValueError:
            print("[ERRO] O número digitado é inválido! ")
        except BaseException as error:
            print(f"[ERRO] Ocorreu um erro: {error}")


def main():
    try:
        number1 = input_int("Digite o primeiro valor: ")
        number2 = input_int("Digite o segundo valor: ", False)
        if number2 == 0:
            raise ValueError


        result = division(number1, number2)

        print(f"Resultado: {result}")
    except ValueError:
        print("[ERRO] Número informado inválido! ")
    except BaseException as error:
        print(f"[ERRO] Ocorreu um erro: {error}")

main()