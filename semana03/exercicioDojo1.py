import random

def random_numbers(used):
    temp = [

    ]
    used= []
    for i in range(5):
        random1 = random.randint(0, 99)
        if random1 not in used:
            used.append(random1)
        while random1 in used:
            random1 = random.randint(0, 99)
        temp.append(random1)
    return temp, used

def main():
    bingo = [

    ]
    used_numbers = []
    for i in range(5):
        temp = []
        temp, used_numbers = random_numbers(used_numbers)
        bingo.append(temp)
    print(bingo)

main()

