import generator as g
import random as r

id = 0 #tracks id of new characters
roster = [] #list of all living characters
resources = { #initialize colony resources
    "Wood": 0,
    "Stone": 0,
    "Bronze": 0
}

colony = { #initialize colony buildings
    "Houses": 0, #increases pop cap
    "Fire Pits": 0, #allows for cooking/increases skill level of cooking
    "Mines": 0, #increases skill of mining
}


#event logic
def run_event(roster):
    #runs a set number of random events from the list
    seed = r.randrange(0,99)
    #Check skill level, get wood
    if seed in range (0,20):
        for x in roster:
            if x.skills["Forestry"] >= 2:
                resources["Wood"] += 1
                x.exp += 10
                print(x.firstname+" "+x.lastname+" has chopped some wood.")
    #Check skill level, get stone
    if seed in range(21,40):
        for x in roster:
            if x.skills["Mining"] >= 2:
                resources["Stone"] += 1
                x.exp += 10
                print(x.firstname+" "+x.lastname+" has mined some stone.")
    #Check skill level, smith Bronze                     
    if seed in range(41,60):
        for x in roster:
            if x.skills["Smithing"] >= 2 and resources["Stone"] > 0:
                resources["Stone"] = resources["Stone"] - 1
                resources["Bronze"] += 1
                x.exp += 10
                print(x.firstname+" "+x.lastname+" has smelted stone into bronze!") #yes thats not how that works who cares
    #make a new colonist
    if seed in range(61,80):
        person1 = roster[r.randrange(0,len(roster))]
        person2 = roster[r.randrange(0,len(roster))]
        if person1 != person2 and person1.gender != person2.gender:
            global id
            baby = g.birth(id, person1.lastname)
            id += 1
            roster.append(baby)
            print(person1.firstname+" "+person1.lastname+" has had a child with "+person2.firstname+" "+person2.lastname+" named "+baby.firstname+" "+baby.lastname+"!")
    #two colonists get in a fight
    if seed in range(81,100):
        person1 = roster[r.randrange(0,len(roster))]
        person2 = roster[r.randrange(0,len(roster))]
        if person1 != person2: 
            if person1.skills["Melee"] > person2.skills["Melee"]:
                person2.health = person2.health - 10
                person1.exp += 10
                print(person1.firstname+" "+person1.lastname+" got in a fight with "+person2.firstname+" "+person2.lastname+". "+person1.firstname+" "+person1.lastname+" won the fight.")
            elif person1.skills["Melee"] < person2.skills["Melee"]:
                person1.health = person1.health - 10
                person2.exp += 10
                print(person1.firstname+" "+person1.lastname+" got in a fight with "+person2.firstname+" "+person2.lastname+". "+person2.firstname+" "+person2.lastname+" won the fight.")
            else:
                person1.health = person1.health - 10
                person2.health = person2.health - 10
                person1.exp += 10
                person2.exp += 10
                print(person1.firstname+" "+person1.lastname+" got in a fight with "+person2.firstname+" "+person2.lastname+". The fight resulted in a tie.")




#spawn in initial colony
for x in range(5):
    x = g.generation(id)
    id += 1
    roster.append(x)




