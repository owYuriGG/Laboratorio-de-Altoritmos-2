
def organizator(list):
    duplicated_itens = []
    normal_list = []
    for i in list:
        counter = 0
        for i2 in list:
            if i2 == i:
                counter += 1
        if counter >= 2:
            if i not in duplicated_itens:
                duplicated_itens.append(i)
                normal_list.append(i)
        elif counter <= 1:
            normal_list.append(i)
    return duplicated_itens, normal_list
            

def main():
    list_duplicated = [1, 1, 2, 3, 4, 4, 5, 6]
    normal_list = []
    duplicated_itens = []
    duplicated_itens, normal_list = organizator(list_duplicated)
    print(duplicated_itens)
    print(normal_list)

main()  