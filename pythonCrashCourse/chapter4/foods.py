my_foods = ['pizza', 'carrots', 'nuggets']
friends_foods = my_foods[:]

#it is important to make a copy using a slice that cover all of the list, instead of setting friends_foods = my_foods .

#Because, if we just link them, we would not be able to make individual changes, since both of them would redirect to the same list

print('My foods', my_foods)
print('\nfriends foods',friends_foods)

my_foods.append('rabanada')
friends_foods.append('frozen yogurt')

print('My foods', my_foods)
print('\nfriends foods',friends_foods)

