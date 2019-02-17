import random
population = 10

def select(generation):
    new_generation = []

    while population > len(new_generation):
        players = []
        #for _ in range(int((population/2)-1)):
        for _ in range(2):
            players.append(random.choice(generation))
            #print(str(players))
            #print("player1 : " + str(players[0][3:]))
        if players[0][3:] < players[1][3:]:
            new_generation.append(players[0])
        else:
            new_generation.append(players[1])

    #print("new_generation : " + str(new_generation))
    return new_generation

# select(generation)
