
import random

numbers = random.sample(range(100), 10)
print('Original list:', numbers)

odd_numbers = filter(lambda x: x % 2 == 1, numbers)
odd_squares = map(lambda x: x ** 2, odd_numbers)
print('New list:', list(odd_squares))
