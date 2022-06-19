import generator as g
import random as r

id = 0 #tracks id of new characters
roster = [] #list of all living characters
resources = { #initialize colony resources
    "Wood": 0,
    "Stone": 0,
    "Bronze": 0,
    "Raw Food": 0,
    "Cooked Food": 0
}

colony = { #initialize colony buildings
    "Houses": 0, #increases pop cap
    "Fire Pits": 0, #allows for cooking/increases skill level of cooking
    "Mines": 0, #increases amount of stone mined
    "Lumber Camps": 0, #increases amount of wood cut
    "Forges": 0, #increases bronze output
}


#event logic
def run_event(roster):
    #runs a set number of random events from the list
    seed = r.randrange(0,6)
    
    #Check skill level, get wood
    if seed == 0:
        for x in roster:
            if x.skills["Forestry"] >= 2 and x.age >= 10:
                resources["Wood"] += 1 * (1+colony["Lumber Camps"])
                x.exp += 10
                print(x.firstname+" "+x.lastname+" has chopped some wood.")
    
    #Check skill level, get stone
    if seed == 1:
        for x in roster:
            if x.skills["Mining"] >= 2 and x.age >= 10:
                resources["Stone"] += 1 * (1+colony["Mines"])
                x.exp += 10
                print(x.firstname+" "+x.lastname+" has mined some stone.")
    
    #Check skill level, smith Bronze                     
    if seed == 2:
        for x in roster:
            if x.skills["Smithing"] >= 2 and resources["Stone"] > 0 and x.age >= 10:
                resources["Stone"] = resources["Stone"] - 1
                resources["Bronze"] += 1 * (1+colony["Forges"])
                x.exp += 10
                print(x.firstname+" "+x.lastname+" has smelted stone into bronze!") #yes thats not how that works who cares
    
    #make a new colonist
    if seed == 3:
        person1 = roster[r.randrange(0,len(roster))]
        person2 = roster[r.randrange(0,len(roster))]
        if person1 != person2 and person1.gender != person2.gender and person1.age >= 10 and person2.age >= 10:
            global id
            baby = g.birth(id, person1.lastname)
            id += 1
            roster.append(baby)
            print(person1.firstname+" "+person1.lastname+" has had a child with "+person2.firstname+" "+person2.lastname+" named "+baby.firstname+" "+baby.lastname+"!")
    
    #two colonists get in a fight
    if seed == 4:
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
    #check skill level, get food
    if seed == 5:
        for x in roster:
            if x.skills["Hunting"] >= 1 and x.age >= 10:
                resources["Raw Food"] += 1
                x.exp += 10
                print(x.firstname+" "+x.lastname+" has hunted for some food.")
    #check skill level, cook food
    if seed == 6:
        for x in roster:
            if x.skills["Cooking"] >= 1 and resources["Raw Food"] >= 1 and x.age >= 10:
                resources["Raw Food"] -= 1
                resources["Cooked Food"] += 1 * (1+colony["Fire Pits"])
                x.exp += 10
                print(x.firstname+" "+x.lastname+" has cooked some food.")

def run_crafting(roster):
    #obtain crafter
    crafter = roster[r.randrange(0,len(roster))]
    #generate seed
    seed = r.randrange(0,5)
    
    #fire pit check
    if seed == 0:
        if crafter.skills["Crafting"] >= 1 and resources["Wood"] >= 2 and colony["Fire Pits"] < 5 and crafter.age >= 10:
            resources["Wood"] = resources["Wood"] - 2
            colony["Fire Pits"] = colony["Fire Pits"] + 1
            print(crafter.firstname+" "+crafter.lastname+" has built a fire pit!")
    
    #house check
    elif seed == 1:
        if crafter.skills["Crafting"] >= 2 and resources["Wood"] >= 10 and colony["Houses"] < 5 and crafter.age >= 10:
            resources["Wood"] = resources["Wood"] - 10
            colony["Houses"] = colony["Houses"] + 1
            print(crafter.firstname+" "+crafter.lastname+" has built a house!")
    
    #lumber camp check
    elif seed == 2:
        if crafter.skills["Crafting"] >= 1 and resources["Wood"] >= 5 and colony["Lumber Camps"] < 5 and crafter.age >= 10:
            resources["Wood"] = resources["Wood"] - 5
            colony["Lumber Camps"] = colony["Lumber Camps"] + 1
            print(crafter.firstname+" "+crafter.lastname+" has built a lumber camp!")
    
    #forge check
    elif seed == 3:
        if crafter.skills["Crafting"] >= 3 and resources["Stone"] >= 10 and resources["Bronze"] >= 2 and colony["Forges"] < 5 and crafter.age >= 10:
            resources["Stone"] = resources["Stone"] - 10
            resources["Bronze"] = resources["Bronze"] - 2
            colony["Forges"] = colony["Forges"] + 1
            print(crafter.firstname+" "+crafter.lastname+" has built a forge!")
    
    #mine check
    else:
        if crafter.skills["Crafting"] >= 1 and resources["Stone"] >= 5 and colony["Mines"] < 5 and crafter.age >= 10:
            resources["Stone"] = resources["Stone"] - 5
            colony["Mines"] = colony["Mines"] + 1
            print(crafter.firstname+" "+crafter.lastname+" has built a mine!")


