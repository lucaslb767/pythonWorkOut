pizzas = ['calabresa', 'peperoni', 'frago com catupiry']

for pizza in pizzas:
    print('Probably my favorite pizza is',pizza)

print('I kinda enjoy pizza')


friend_pizzas = pizzas[:]

pizzas.append('ham')
friend_pizzas.append('4 cheese')

print('My favorite pizzas are: ')

for pizza in pizzas:
    print(pizza)

print('My friend favorite pizzas are: ')

for pizza in friend_pizzas:
    print(pizza)