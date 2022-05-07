import generator as g
import random as r

id = 0 #tracks id of new characters
roster = [] #list of all living characters
resources = { #initialize colony resources
    "Wood": 0,
    "Stone": 0,
    "Bronze": 0
}


#event logic
def run_event(roster):
    #runs a set number of random events from the list
    seed = r.randrange(0,99)
    #Two fall in love
    if seed in range (0,25):
        for x in roster:
            if x.clas == "Lumberjack":
                resources["Wood"] += 1
                #GIVE XP TO PERSON
                print(x.firstname+" "+x.lastname+" has chopped some wood.")
    if seed in range(26,75):
        for x in roster:
            if x.clas == "Miner":
                resources["Stone"] += 1
                #GIVE XP TO PERSON
                print(x.firstname+" "+x.lastname+" has mined some stone.")                     
    if seed in range(76,99):
        print("This is a test result to see if the function is working.")




#spawn in initial colony
for x in range(5):
    x = g.generation(id)
    id += 1
    roster.append(x)





#gameplay loop
while True:
    print("What would you like to do? \n 1. Roster Lookup \n 2. Proceed with a new year")
    i = input()
    if i == "1":
        for p in roster:
            print(str(p.id) +" "+p.firstname+" "+p.lastname+", a "+p.alignment+" level "+str(p.level)+" "+p.clas+" who is "+str(p.age)+" years old.")
    elif i == "2":
        #new year default events
        #Age increase
        for p in roster:
            p.age += 1
        #Natural death chance
        for i in roster:
            if i.age < 65:
                death_chance = 0.05
                roll = r.random()
                if roll <= death_chance:
                    print(i.firstname+" "+i.lastname+" has died of natural causes.")
                    roster.remove(i)
            else:
                death_chance = 0.2
                roll = r.random
                if roll <= death_chance:
                    print(i.firstname+" "+i.lastname+" has died of natural causes.")
                    roster.remove(i)
        #Event loop
        for x in range(5):
            run_event(roster)