#spawn in initial colony
for x in range(5):
    x = g.generation(id)
    id += 1
    roster.append(x)




year = 1
game_status = True
#gameplay loop
while game_status: 
    print("Year: "+str(year))
    print("Number of colonists:"+" "+str(len(roster)))
    print("~RESOURCES~")
    print("Wood:"+" "+str(resources["Wood"]))
    print("Stone:"+" "+str(resources["Stone"]))
    print("Bronze:"+" "+str(resources["Bronze"]))
    print("Raw Food:"+" "+str(resources["Raw Food"]))
    print("Cooked Food:"+" "+str(resources["Cooked Food"]))
    print("~BUILDINGS~")
    print("Houses: "+str(colony["Houses"]))
    print("Fire Pits: "+str(colony["Fire Pits"]))
    print("Mines: "+str(colony["Mines"]))
    print("Lumber Camps: "+str(colony["Lumber Camps"]))
    print("Forges: "+str(colony["Forges"]))
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
                print("Skills:\nMelee: "+str(x.skills["Melee"])+"\nCrafting: "+str(x.skills["Crafting"])+"\nForestry: "+str(x.skills["Forestry"])+"\nMining: "+str(x.skills["Mining"])+"\nSmithing: "+str(x.skills["Smithing"])+"\nCharisma: "+str(x.skills["Charisma"])+"\nHunting: "+str(x.skills["Hunting"])+"\nCooking: "+str(x.skills["Cooking"])+"\n")

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
                roll = r.random()
                if roll <= death_chance:
                    print(i.firstname+" "+i.lastname+" has died of natural causes.")
                    roster.remove(i)
        
        #first game over check
        if len(roster) == 0:
            print("Game over! Your colony has ended.")
            i = input("Press anything to end the game.")
            game_status = False
        
        #Event loop
        for x in range(5):
            run_event(roster)

        #Crafting loop
        for x in range(5):
            run_crafting(roster)    

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
                   roll = r.randrange(0,7) 
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
                   elif roll == 5:
                       y.skills["Hunting"] += 1
                   elif roll == 6:
                       y.skills["Cooking"] += 1
                   else:
                       y.skills["Charisma"] += 1


                elif y.clas == "Crafter":
                    y.skills["Crafting"] += 1
                    roll = r.randrange(0,7) 
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
                    elif roll == 5:
                       y.skills["Hunting"] += 1
                    elif roll == 6:
                       y.skills["Cooking"] += 1
                    else:
                        y.skills["Charisma"] += 1

                elif y.clas == "Lumberjack":
                    y.skills["Forestry"] += 1
                    roll = r.randrange(0,7) 
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
                    elif roll == 5:
                       y.skills["Hunting"] += 1
                    elif roll == 6:
                       y.skills["Cooking"] += 1
                    else:
                        y.skills["Charisma"] += 1

                elif y.clas == "Miner":
                    y.skills["Mining"] += 1
                    roll = r.randrange(0,7) 
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
                    elif roll == 5:
                       y.skills["Hunting"] += 1
                    elif roll == 6:
                       y.skills["Cooking"] += 1
                    else:
                        y.skills["Charisma"] += 1

                elif y.clas == "Blacksmith":
                    y.skills["Smithing"] += 1
                    roll = r.randrange(0,7) 
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
                    elif roll == 5:
                       y.skills["Hunting"] += 1
                    elif roll == 6:
                       y.skills["Cooking"] += 1
                    else:
                        y.skills["Charisma"] += 1

                elif y.clas == "Politician":
                    y.skills["Charisma"] += 1
                    roll = r.randrange(0,7) 
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
                    elif roll == 5:
                       y.skills["Hunting"] += 1
                    elif roll == 6:
                       y.skills["Cooking"] += 1
                    else:
                        y.skills["Charisma"] += 1

                print(y.firstname+" "+y.lastname+" has leveled up!")
        #health check
        for y in roster:
            if y.health <= 0:
                print(y.firstname+" "+y.lastname+" has died!")
                roster.remove(y)
        
        #second game over check
        if len(roster) == 0:
            print("Game over! Your colony has ended.")
            i = input("Press anything to end the game.")
            game_status = False

        year += 1