# Escreva uma função que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário,
# onde a chave é a vogal considerada.

def counter(text):
    dict = {
    }
    vowels = 'a', 'e', 'i', 'o', 'u'
    for i in text:
        if i in vowels:
            if i not in dict:
                dict[i] = 1
            elif i in dict:
                dict[i] += 1
    return dict

def main():
    text = str(input("Digite uma frase: "))
    vowels_dict = counter(text)
    print(vowels_dict)

main()
