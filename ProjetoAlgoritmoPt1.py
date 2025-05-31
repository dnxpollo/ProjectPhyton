#Saudação
print('Welcome to Antedeguemon Store!')
name = input('Enter your name: ')
sobrenome = input('Now, enter your lastname: ')
print(f'Hello, {name}!')

#Coletando as informações sobre a compra
valorDoPedido = input('Qual o valor total? ')
nmrParcelas = input('Em quantas parcelas? ')
juros = 0.00 #iniciando a variável zerada
valorDoPedido = float(valorDoPedido) #O valor do pedido pode ser um número de ponto flutuante
nmrParcelas = int(nmrParcelas) #A quantidade de parcelas precisa ser um número inteiro

#Informação dada no corpo do trabalho
valorDaParcela = valorDoPedido*(1+juros)/nmrParcelas
valorTotalParcelado = valorDaParcela * nmrParcelas


print('Até aqui tudo bem!') #Marcando ponto para saber se o código está correndo bem

if nmrParcelas < 4 :
    juros = 0.00
elif nmrParcelas >= 4 and nmrParcelas <= 6 :
    juros = 0.04
elif nmrParcelas >= 6 and nmrParcelas < 9 :
    juros = 0.08
elif nmrParcelas >= 9 and nmrParcelas < 13 :
    juros = 0.16
elif nmrParcelas >= 13 :
    juros = 0.32
else:
    print(f'Sr.(a) {name}{sobrenome}, entre em contato com nosso telefone para resolver sua situação!')

print(f'O valor de cada parcela é: R$ {valorDaParcela:.2f}')
print(f'O valor total parcelado é: R$ {valorTotalParcelado:.2f}')

print('Até aqui continuamos bem!')




