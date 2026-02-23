#Crie um programa que leia dois números e mostra a soma entre eles.

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

s = n1 + n2

print('A soma entre {} e {} é {}'.format(n1, n2, s))


#pulando espaço
print('')


#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo a todas as informações possíveis sobre ele.

var = input('Digite algo: ')
print(type(var))

print('===VERIFICANDO SE É ALFANUMÉRICO===' , var.isalnum())
print(var.isalnum())

print('===VERIFICANDO SE É ALFABETICO===')
print(var.isalpha())

print('===VERIFICANDO SE É DECIMAL===')
print(var.isdecimal())

print('===VERIFICANDO SE É DIGITO===')
print(var.isdigit())

print('===VERIFICANDO SE É ESPAÇO EM BRANCO===')
print(var.isupper())

print('===VERIFICANDO SE É MINUSCULO===')
print(var.islower())

print('===VERIFICANDO SE É PRINTAVEL===')
print(var.isprintable())

print('===VERIFICANDO SE É ESPAÇO EM BRANCO===')
print(var.isspace())
