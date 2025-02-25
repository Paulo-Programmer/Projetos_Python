# 1️⃣ Lista de Compras 🛒
# Descrição: Um sistema onde o usuário pode adicionar, listar e remover itens da lista de compras. 
# Pode incluir a quantidade e o preço estimado para calcular o total.

# Funcionalidades:
# Adicionar item (nome, quantidade, preço estimado)
# Listar itens da compra
# Remover itens
# Salvar e carregar a lista em um arquivo TXT ou JSON
import os
lista_compra = []
total_preco = 0.0
CAMINHO_ARQUIVO = 'lista_compra.txt'

# def total_compra(item):
#     total_preco = +item
#     return total_preco 

#Função para carregar os itens da Lista em um arquivo TXT
def carregar_lista_compra():
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                lista_compra.append(linha.strip())

#Função para salvar os itens na Lista de compra no arquivo TXT
def salvar_lista_compra():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        for itens in lista_compra:
            arquivo.write(itens + '\n')

def adicionar_item():
   
    item = input('Digite o item que desejas adicionar: ')
    lista_compra.append(item)

    qtd_item = input('Digite a qtd do item:')
    preco_item = float(input('Qual o preço do item: '))
    salvar_lista_compra() 
    #salva no arquivo após adicionar
    print(f'O item {item} com a qtd {qtd_item} foi adicionado na Lista de Compra!')

def listar_itens():
    if not lista_compra:
        print('A Lista de compra está vazia!')
    else:
        print('Listando os itens da compra!')
        for i, lista in enumerate(lista_compra, 1):
            print(f'{i}. {lista}')


def remover_item():
    listar_itens()
    try:
        index = int(input('Digite o número do item pra remover')) - 1
        if 0 <= index < len(lista_compra):
            item_removido = lista_compra.pop(index)
            salvar_lista_compra() 
            #salvando no arquivo,após remover
            print(f'O item {item_removido} foi removido com sucesso!')
        else:
            print('Número inválido!')
    except ValueError:
        print('Opção Inválida!')

#Carregar os itens ao iniciar
carregar_lista_compra()
while True:
    print('Lista de Compras!')
    print('1 - Adicionar item na Lista de Compra.')
    print('2 - Listar Itens da compra')
    print('3 - Remover itens da Lista!')
    print('4 - sair ')

    opcao = input('Digite a opção desejada: ')
    if opcao == '1':
        adicionar_item()
        print()
    elif opcao == '2':
        listar_itens()
        print()
    elif opcao == '3':
        remover_item()
        print()
    elif opcao == '4':
        print('Saindo...')
        break
    else:
        print('Opção Inválida!!!')