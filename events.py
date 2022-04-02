import core as c

def event_child(roster):
    person1 = "N"
    person2 = "N"
    for i in roster:
        if (i.age >= 18) and (i.age <= 40):
            if person1 == "N":
                person1 = i.firstname #this won't work, we need some sort of ID system



#example events:
# two people have child
# one person gets murdered by another
# town gets attacked, random number of people die/level up

def run_event(num,roster):
    #runs a set number of random events from the list
    pass