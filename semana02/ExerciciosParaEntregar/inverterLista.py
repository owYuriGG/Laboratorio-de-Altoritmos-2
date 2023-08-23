# Você deve criar uma função chamada inverter_lista que aceita uma lista como entrada e retorna uma nova lista que é a inversão da lista original. 
# Não é permitido o uso de métodos internos de reversão de listas, como reverse() ou slicing negativo. Você deve criar a lógica de inversão manualmente.

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
