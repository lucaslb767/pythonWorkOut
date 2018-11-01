cars = ['honda', 'mitsubish', 'audi', 'fiat']

print('Here is the original list:', cars)

print('\n here is the sorted list:', sorted(cars))

print('\n here  is the reversed sorted list', sorted(cars,reverse=True))

print('\n here is the original list again:', cars)

cars.reverse()

print('\n here is the reversed list. Not sorted, just the reversed order', cars )

cars.sort()

print(cars)

cars.sort(reverse=True)
print(cars)