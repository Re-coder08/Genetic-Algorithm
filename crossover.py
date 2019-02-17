import random
#generation = [[3.27, 0.21, 0.96, -1], [1.27, 2.02, 0.53, -1], [3.82, -0.21, 2.02, -1], [4.06, 2.72, -0.63, -1], [-0.42, 3.87, 4.44, -1], [3.3, 2.95, 3.67, -1], [-0.15, -0.89, 4.75, -1], [0.85, 2.43, -0.28, -1], [4.1, 4.3, -0.73, -1], [2.81, -0.78, 3.83, -1]]
population = 10

def cross(generation):
    new_generation =[]
    for i in range(round(population/2)):
        if i == 0:
            parent1 = generation[0]
            parent2 = generation[1]

        if i == 1:
            parent1 = generation[2]
            parent2 = generation[3]

        if i == 2:
            parent1 = generation[4]
            parent2 = generation[5]

        if i == 3:
            parent1 = generation[6]
            parent2 = generation[7]

        if i == 4:
            parent1 = generation[8]
            parent2 = generation[9]

        child1 = parent1[0:1] + parent2[1:3]
        child1.append(-1)
        new_generation.append(child1)
        child2 = parent2[0:1] + parent1[1:3]
        child2.append(-1)
        new_generation.append(child2)

    return new_generation
