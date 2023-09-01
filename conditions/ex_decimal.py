"""
Faça um Programa que leia um número inteiro menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.
	Observando os termos no plural a colocação do "e", da vírgula
	entre outros. Exemplo:
	326 = 3 centenas, 2 dezenas e 6 unidades
	12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301,
	101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
num = int(input('type a number less than 1000: '))

if num < 1000:
	hundreds = num // 100
	num = num % 100
	tens = num // 10
	num = num % 10
	ones = num // 1
	
	if hundreds > 1:
		print(hundreds, 'centenas')
	elif hundreds == 1:
		print('1 centena')

	if tens > 1:
		print(tens, 'dezenas')
	elif tens == 1:
		print('1 dezena')

	if ones > 1:
		print(ones, 'unidades')
	elif ones == 1:
		print('1 unidade')
else:
	print('Numero digitado é igual ou maior que 1000')