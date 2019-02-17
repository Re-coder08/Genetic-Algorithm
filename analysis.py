result = 0
def get_avgofgeneration(generation):
    temp = []
    for vector in generation:
        temp.append(vector[3])

    fitness_total = 0
    for i in temp:
        fitness_total = fitness_total + i

    result = (fitness_total/len(temp))
    result = float("{0:.2f}".format(result))
    return result

def get_bestofgeneration(generation):
    best_of_gen = 0
    worst_of_gen = 100
    best_worst = [0, 0]
    for vector in generation:
        if best_of_gen < vector[3]:
            best_of_gen = vector[3]
            best_worst[0] = vector
        if worst_of_gen > vector[3]:
            worst_of_gen = vector[3]
            best_worst[1] = vector

    return best_of_gen, worst_of_gen, best_worst

def avgofrun(list):
    result = 0
    total = 0
    for i in list:
        total = total + i

    result = (total/len(list))
    return result

def overall_bfit(list):
    temp = []
    for i in list:
        for v in i :
            for p in v:
                temp.append(p)

    return temp
