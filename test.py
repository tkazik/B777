# test
import numpy as np


a = 1
b = 2
c = a + b

print(f'a and b is {c}')


msg = "Roll a dice"
print(msg)

nb_rolls = 3
eyes = 0
for x in range(1, nb_rolls+1):
  eyes = np.random.randint(1,6)
  print(f'{x}. roll: {eyes}')


rng = np.random.default_rng()
print(f'10 rolls: {rng.integers(1, 7, size=10)}')
