def invert_list(list):
    reverse = []
    
    index = len(list)

    while index > 0:
        index -= 1
        reverse.append(list[index])
    return reverse

def main():
    normal_list = [1, 2, 3, 4]
    reverse = invert_list(normal_list)
    print(reverse)

main()