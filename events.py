import random as r


#example events:
# two people have child
# one person gets murdered by another
# town gets attacked, random number of people die/level up

def run_event(roster):
    #runs a set number of random events from the list
    seed = r.randrange(0,99)
    #Two fall in love
    if seed in range (0,50):
        for x in roster:
            for y in roster:
                if (x.alignment == y.alignment) and (x.id != y.id) and (y.id not in x.relationships): #also need to add check if x.relationships[y.id] != 3
                    x.relationships[y.id]=3
                    print(x.firstname+" "+x.lastname+" has fallen in love with "+y.firstname+" "+y.lastname+"!")
                    break #current error: need to set up breaks in such a way that it keeps going even if one already in relationship
            
    if seed in range(51,99):
        print("This is a test result to see if the function is working.")
    
