# Dado uma lista de números inteiros, agrupe a lista em um conjunto de intervalos
# Exemplo:
# Entrada: 100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150
# Saída: [100-105], [110-111], [113-115], [150]

def group_intervals(list):
    list.sort()
    intervals = []
    start = list[0]
    end = list[0]

    for index in list[1:]:
        if index == end + 1:
            end = index
        else:
            if start == end:
                intervals.append(f"[{start}]")
            else:
                intervals.append(f"[{start}-{end}]")
            start = index
            end = index

    if start == end:
        intervals.append(f"[{start}]")
    else:
        intervals.append(f"[{start}-{end}]")

    return intervals


def main():
    original_numbers = [100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150]
    grouped_list = group_intervals(original_numbers)
    print(grouped_list)

main()
