def avarage(matriz):
    totalAvarage = 0
    line1Avarage = 0
    line2Avarage = 0
    line3Avarage = 0
    for line in range(len(matriz)):
        for colum in range(len(matriz[line])):
            if line == 0:
                line1Avarage += matriz[line][colum]
                totalAvarage += matriz[line][colum]
            elif line == 1:
                line2Avarage += matriz[line][colum]
                totalAvarage += matriz[line][colum]
            elif line == 2:
                line3Avarage += matriz[line][colum]
                totalAvarage += matriz[line][colum]
    totalAvarage = totalAvarage / 9
    line1Avarage = line1Avarage / 3
    line2Avarage = line2Avarage / 3
    line3Avarage = line3Avarage / 3
    return totalAvarage, line1Avarage, line2Avarage, line3Avarage

def main():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    totalAvarage, line1Avarage, line2Avarage, line3Avarage = avarage(matriz)
    print(f"A média da matriz é: {totalAvarage}, da primeira linha: {line1Avarage}, da segunda: {line2Avarage}, da terceira: {line3Avarage}")

main()