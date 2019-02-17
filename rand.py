import random

def Rand(start, end, num):
    res = []
    for j in range(3):
        res.append(float("{0:.2f}".format(random.uniform(start, end))))
    res.append(-1)
    return res
