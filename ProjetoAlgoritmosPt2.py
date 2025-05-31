#Mensagem de Boas-Vindas
name = 'Sérgio Henrique'
surname = 'Ferreira de Andrade'
print(f'{name} {surname}')

#Menu
print('Menu')
sabor = {'Bife Acebolado', 'Filé de Frango'}
tamanho = {'P', 'M', 'G'}
saborLista = list(sabor) #Transformando o conjunto sabor em uma lista
tamanhoLista = list(tamanho) #Transformando o conjunto tamanho em uma lista

#Mostrando as listas
for item in sabor:
    print(item)
for item in tamanho:
    print(item)

#Escolha do pedido
input('Escolha o sabor: ')
input('Escolha o tamanho: ')