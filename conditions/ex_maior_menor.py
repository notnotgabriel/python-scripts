"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
a = 2 
b = 1
c = 3


if a >= b >= c:
  maior = a
  menor = c
elif a >= c >= b:
  maior = a
  menor = b
elif b >= a >= c:
  maior = b
  menor = c
elif b >= c >= a:
  maior = b
  menor = a
elif c >= a >= b:
  maior = c
  menor = b
else:
  maior = c
  menor = a

print('maior', maior)
print('menor', menor)
