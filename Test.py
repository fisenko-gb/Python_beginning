import random

numbers = [random.randrange(1, 100, 1) for i in range(5)]

chet = lambda i: not i%2

f = list(filter(lambda i: False if not i%2 else True, numbers))


