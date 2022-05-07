import random as r 

#possible attributes
gender = ["Male", "Female"]
m_firstnames = ["George", "John", "Davis", "Liam", "Noah", "Oliver", "Elijah", "William", "James", "Benjamin", "Lucas", "Henry", "Alexander", "Mason", "Michael", "Ethan", "Daniel", "Jacob", "Logan", "Levi", "Sebastian", "Mateo", "Jack", "Owen", "Theodore"]
f_firstnames = ["Marie", "Susie", "Sarah", "Olivia", "Emma", "Charlotte", "Amelia", "Ava", "Sophia", "Isabella", "Mia", "Evelyn", "Harper", "Luna", "Camila", "Gianna", "Elizabeth", "Eleanor", "Ella", "Abigail", "Sofia", "Avery", "Scarlett", "Emily", "Aria"]
lastnames = ["Whitebottom", "Ferriss", "Johnson", "Smith", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee"]
classes = ["Fighter", "Crafter", "Lumberjack", "Miner", "Blacksmith", "Politician" ]
alignments = ["Good", "Neutral", "Evil"]

#class construction
class Character:
  def __init__(self, id, gender, firstname, lastname, age, level, exp, exp_max, clas, alignment, skills):
    self.id = id
    self.gender = gender
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.level = level
    self.exp = exp
    self.exp_max = exp_max
    self.clas = clas
    self.alignment = alignment
    self.skills = skills

#generation
def generation(id):
    #choose gender
    chose_gender = gender[r.randrange(0,2)]

    #choose first name, based on gender
    if chose_gender == "Male":
        chose_first = m_firstnames[r.randrange(0,24)]
    else:
        chose_first = f_firstnames[r.randrange(0,24)]

    #choose last name
    chose_last = lastnames[r.randrange(0,22)]

    #age is random for now, but later will change for birth events
    chose_age = r.randrange(0,40)

    #choose class
    choose_class = classes[r.randrange(0,5)]

    #skillset based on class
    if choose_class == "Fighter":
        choose_skills = {
            "Melee": 2,
            "Crafting": 0, 
            "Forestry": 0,
            "Mining": 0,
            "Smithing": 1, 
            "Charisma": 0
        }
    elif choose_class == "Crafter":
        choose_skills = {
            "Melee": 0,
            "Crafting": 2, 
            "Forestry": 0,
            "Mining": 0,
            "Smithing": 0, 
            "Charisma": 1
        }
    elif choose_class == "Lumberjack":
        choose_skills = {
            "Melee": 1,
            "Crafting": 0, 
            "Forestry": 2,
            "Mining": 0,
            "Smithing": 0, 
            "Charisma": 0
        }
    elif choose_class == "Miner":
        choose_skills = {
            "Melee": 0,
            "Crafting": 0, 
            "Forestry": 0,
            "Mining": 2,
            "Smithing": 1, 
            "Charisma": 0
        }
    elif choose_class == "Blacksmith":
        choose_skills = {
            "Melee": 0,
            "Crafting": 0, 
            "Forestry": 0,
            "Mining": 1,
            "Smithing": 2, 
            "Charisma": 0
        }
    elif choose_class == "Politician":
        choose_skills = {
            "Melee": 0,
            "Crafting": 1, 
            "Forestry": 0,
            "Mining": 0,
            "Smithing": 0, 
            "Charisma": 2
        }
    #choose alignment
    choose_alignment = alignments[r.randrange(0,3)]
    
    generated = Character(id, chose_gender,chose_first,chose_last,chose_age, 1, 0, 100, choose_class, choose_alignment, choose_skills)
    return generated
