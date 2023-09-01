min = 10
max = 600
valor_saque = int(input('informe o valor do saque: '))


if min <= valor_saque <= 600:
  notas_100 = valor_saque // 100
  valor_saque = valor_saque % 100

  notas_50 = valor_saque // 50
  valor_saque = valor_saque % 50

  notas_10 = valor_saque // 10
  valor_saque = valor_saque % 10

  notas_5 = valor_saque // 5
  valor_saque = valor_saque % 5

  notas_1 = valor_saque // 1
  valor_saque = valor_saque % 1

  if notas_100 > 0:
    print('Qtd de notas 100:', notas_100)
  if notas_50 > 0:
    print('Qtd de notas 50:', notas_50)
  if notas_10 > 0:
    print('Qtd de notas 10:', notas_10)
  if notas_5 > 0:
    print('Qtd de notas 5:', notas_5)
  if notas_1 > 0:
    print('Qtd de notas 1:', notas_1)

else:
  print('saque indisponivel para este valor')