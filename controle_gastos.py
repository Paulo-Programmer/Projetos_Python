#Descrição: Um aplicativo simples para registrar gastos diários e visualizar o total de despesas do mês.
# Funcionalidades:

# Adicionar um gasto (descrição, valor, data)
# Listar os gastos registrados
# Calcular o total gasto no mês
# Exportar os dados para um arquivo CSV ou JSON

import json

# Nome do arquivo onde os dados serão salvos
arquivo_json = 'gastos_mensais.json'

def carregar_dados():
    try:
        with open(arquivo_json, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_dados(lista):
    with open(arquivo_json, 'w', encoding='utf-8') as f:
        json.dump(lista, f,indent= 4)

lista = carregar_dados()

def adicionar(lista):
    desc = input('Digite a descrição do produto: ').strip()
    if not desc:
        print('A descrição não pode estar vazia')
        return 
    
    try:
        valor = float(input('Digite o valor do gasto: '))
    except  ValueError:
        print('Erro!! Digite um número, por gentileza')
        return
    
    data = input('Digite a data [DD/M/ANO]: ').strip()
    if not data:
        print('preencha a data[d/m/y]')
        return
    
    lista.append({'descrição': desc, 'valor' : valor, 'data': data})
    salvar_dados(lista) #salvar os dados após adicioanr um item
    
    print(f'O item {desc} no valor de {valor} foi adicionado com sucesso!')
 


def listar_gastos(lista):
    if not lista:
        print('A lista de gastos está vazia')
    else:
        print('Listandos os gastos: ')
        for i, item in enumerate(lista, 1):
            descricao = item.get('descrição', 'Sem descrição')
            valor = item.get('valor', 0.0)
            data = item.get('data', 'Data não informada')
            print(f"{i}. {descricao} - R${valor} - Data: {data}")

def remover_gasto(lista):
    listar_gastos(lista)
    try:
        index = int(input('Digite o número do item que desejas remover: ')) - 1
        if 0<= index < len(lista):
            item_lista = lista.pop(index)
            salvar_dados(lista) #salvar os dados após remover
            print(f'O item {item_lista} foi removido com sucesso!\n')
        else:
            print(f'O número {index} não existe na lista!')
    except ValueError:
        print(f'Opção inválida!')

#Função para calcular o total de gastos
def total_gastos(lista):
    if not lista:
        print(f'Lista vázia e sem nenhum gastos')
        return
    total = sum(float(item['valor']) for item in lista)
    print(f'O valor total de gastos é: {total:.2f}')

#Loop principal do programa
while True:
            print("\n===== Lista de Gastos Mensais =====")
            print('1. Adicionar item na Lista')
            print('2. Listar os itens')
            print('3. Remover item na lista!')
            print('4. Total dos gastos Mensais')
            print('5. Sair ')

            opcao = input('Digite a opção que desejas:')

            if opcao == '1':
                adicionar(lista)
            elif opcao == '2':
                listar_gastos(lista)
            elif opcao == '3':
                remover_gasto(lista)
            elif opcao == '4':
                total_gastos(lista)
            elif opcao == '5':
                print('Saindo...')
                break
            else:
                print('Opção inválida, digite uma opção entre 1 a 5!!')
