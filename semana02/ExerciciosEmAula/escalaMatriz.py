#Escreva uma função que recebe uma matriz e um número escalar como entrada e retorna uma nova matriz
#resultante da multiplicação de todos os elementos da matriz pelo escalar

def scale(matriz, scale_value):
    result = []

    for line in range(len(matriz)):
        result.append([])
        for colum in range(len(matriz[line])):
            result[line].append(matriz[line][colum] * scale_value)
            print("Calcular o escalar", matriz[line][colum])
    return result

def main():
    matriz = [
        [5, 32, 5],
        [2, 76, 43],
        [20, 27, 83]
    ]
    result = scale(matriz, 5)
    print(result)

main()
