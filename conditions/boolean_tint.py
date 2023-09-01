unit_tint_can_cost = 80
capacity_size_tint = 6
tint_can_size_liters = 18

unit_tint_gallon_cost = 25
tint_gallon_size_liters = 4

can_price_by_liter = unit_tint_can_cost / tint_can_size_liters
gallon_price_by_liter = unit_tint_gallon_cost / tint_gallon_size_liters

area = int(input('what is the size of the area to be painted? '))
# 10 percent more
area = area * 1.1

excesso = area - int(area)
area = int(area)

if excesso > 0:
  area = area + 1

liters = area // capacity_size_tint

print('you will need', liters, 'tint litters')

if area % capacity_size_tint:
  liters = liters + 1

tint_can = liters // tint_can_size_liters
litros_excesso_tint_can = tint_can % tint_can_size_liters

if liters % tint_can_size_liters:
  tint_can = tint_can + 1

tint_gallon = liters // tint_gallon_size_liters

if liters % tint_gallon_size_liters:
  tint_gallon = tint_gallon + 1


print('If you buy only 18 liters tint can')
print('you will need', tint_can, 'tint cans')
print('The total cost is R$', tint_can * unit_tint_can_cost)

print('\n\n')

print('If you buy only 4 liters gallons')
print('you will need', tint_gallon, 'tint gallon')
print('The total cost is R$', tint_gallon * unit_tint_gallon_cost)


print('\n\n')

print('mixing gallons and tint cans')

if litros_excesso_tint_can <= 3*4:
  tint_gallon = litros_excesso_tint_can // 4
  if litros_excesso_tint_can % 4 > 0:
    tint_gallon += 1
else:
  tint_can += 1

total_liters = tint_can * tint_can_size_liters + tint_gallon * tint_gallon_size_liters
total_cost = tint_can * unit_tint_can_cost + tint_gallon * unit_tint_gallon_cost

print('you will need', tint_can, 'tint cans')
print('you will need', tint_gallon, 'tint gallons')
print('with total liters of', total_liters)
print('The total cost is R$', total_cost)