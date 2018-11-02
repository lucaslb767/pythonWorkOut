squares =[]

for value in range(1,53):
    square = value**2
    squares.append(square)
    print('The square value of',value,'is',square)

print(squares)

#we can build the same thing by using list comprehensions

squares2 = [value**2 for value in range(1,11)]
print(squares2)
