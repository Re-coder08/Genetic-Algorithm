import evo_ga

def Fitness(vector):
    x1 = vector[0]
    x2 = vector[1]
    x3 = vector[2]
    fitness_result = (x1)*(x1) + (x2)*(x2) + (x3)*(x3)
    vector[3] = float("{0:.2f}".format(fitness_result))
    return vector
