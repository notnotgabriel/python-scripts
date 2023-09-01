print('Média escolar')

subject = input('Digite a matéria: ')

first_period = float(input('Digite sua nota para o primeiro bimestre: '))
second_period = float(input('Digite sua nota para o segundo bimestre: '))
third_period = float(input('Digite sua nota para o terceiro bimestre: '))
fourth_period = float(input('Digite sua nota para o quarto bimestre: '))

average = (first_period + second_period + third_period + fourth_period) / 4

print('Para a matéria', subject, 'sua média foi', average)