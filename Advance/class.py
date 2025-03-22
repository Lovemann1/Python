import random
salary_list = random.randint(50000, 100000)

# for every_number in range(10000):
#     every_number = random.randint(50000,100000)

list_ = [random.randint(50000,100000) for _ in range(10000)]

from statistics import mean
print(mean(list_))