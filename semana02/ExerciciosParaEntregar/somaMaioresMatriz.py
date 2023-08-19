def sum_highest(matriz):
    highest1 = matriz[0][0]
    highest2 = matriz[1][0]
    highest3 = matriz[2][0]
    for line in range(len(matriz)):
        for colum in range(len(matriz[line])):
            if line == 0:
                if matriz[line][colum] > highest1:
                    highest1 = matriz[line][colum]
            elif line == 1:
                if matriz[line][colum] > highest2:
                    highest2 = matriz[line][colum]
            elif line == 2:
                if matriz[line][colum] > highest3:
                    highest3 = matriz[line][colum]
    sum = highest1 + highest2 + highest3
    return sum

def main():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    sum = sum_highest(matriz)
    print(sum)

main()