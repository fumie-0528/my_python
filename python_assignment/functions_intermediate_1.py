
import random
def rand_int(min=0, max=100):
    range = max - min
    return round(random.random() * range + min)

print(rand_int())
print(rand_int(max=50))
print(rand_int(min=50))
print(rand_int(min=50, max=150))

# account for any edge cases (eg. min > max, max < 0)

def rand_int(min=50, max=10):
    range = min - max
    return round(random.random() * range + max)

print(rand_int())
print(rand_int(max=5))
print(rand_int(min=70))
print(rand_int(min=500, max=50))


def rand_int(min=-20, max=0):
    range = max - min
    return round(random.random() * range + min)

print(rand_int())
print(rand_int(max=-10))
print(rand_int(min=-30))
print(rand_int(min=-150, max=-50))