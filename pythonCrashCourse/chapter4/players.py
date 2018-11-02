players =['ed', 'gina', 'bill', 'nina', 'trish']

print(players[0:3])

#you can omit the first index to include everything from the begginig till the second index

print(players[:3])

#same with omit the second one, it will include everything starting with the first index

print(players[2:])

#we can use negative index to start from the end also

print(players[-2:])

#we can use the sliced in a for loop

for player in players[:2]:
    print(player)