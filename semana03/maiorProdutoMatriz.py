# Dado uma matriz de números inteiros positivos de dimensões n x n, onde n >= 5, 
#encontre o maior produto de uma seqüência de 5 números consecutivos 
#(a seqüência pode estar na vertical, na horizontal ou na diagonal principal).

#Por exemplo, a matriz abaixo retorna 32:

# 2 1 1 1 1
# 1 2 1 1 1
# 1 1 2 1 1
# 1 1 1 2 1
# 1 1 1 1 2

def sum(matrix):
    n = len(matrix)
    largest_product = 0

    # Verifica sequências horizontais
    for line in range(n):
        for colum in range(n - 4):
            product = matrix[line][colum] * matrix[line][colum+1] * matrix[line][colum+2] * matrix[line][colum+3] * matrix[line][colum+4]
            largest_product = max(largest_product, product)

    # Verifica sequências verticais
    for line in range(n - 4):
        for colum in range(n):
            product = matrix[line][colum] * matrix[line+1][colum] * matrix[line+2][colum] * matrix[line+3][colum] * matrix[line+4][colum]
            largest_product = max(largest_product, product)

    # Verifica sequências diagonais principais
    for line in range(n - 4):
        for colum in range(n - 4):
            product = matrix[line][colum] * matrix[line+1][colum+1] * matrix[line+2][colum+2] * matrix[line+3][colum+3] * matrix[line+4][colum+4]
            largest_product = max(largest_product, product)
    return largest_product

def main():
    matriz = [
        [2, 1, 1, 1, 1],
        [1, 2, 1, 1, 1],
        [1, 1, 2, 1, 1],
        [1, 1, 1, 2, 1],
        [1, 1, 1, 1, 2]
    ]
    product = sum(matriz)
    print(product)

main()
