import numpy as np

def iterative_mean(inp: list) -> float:
    average = 0.0
    for i in range(0, len(inp)):
        average = average + ((inp[i] - average) / (i + 1))
    return average




lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print(np.mean(lst))
print(iterative_mean(lst))
