

class Character:
   def __init__(self,name,initialHealth):
       self.name = name
       self.Health = initialHealth

   def take_damage(self,damageAmount):
       self.Health = self.Health - damageAmount
       return self.Health

   def __str__(self):
       print(self.name,"(health=",self.Health,")",end="\n")


class Hero(Character):
   def __init__(self,name,initialHealth):
       Character.__init__(self,name,initialHealth)
       self.inventory = []

   def restore_health(self,restoreHealth):
       self.Health = self.Health + restoreHealth

   def add_inventory(self,inventoryItem):
       self.inventory.append(inventoryItem)

   def remove_inventory(self,inventoryItem):
       self.inventory.remove(inventoryItem)

   def get_inventory(self):
       return self.inventory


class Enemy(Character):
   def __init__(self,name,initialHealth,damageAmount):
       Character.__init__(self,name,initialHealth)
       self.damageAmount = damageAmount

if __name__ == "__main__":
   # Create a Hero named “Han” with health of 40.
   Geralt = Hero("Geralt",40)

   # Create an Enemy named “Zombie” with health of 20 and damage of 15.
   Vampire = Enemy("Vampire",20,15)

   # Create an Enemy named “Warewolf” with health of 15 and damage of 10.
   Warewolf = Enemy("Warewolf",15,10)

   # Print “Start:” and then print the three characters.
   print("“Start:")
   Geralt.__str__()
   Vampire.__str__()
   Warewolf.__str__()

   # Print “Battle 1:” and then print the hero and the warewolf.
   print("Battle 1:")
   # The hero damages the warewolf by 10. The warewolf damages the hero by its full damage strength
   Geralt.take_damage(Warewolf.damageAmount)
   Warewolf.take_damage(10)
   Geralt.__str__()
   Warewolf.__str__()

   # Print “Battle 2:” and then print the hero and the zombie.
   print("Battle 2:")
   # An encounter occurs between the hero and the zombie. The hero damages the zombie by 20.
   # The zombie damages the hero by its full damage strength.
   Geralt.take_damage(Vampire.damageAmount)
   Zombie.take_damage(20)
   Geralt.__str__()
   Zombie.__str__()

   # Print “Restore Health” and then print the hero
   print("Restore Health: ")
   Geralt.restore_health(5)
   Geralt.__str__()

   # Print “Inventory:” and then print the hero’s inventory by using the get_inventory method.
   print("Inventory: ")
   Geralt.add_inventory("gold coin")
   Geralt.add_inventory("Vampire Fangs")
   print(Geralt.get_inventory())
