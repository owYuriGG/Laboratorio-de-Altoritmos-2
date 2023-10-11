import math

def input_int(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print("[ERRO] O valor recebido é inválido! ")
        except BaseException as error:
            print(f"[ERRO] Ocorreu um erro: {error}")

def verify_combinations(n, m):
    combinations = math.factorial(n) / (math.factorial(m) * math.factorial(n-m))
    return combinations

def main():
    N = input_int("Digite a quantia de alunos na turma: ") ## N é o número de alunos na turma
    M = input_int("Digite a quantia de alunos no grupo M: ") ##M é o número de alunos em determinado grupo

    combinations = verify_combinations(N, M)
    print(combinations)

main()