#makes a new character
import random as r 

#possible attributes
gender = ["Male", "Female"]
m_firstnames = ["George", "John", "Davis"]
f_firstnames = ["Marie", "Susie", "Sarah"]
lastnames = ["Whitebottom", "Ferriss", "Johnson"]
classes = ["Fighter", "Mage", "Ranger", "Merchant", "Politician" ]
alignments = ["Good", "Neutral", "Evil"]

class Character:
  def __init__(self, gender, firstname, lastname, age, level, clas, alignment):
    self.gender = gender
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.level = level
    self.clas = clas
    self.alignment = alignment

#generation

def generation():
    #choose gender
    chose_gender = gender[r.randrange(0,2)]

    #choose first name, based on gender
    if chose_gender == "Male":
        chose_first = m_firstnames[r.randrange(0,3)]
    else:
        chose_first = f_firstnames[r.randrange(0,3)]

    #choose last name
    chose_last = lastnames[r.randrange(0,3)]

    #age is random for now, but later will change for birth events
    chose_age = r.randrange(0,41)

    #choose class
    choose_class = classes[r.randrange(0,5)]

    #choose alignment
    choose_alignment = alignments[r.randrange(0,3)]
    
    generated = Character(chose_gender,chose_first,chose_last,chose_age, 1, choose_class, choose_alignment)
    return generated
