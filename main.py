import numpy as np


def binary_search(low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if mid == x:
            return mid
        elif mid > x:
            return binary_search(low, mid - 1, x)
        else:
            return binary_search(mid + 1, high, x)
    else:
        return -1


left = 0
right = 99

desiredValue = np.random.randint(0, 100)

print(
    f'desired value: {desiredValue} \nguessed value: {binary_search(left, right, desiredValue)}')
