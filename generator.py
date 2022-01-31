#makes a new character
import random as r 

#possible attributes
gender = ["Male", "Female"]
m_firstnames = ["George", "John", "Davis"]
f_firstnames = ["Marie", "Susie", "Sarah"]
lastnames = ["Whitebottom", "Ferriss", "Johnson"]

class Character:
  def __init__(self, gender, firstname, lastname, age, level):
    self.gender = gender
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.level = level

#generation

def generation():
    chose_gender = gender[r.randrange(0,2)]

    if chose_gender == "Male":
        chose_first = m_firstnames[r.randrange(0,3)]
    else:
        chose_first = f_firstnames[r.randrange(0,3)]

    chose_last = lastnames[r.randrange(0,3)]

    #age is random for now, but later will change for birth events
    chose_age = str(r.randrange(0,41))
    
    generated = Character(chose_gender,chose_first,chose_last,chose_age, 1)
    return generated
