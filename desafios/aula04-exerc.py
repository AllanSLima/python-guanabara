##Primeiro desafio

#Crie um script Python que leia o nome de uma pessoa a mostra uma mensagem da boas-vindas de acordo com o valor digitado.

nome = input('Qual é seu nome? ')

print('Boas-vindas' , nome + '!')


##Segundo desafio

#Crie um script Python que leia o dia, o mês e o ano da nascimento de uma pessoa e mostra uma mensagem com a data formatada.

dia = input('Em que dia você nasceu? ')
mes = input('Em que mês você nasceu? ')
ano = input('Em que ano você nasceu? ')

print('Olá, ' + nome + ', você nasceu no dia ' + dia + ' de ' + mes + ' de ' + ano + '.')
print('Olá,' , nome + ', você nasceu no dia' , dia , 'de' , mes , 'de' , ano + '.')


##Terceiro desafio

#Crie um script Python que leia dois números e tente mostrar a soma entre eles.

#Este desafio vai dar erro pois com o que foi ensinado na aula não da para resolver.

n1 = input('Digite um numero: ')
n2 = input('Digite outro numero: ')

#Se colocarmos para printar, vai somar duas strings, ou seja, duas mensagens, e não numeros.
print(n1 + n2)


#Para resolver isso devemos indicar o que está sendo digitado pelo usuario, não foi mostrado na aula mas eu pesquisei

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

print(n1 + n2)

#Agora a soma funciona.