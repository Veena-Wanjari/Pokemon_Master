class Pokemon:
  def __init__(self, name, types, level):
    self.name = name
    self.level = 5
    self.types = types
    self.max_health = level * 4
    self.current_health = self.max_health
    self.knocked_out = False
    
  def __repr__(self):
    return f"{self.name}, belongs to {self.types} Pokemon type and has {self.level} level health points." 

#method for reviving after knock out
  def revive(self):
        self.is_knocked_out = False
        # A revived pokemon can't have 0 health. This is a safety precaution. revive() should only be called if the pokemon was given some health, but if it somehow has no health, its health gets set to 1.
        if self.current_health == 0:
            self.current_health = 1
            print(f"{self.name} is revived!") 
    
#method for knocking out Pokemon
  def knock_out(self):
    self.knocked_out = True
    if self.current_health != 0:
        self.current_health = 0
        print(f"{self.name} Pokemon is knocked out !!")
  
#method of taking damage and loosing health points
  def lose_health(self, damage):
      self.current_health -= damage
      if self.current_health <= 0:
         self.current_health = 0
         self.knock_out()
      else:
         print(f"{self.name}'s now has {self.current_health} points of health")

 #method for gaining health points 
  def gain_health(self, healing):
      if self.current_health == 0:
          self.revive()
      self.current_health += healing
      print(f"{self.name} has gained {healing} health points and current health is {self.current_health}")


#Attack between Fire : Water, Fire : Grass and Fire : Fire  
  def attack(self, other_pokemon):
    print("\n")
    print(f"{self.name} ATTACKS {other_pokemon.name}")
    if self.types == "Fire":
      if other_pokemon.types == "Water":
        damage = self.level / 2
        print("Attack not very effective !!")
        
      elif other_pokemon.types == "Grass":
        damage = self.level * 2
        print("Attack is very effective !!")
        
      else:
        damage = self.level
        print("Attack not so very effective")
        

#Attack between Water : Fire, Water : Grass and Water : Water
   
    elif self.types == "Water":      
      if other_pokemon.types == "Fire":
        damage = (10 * self.level) * 2
        print("Attack is very effective !!")
        
      elif other_pokemon.types == "Grass":
        damage = (10 * self.level) / 2
        print("Attack is not very effective !!")
        
      else:
        damage = (10 * self.level)
        print("Attack not so very effective")

#Attack between Grass : Fire, Grass : Water and Grass : Grass
   
    elif self.types == "Grass":
      if other_pokemon.types == "Fire":
        damage = (10 * self.level) / 2
        print("Attack is not very effective !!")
        
      elif other_pokemon.types == "Water":
        damage = (10 * self.level) * 2
        print("Attack is very effective !!")
        
      else:
        damage = (10 * self.level) 
        print("Attack not so very effective") 

    else:
      print("Pokemon Type Not Existed.....") 
    other_pokemon.lose_health(damage)
    

#creating Trainer class

class Trainer:
  def __init__(self, name, pokemons_list, no_of_potions):
    
    self.name = name
    self.pokemons_list = pokemons_list
    self.no_of_potions = no_of_potions
    self.current_pokemon = 0

  
#printing name of trainer, pokemons list and current active pokemoin
  def __repr__(self):
      print("\n")
      print(f"The trainer {self.name} has the following pokemon:")
      for pokemon in self.pokemons_list:
          print(pokemon)
      return f"The current active Pokemon is {self.pokemons_list[self.current_pokemon].name} "
   
    
#use a potion on current pokemon      
  def use_potion(self):
      print(f"{self.pokemons_list[self.current_pokemon].name} has used potions.")
      if self.no_of_potions > 0:
          self.pokemons_list[self.current_pokemon].gain_health(20)
          self.no_of_potions -= 1
          print(f"Potions left: {self.no_of_potions}")      
      else:
          print(f"{self.name}, you have no potions left !!")
 
        
#swtiching pokemon
  def switch_pokemon(self, new_pokemon):
      if new_pokemon < len(self.pokemons_list) and new_pokemon >= 0:
          if self.pokemons_list[new_pokemon].knocked_out == True:
              print("{self.name} Pokemon is knocked out !!")
          elif new_pokemon == self.current_pokemon:
              print(f"{self.name} is already a active pokemon")
          else:
              self.current_pokemon = new_pokemon
              print(f"Now it is {self.name} Pokemon turn ")
              
  def attack_other_trainer(self, other_trainer):
      my_pokemon = self.pokemons_list[self.current_pokemon]
      other_pokemon = other_trainer.pokemons_list[other_trainer.current_pokemon]
      my_pokemon.attack(other_pokemon)
 
# Three classes that are subclasses of Pokemon. Charmander is a fire type, Venusaur is a Grass type and Misty is a Water type.
class Charmander(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Charmander", "Fire", level)

class Venusaur(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Venusaur", "Grass", level)

class Misty(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Misty", "Water", level)    


# Fire = Pokemon("Charmander", "Fire", 10)
# Grass = Pokemon("Venusaur", "Grass", 5)
# Water = Pokemon("Misty", "Water", 6)   


#Pokemons with different levels
a = Charmander(9)
b = Venusaur(5)
c = Misty(8)

trainer1 = Trainer("Erica", [c, b], 10)
trainer2 = Trainer("Pikachu", [a], 14)

print(repr(trainer1))
print(repr(trainer2))


#Testing attack , potion and switch

trainer1.attack_other_trainer(trainer2)
trainer2.attack_other_trainer(trainer1)

trainer1.use_potion()

trainer2.switch_pokemon(1)


