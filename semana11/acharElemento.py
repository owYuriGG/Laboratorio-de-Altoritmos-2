def find_element(list, index):
    try:
        if index <= (len(list) - 1) and index >= 0:
            print(list[index])
        else:
            raise IndexError
    except IndexError:
        print('[ERRO] O índice dado é inválido! ')

def main():
    list = [1, 2, 3, 4, 5]
    index = int(input('digita o index ai vai: '))
    find_element(list, index)

main()
