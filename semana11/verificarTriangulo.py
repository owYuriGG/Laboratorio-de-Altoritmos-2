def verify_triangle(side1, side2, side3):
    try:
        if side1 == side2 and side2 == side3:
            print("Esse trinângulo é equilátero.")
        elif side1 != side2 and side2 != side3 and side1 != side3:
            print("Esse triângulo é escaleno.")
        elif (side1 + side2) < side3 or (side2 + side3) < side1 or (side1 + side3) < side2:
            raise ValueError
        elif (side1 == side2) or (side2 == side3) or (side1 == side3):
            print("Esse triângulo é isóceles.")
    except ValueError as error:
        print("[ERRO] Este triângulo tem formato inválido!")

def main():
    side1 = int(input())
    side2 = int(input())
    side3 = int(input())
    verify_triangle(side1, side2, side3)

main()