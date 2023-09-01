age = int(input('Your age: '))

if age >= 18:
  print('Allowed to drink')
else:
  print('Not allowed to drink')

# falsy
# None, False, [], {}, (), '', "", 0, 0.0

x = int(input('type a number: '))
y = int(input('type other number: '))

if x > y:
  print('x is bigger than y')
elif x == y: 
  print('x is equal to y')
else:
  print('x is lower than y')