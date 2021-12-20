import math


def liquid_volume(h, r=10):
    return ((4 * math.pi * r ** 3) / 3) - ((math.pi * h ** 2 * (3 * r - h)) / 3)


print(liquid_volume(2))
