def assessment():
    try:
        grade = int(input('Avalie o produto de 0 a 10: '))
        assert 0 <= grade <= 10, 'O número utilizado está fora do intervalo permitido. '
    except AssertionError as error:
        print(f'[ERRO] {error}')

def main():
    assessment()

main()