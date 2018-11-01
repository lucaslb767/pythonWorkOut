places = ['canada','sweden', 'norway', 'egypt', 'antartica']

print(places)

print('\n sorted():', sorted(places))

print('\n actual list:', places)

print('\n reverse sorted():', sorted(places, reverse=True))

print('\n actual list:', places)

places.reverse()

print('\n reversed: ', places)

places.reverse()

print('\n back to normal', places)

places.sort()

print('\n definitely sorted .sort()', places)

places.sort(reverse=True)

print('\n definitely inverted sorted .sort(reverse=True)',places)