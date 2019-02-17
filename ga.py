import random
import numpy
import rand
import fit
import tournament
import crossover
import mutation
import analysis

generations = 20
run = 20
lowerbound = -1.0
upperbound = 5.0
Pi = 0.8
Pm = 0.1
length = 3
population = 10

def ga(run):
    overall_best_fitness = []
    for r in range(run):
        print("RUN NO : " + str(r) + "------> START")
        generation = init_vectors(population, length)
        print(generation)
        best_of_run = []
        worst_of_run = []
        avg_of_run = []
        i = 0
        for gen in range(generations):
            i = i + 1
            print('Generation : ' + str(gen) + "\n")
            generation = fitness(generation)
            print("Fitness : " + str(generation))
            if i == 10:
                i = 0
                avg_of_generation = []
                best_of_generation = 0
                avg_of_generation = analysis.get_avgofgeneration(generation)
                best_of_generation, worst_of_generation, best_worst = analysis.get_bestofgeneration(generation)
                best_of_run.append(best_worst[0])
                worst_of_run.append(best_worst[1])
                avg_of_run.append(avg_of_generation)
                print("===================================================")
                print("|avg of generation : "+ str(avg_of_generation))
                print("|best of generation :" + str(best_of_generation)+" vector is : "+str(best_worst[0]))
                print("|worst of generation :" + str(worst_of_generation)+" vector is : "+str(best_worst[1]))
                print("===================================================")
            generation = selection(generation)
            generation = crossover_1(generation)
            generation = mutation_1(generation)

        print("RUN NO : " + str(r) + "------> END")
        overall_best_fitness.append(best_of_run)
        print("best_of_run " + str(r)+ " : "+ str(max(best_of_run)))
        print("worst_of_run  " + str(r)+ " : "+ str(min(worst_of_run)))
        print("avg_of_run  " + str(r)+ " :  "+ str(float("{0:.2f}".format(
        (analysis.avgofrun(avg_of_run))))))

    print("\noverall_best_fitness : " + str(max(analysis.overall_bfit(overall_best_fitness))))

def init_vectors(population, length):
    generation = []
    for _ in range(population):
        generation.append(rand.Rand(lowerbound, upperbound, length))

    return generation

def fitness(generation):
    for gen in generation:
        fit.Fitness(gen)

    return generation

def selection(generation):
    new_generation = tournament.select(generation)

    return new_generation

def crossover_1(generation):
    generation = crossover.cross(generation)

    return generation

def mutation_1(generation):
    generation = mutation.mutate(generation)
    return generation

if __name__ == "__main__":
    ga(run)
