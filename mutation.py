import random

def mutate(list):
    new_generation = []
    new_vectors = []
    i = 0
    for vector in list:
        temp = []
        for point in vector:
            i = i + 1
            if i <= 3 :
                rand = random.uniform(0.0, 1.0)
                if rand <= 0.1:
                    point = float("{0:.2f}".format(random.uniform(-1.0, 5.0)))
                    temp.append(point)
                else:
                    temp.append(point)
            else:
                temp.append(point)
                i = 0
        new_generation.append(temp)

    return new_generation
