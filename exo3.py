from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map
squared = list(map(lambda x: x*x, numbers))

# filter
even = list(filter(lambda x: x % 2 == 0, numbers))

# reduce
summation = reduce(lambda x, y: x + y, numbers)

print(squared)
print(even)
print(summation)
