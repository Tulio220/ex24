import random as rnd

def calcula_media(v):   
    """
    Funcao que calcula a media dos valores de uma lista
    """
    if len(v) > 0:
        return sum(v)/len(v)
    else:
        return 0 

def inicializa_lista(quantidade=5):
    lista = []
    for _ in range(quantidade):
        valor = rnd.randint(0,100)
        lista.append(valor)
    return lista

def pesquisar_valor(v, valor):
    """
    Funcao que pesquisa um valor na lista
    """
    if valor in v:
        return f"O valor {valor} está na lista."
    else:
        return f"O valor {valor} não está na lista."

def menu():
    print('='*10)
    print('1- iniciar lista aleatória')
    print('2- calcular média')
    print('3- pesquisar valor')
    print('4- sair')
    return int(input('Digite sua opção: '))

# main
if __name__ == '__main__':
    v = []
    op=0
    while op != 4:
        op = menu()
        if op == 1:
            v = inicializa_lista()
            print(v)
        elif op == 2:
            media = calcula_media(v)
            print(f"A média é {media:.2f}")
        elif op == 3:
            valor_pesquisar = int(input("Digite o valor que deseja pesquisar: "))
            resultado = pesquisar_valor(v, valor_pesquisar)
            print(resultado)
    else:
        print('Saindo....')