year = 1
#gameplay loop
while True: 
    print("Year: "+str(year))
    print("Number of colonists:"+" "+str(len(roster)))
    print("~RESOURCES~")
    print("Wood:"+" "+str(resources["Wood"]))
    print("Stone:"+" "+str(resources["Stone"]))
    print("Bronze:"+" "+str(resources["Bronze"]))
    print("~BUILDINGS~")
    print("Houses: "+str(colony["Houses"]))
    print("Fire Pits: "+str(colony["Fire Pits"]))
    print("Mines: "+str(colony["Mines"]))
    print("What would you like to do? \n 1. Roster Lookup \n 2. Proceed with a new year")
    i = input()
    if i == "1":
        for p in roster:
            print(str(p.id) +" "+p.firstname+" "+p.lastname+", a "+p.alignment+" level "+str(p.level)+" "+p.clas+" who is "+str(p.age)+" years old.")
        print("Type the ID of the colonist for an expanded view, otherwise type anything else.")
        i = input()
        for x in roster:
            if i == str(x.id):
                print(x.firstname+" "+x.lastname+", a "+str(x.age)+" year old "+x.alignment+" "+x.clas)
                print("Level "+str(x.level)+", "+str(x.exp)+"/"+str(x.exp_max))
                print("Health "+str(x.health)+"/"+str(x.health_max))
                print("Skills:\nMelee: "+str(x.skills["Melee"])+"\nCrafting: "+str(x.skills["Crafting"])+"\nForestry: "+str(x.skills["Forestry"])+"\nMining: "+str(x.skills["Mining"])+"\nSmithing: "+str(x.skills["Smithing"])+"\nCharisma: "+str(x.skills["Charisma"])+"\n")

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
        #level up check
        for y in roster:
            if y.exp >= y.exp_max:
                #implement new level
                y.level += 1
                y.exp = y.exp - y.exp_max
                y.exp_max += 10
                #get new health
                y.health_max += 10
                y.health = y.health_max
                #insert class logic here
                if y.clas == "Fighter":
                   y.skills["Melee"] += 1
                   roll = r.randrange(0,5) 
                   if roll == 0:
                       y.skills["Melee"] += 1
                   elif roll == 1:
                       y.skills["Crafting"] += 1
                   elif roll == 2:
                       y.skills["Forestry"] += 1
                   elif roll == 3:
                       y.skills["Mining"] += 1
                   elif roll == 4:
                       y.skills["Smithing"] += 1
                   else:
                       y.skills["Charisma"] += 1


                elif y.clas == "Crafter":
                    y.skills["Crafting"] += 1
                    roll = r.randrange(0,5) 
                    if roll == 0:
                        y.skills["Melee"] += 1
                    elif roll == 1:
                        y.skills["Crafting"] += 1
                    elif roll == 2:
                        y.skills["Forestry"] += 1
                    elif roll == 3:
                        y.skills["Mining"] += 1
                    elif roll == 4:
                        y.skills["Smithing"] += 1
                    else:
                        y.skills["Charisma"] += 1

                elif y.clas == "Lumberjack":
                    y.skills["Forestry"] += 1
                    roll = r.randrange(0,5) 
                    if roll == 0:
                        y.skills["Melee"] += 1
                    elif roll == 1:
                        y.skills["Crafting"] += 1
                    elif roll == 2:
                        y.skills["Forestry"] += 1
                    elif roll == 3:
                        y.skills["Mining"] += 1
                    elif roll == 4:
                        y.skills["Smithing"] += 1
                    else:
                        y.skills["Charisma"] += 1

                elif y.clas == "Miner":
                    y.skills["Mining"] += 1
                    roll = r.randrange(0,5) 
                    if roll == 0:
                        y.skills["Melee"] += 1
                    elif roll == 1:
                        y.skills["Crafting"] += 1
                    elif roll == 2:
                        y.skills["Forestry"] += 1
                    elif roll == 3:
                        y.skills["Mining"] += 1
                    elif roll == 4:
                        y.skills["Smithing"] += 1
                    else:
                        y.skills["Charisma"] += 1

                elif y.clas == "Blacksmith":
                    y.skills["Smithing"] += 1
                    roll = r.randrange(0,5) 
                    if roll == 0:
                        y.skills["Melee"] += 1
                    elif roll == 1:
                        y.skills["Crafting"] += 1
                    elif roll == 2:
                        y.skills["Forestry"] += 1
                    elif roll == 3:
                        y.skills["Mining"] += 1
                    elif roll == 4:
                        y.skills["Smithing"] += 1
                    else:
                        y.skills["Charisma"] += 1

                elif y.clas == "Politician":
                    y.skills["Charisma"] += 1
                    roll = r.randrange(0,5) 
                    if roll == 0:
                        y.skills["Melee"] += 1
                    elif roll == 1:
                        y.skills["Crafting"] += 1
                    elif roll == 2:
                        y.skills["Forestry"] += 1
                    elif roll == 3:
                        y.skills["Mining"] += 1
                    elif roll == 4:
                        y.skills["Smithing"] += 1
                    else:
                        y.skills["Charisma"] += 1

                print(y.firstname+" "+y.lastname+" has leveled up!")
        #health check
        for y in roster:
            if y.health <= 0:
                print(y.firstname+" "+y.lastname+" has died!")
                roster.remove(y)
        year += 1