#Código que juntava mensagens da aula anterior, utilizando uma variavel para a soma:

n1 = input('Digite um numero: ')
n2 = input('Digite outro numero: ')
s = n1 + n2
print('A soma vale' , s)

#A junção de duas mensagens é denominada de contatenação

#Podemos printar assim também
print('A soma vale ' + s)
##Ou:
#Este formato é o novo do Python, de preferencia utilzar esse:
print('A soma vale {}'.format(s))


#pulando espaço
print('')


#Agora, vamos arrumar essa soma para de fato somar os numeros, e não somar mensagens.
#Vamos usar a função int, que na verdade é um tipo primitivo.
#No python, temos 4 tipos primitivos:

# int == numeros inteiros
# float == numeros reais ou com pontos flutuantes. Por exemplo: 7.0, 9.5
# bool == valores logicos ou booleanos, ou seja, True ou False
# str == basicamente texto. Lembrando que se tivermos um numero entre aspas, esse numero é tratado como texto. Ex: '7.5'

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
print('A soma vale {}'.format(s))


#pulando espaço
print('')


#Podemos verificar o tipo de uma variavel com a função type:
print('===VERIFICANDO TYPE SENDO STRING===')
n1 = input('Digite um valor: ')
print(type(n1))


#pulando espaço
print('')


#Como não definimos um tipo para esse input, o tipo retorna string. Se definirmos, vai retornar o tipo que definirmos:
print('===VERIFICANDO TYPE SENDO INT===')
n1 = int(input('Digite um valor: '))
print(type(n1))


#pulando espaço
print('')


#Agora vamos colocar os valores de n1 e n2 no meio do texto exibido:
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
print('A soma entre {} e {} é {}'.format(n1, n2, s))


#pulando espaço
print('')


#Se convertemos o valor digitado para float, será adicionado um ponto flutuante na saida do dado:
print('===VERIFICANDO FLOAT===')
n1 = float(input('Digite um numero: '))
print(n1)


#pulando espaço
print('')


#Se convertemos o valor digitado para bool, será verificado se existe algum valor dentro da variavel, se tiver, retorna true
#Se colocarmos espaço inves de digitar um numero, o retorno será false:
print('===VERIFICANDO BOOL===')
n1 = bool(input('Digite um numero: '))
print(n1)


#pulando espaço
print('')


#Podemos verificar se o valor digitado é numerico, é alfabetico, é letra maiuscula, enfim, tem diversas funções dentro de is
print('===VERIFICANDO FUNÇÃO IS===')
n1 = input('Digite algo: ')
print(n1.isnumeric())

#pulando espaço
print('')

print('===VERIFICANDO FUNÇÃO IS SENDO ALPHA===')
n1 = input('Digite algo: ')
print(n1.isalpha())

#pulando espaço
print('')

print('===VERIFICANDO FUNÇÃO IS SENDO ALPHANUM===')
n1 = input('Digite algo: ')
print(n1.isalnum())

#pulando espaço
print('')

print('===VERIFICANDO FUNÇÃO IS SENDO MAIUSCULA===')
n1 = input('Digite algo: ')
print(n1.isupper())
