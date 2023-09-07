# 7. Imagine que você está criando um programa para gerenciar o estoque de produtos em uma loja.
# Você pode usar um dicionário para rastrear os produtos, suas quantidades e preços. Deve permitir:
# Adicionar um produto: Solicite o nome do produto, quantidade em estoque e preço unitário.
# Armazene essas informações em um dicionário dentro do dicionário estoque. 
# Caso o produto já exista, deve somente incrementar o estoque com a quantidade informada.

# Buscar um produto: Solicite o nome do produto e exiba as informações disponíveis, incluindo
# quantidade em estoque e preço unitário. 

# Visualizar todos os produtos: Mostre uma lista de todos os produtos disponíveis, juntamente com
# suas quantidades e preços.

# Vender um produto: Solicite o nome do produto vendido e a quantidade vendida. Atualize a
# quantidade em estoque e calcule o valor total da venda.

# Relatório de Vendas: Mostre um relatório que liste todas as vendas realizadas, incluindo o nome
# do produto, a quantidade vendida e o valor total da venda.

import os

def clear():
    os.system("cls")

def menu():
    print("")
    print("----- Controle de Estoque -----")
    print("1 - Adiconar produto ao estoque")
    print("2 - Buscar produto")
    print("3 - Visualizar todos os produtos")
    print("4 - Vender um produto")
    print("5 - Relatório de vendas")
    print("6 - Sair")
    print("----- Controle de Estoque -----")
    print("")
    option = int(input("Selecione uma opção: "))
    return option

def add_product(stock): #Função para adicionar produto ao estoque
    product = str(input("Digite o nome do produto: "))
    amount = int(input("Digite a quantia de unidades do produto: "))
    #Verifica se o produto já existe em estoque e soma as unidades caso ele já esteja
    if product in stock:
        clear()
        print("Este produto já está cadastrado em estoque! Somando estoque...")
        stock[product]['amout'] += amount
        return stock
    else: 
        price = float(input("Digite o preço de venda do produto: "))
        #Tendo as informações do produto, ele adiciona ao estoque.
        stock[product] = {
            'amount' : amount,
            'price' : price
        }
        clear()
        print("Produto adicionado com sucesso!")
        return stock

def search_product(stock): #Função para buscar um produto e mostrar suas informações
    product = str(input("Digite o nome do produto a ser procurado: "))
    clear()
    #Verificação se há o produto pesquisado em estoque
    if product in stock:
        print("----------")
        print(f"Produto: {product}")
        print(f"Preço de venda: R${stock[product]['price']}")
        print(f"Quantia em estoque: {stock[product]['amount']}")
        print("----------")
    else:
        print("O produto não existe em estoque!")

def see_products(stock): #Função para visualizar todos os produtos em estoque, junto com suas informações
    clear()
    print("----------")
    for product in stock:
        print(f"Produto: {product}")
        print(f"Preço de venda: R${stock[product]['price']}")
        print(f"Quantia em estoque: {stock[product]['amount']}")
        print("----------")

def sell_product(stock, sales_control): #Função para vender um produto
    product = str(input("Digite o nome do produto: "))
    #Verificação se o produto existe
    if product not in stock:
        clear()
        print("Este produto não existem em seu estoque!")
    #Se houver produto em estoque, ele verifica a quantia a ser vendida
    elif product in stock:
        amount = int(input("Qual a quantia a ser vendida? "))
        #Após solicitar a quantia, ele verifica se há estoque o suficiente para realizar a venda
        if stock[product]['amount'] < amount:
            clear()
            print("Estoque insuficiente!")
            return stock, sales_control
        #Se houver estoque suficiente, ele realiza a venda, diminuindo a quantia em estoque
        #calcula o preço, e adiciona ao relatório de vendas,
        else:
            clear()
            stock[product]['amount'] -= amount
            sale_price = amount * stock[product]['price']
            sales_control.append(f"Venda --> {product}, quantia vendida: {amount}, valor da venda: R${sale_price}.")
            print(f"Venda realizada com sucesso! Valor da venda: R${sale_price}, quantia vendida: {amount} {product}")
            return stock, sales_control

def print_sales_control(sales_control): #Função para mostrar o relatório de vendas
    clear()
    for item in sales_control:
        print(item)

def main():
    stock = {
        'batata' : {
            'amount' : 500,
            'price' : 2.50
        },
        'cafe' : {
            'amount' : 50,
            'price' : 5
        },
        'refrigerante' : {
            'amount' : 20,
            'price' : 10
        }
    }
    sales_control = []
    while True:
        option = menu()
        if option == 1:
            stock = add_product(stock)
        elif option == 2:
            search_product(stock)
        elif option == 3:
            see_products(stock)
        elif option == 4:
            stock, sales_control = sell_product(stock, sales_control)
        elif option == 5:
            print_sales_control(sales_control)
        elif option == 6:
            break

main()
