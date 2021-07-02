################################################################
#-------- > EXERCICIO 04 LISTA 01

list = []
def Register(registeredProduct: dict):
    list.append(registeredProduct)
    return
option = int(input('Novo cadastro? 0 - Não     1 - Sim '))
while option == 1:
    newProduct = {}

    newProduct['codigo'] = int(input('Digite o código do produto: '))
    if newProduct['codigo'] == 0:
        print('Código 0, encerrando cadastro de produtos.')
        break
    newProduct['estoque'] = int(input('Quantidade em estoque: '))
    newProduct['min'] = int(input('Quantidade mínima do estoque: '))
    Register(newProduct)
    option = int(input('Novo cadastro?  0 - Não     1 - Sim '))

if len(list) > 0:
    print('Produtos P/ código em ordem crescente:')
    print('---' * 10)
    print("  Código |".center(10), end='')
    print(" Estoque |".center(10), end='')
    print("  Mínimo ".center(10))


    for product in sorted(list, key=lambda item: item['codigo']):
        print(str(product['codigo']).center(9), end='|')
        print(str(product['estoque']).center(9), end='|')
        print(str(product['minimo']).center(9))
    print('---' * 10)
else:
    print('VALOR NULL.')