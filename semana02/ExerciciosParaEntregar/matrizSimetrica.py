# Escreva uma função que verifica se uma matriz quadrada é simétrica, ou seja, se ela é igual à sua matriz transposta.

def verify(matriz):
    n = len(matriz)
    for i in range(n):
            for j in range(n):
                if matriz[i][j] != matriz[j][i]:
                    return "A matriz não é simétrica!"
    return "A matriz é simétrica!"

def main():
    matriz = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
    ]
    
    print(verify(matriz))

main()
