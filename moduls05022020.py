import math
import random
import statistics
import keyword

print(math.pow(2, 3))
print(random.randint(1, 99))

nums = [1, 5, 33, 12,46, 33, 2]
print(statistics.mean(nums)) # Среднее
print(statistics.median(nums)) # Медиана
print(statistics.mode(nums)) # Мода

print(keyword.iskeyword('False'))
print(keyword.iskeyword('for'))
print(keyword.iskeyword('tour'))
