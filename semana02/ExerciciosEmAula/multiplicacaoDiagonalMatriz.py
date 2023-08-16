def diagonal_multiplicator(matriz):
    result = 1
    for line in range(len(matriz)):
        for colum in range(len(matriz[line])):
            if line == colum:
                result *= matriz[line][colum]
    return result

def main():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result = diagonal_multiplicator(matriz)
    print(result)


main()
