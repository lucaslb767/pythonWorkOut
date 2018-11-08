requested_items =['calabresa', 'milho' ]

if requested_items:
    for requested in requested_items:
        print('Adding '+ requested +'.')
    print('\n finished making your pizza')
else:
    print('are you sure you want a plain pizza ?')


##using multiple lists

avaiable_toppings = ['calabresa', 'queijo', 'pepperoni']

requested_toppings = ['calabresa', 'queijo', 'frango']

for requested_topping in requested_toppings:
    if requested_topping in avaiable_toppings:
        print('adding ', requested_topping)
    else:
        print('sorry, topping not available')

print('finished making your pizza')