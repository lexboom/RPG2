

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
    Geralt = Hero("Geralt",40)
    Geralt.add_inventory("50 gold coins")

   # Vampire Enemy with health of 30 and damage of 20.
    Vampire = Enemy("Vampire",30,20)

   # Create an Enemy named “Werewolf” with health of 15 and damage of 10.
    Werewolf = Enemy("Werewolf",15,10)

   # Print “Start:” and then print the three characters.#
print("“Our Hero Geralt finds himself in Skellige Isles in search of a boat to get him to Novigrad.")
Geralt.__str__()
   ## Talking to the captain ##
print('Press (3) to talk to a captain')
key = int(input())
if key == 3:
    print('What ye bothering me fer?')
    print('Geralt: "I Need a ride to Novigrad"')
    print('''Captain: "That'll cost ye 10 gold"''')
    print('Press (4) to view inventory')
    key2 = int(input())
    if key2 == 4:
        print(Geralt.get_inventory())
        print('Press (5) to buy a fare')
        key3 = int(input())
        if key3 == 5:
            Geralt.remove_inventory("50 gold coins")
            Geralt.add_inventory("40 gold coins")
            print(Geralt.get_inventory())
            print('Geralt Sails his way across the rough seas determined to make it to Novigrad in the hopes of a long awaited reunion with Jennefer')
        else:
          print('Press (5) to buy a fare')
    else:
          print('Press (4) to view inventory')
else:
      print('Press (3) to talk to captain')
      key = int(input())
      if key == 3:
          print('What ye bothering me fer?')
          print('Geralt: "I Need a ride to Novigrad"')
          print('''Captain: "That'll cost ye 10 gold"''')
          print('Press (4) to view inventory')
          key2 = int(input())
          if key2 == 4:
              print(Geralt.get_inventory())
              print('Press (5) to buy a fare')
              key3 = int(input())
              if key3 == 5:
                  Geralt.remove_inventory("50 gold coins")
                  Geralt.add_inventory("40 gold coins")
                  print(Geralt.get_inventory())
                  print(
                      'Geralt Sails his way across the rough seas determined to make it to Novigrad in the hopes of a long awaited reunion with \n Jennefer')
              else:
                  print('Press (5) to buy a fare')
          else:
              print('Press (4) to view inventory')
      else:
          print('OK, you missed the ship your journey must wait for the nest ship')
          exit()

print('Geralt makes his way to the shores of the Mainland. As he and his stead Roach traverse the backwoods paths he can smell \n something is lurking near by. Geralt makes an attempt to speed roach up in an attempt to outrun the mysteryious beast. \n He can hear branches breaking  behind him run from the trees appears a Werewolf. Geralt has no choice but to make a stand against the monster.')

     # Print Battle 1 and then print the hero and the werewolf.
print('Press (2) to attack the Werewolf')
key4 = int(input())
if key4 == 2:
    Geralt.take_damage(Werewolf.damageAmount)
    Werewolf.take_damage(15)
    print(' The Werewolf damages the hero by its full damage strength. Geralt damages the Werewolf critcally')
    Geralt.__str__()
    Werewolf.__str__()
    Geralt.add_inventory("Werewolf Claws")
    print('Geralt picks up Werewolf Claws')
    print("Inventory: ", Geralt.get_inventory())
else:
    print('Press (2) to attack the Werewolf')

##Healing part##
print('Geralt continues on this path to novigrad when he stumbles upon a wormwood tree. Geralt had learned in his time at the school\n of the wolf that wormword could be used for it"'"s healing properties.")
print('To pick and consume the wormwood press (1)')
healing = int(input())
if healing == 1:
    print("Restore Health: ")
    Geralt.restore_health(10)
    Geralt.__str__()
else:
    print('Press (1)')


##Vampire Battle#####


print('Geralt finds himself in a village full of hysterical people. The villagers seemed happy to see Geralt, not a common welcoming \nfor a Witcher. A villager runs up to our hero and grabs him by the shoulder...')
print("Villager: We found a villager yesterday morning dead, pale as a ghost with a strange bite mark on his neck")
print('Geralt: any chance the body is still above ground?')
print('I can take you to it if ye like sire')
print('\n The villager brings the Witcher around to get a glance at the lifeless pale body\n')
print('Geralt: Looks like a Higher Vampire, It will cost you a hefty bag...')
print('Villager: The whole village collected 500 Orens, That is all we have sire.')
print('Geralt: A bit light but I guess it will have to do.')
print('\n Geralt gathered some animal blood to bait the creature, and found a tree to wait in for the moonlight. Geralt awoke to the sounds\n of snarling coming from below. Geralt leaps from the tree landing right in front of the bloodthirsty beast.')

print('\nThe Vampire Strikes Geralt')
Geralt.take_damage(Vampire.damageAmount)
Geralt.__str__()
print('Press (2) to attack the Vampire')
key4 = int(input())
if key4 == 2:
    Vampire.take_damage(20)
    Vampire.__str__()
else:
    print('Press (2) to attack the Vampire')
    key4 = int(input())
    if key4 == 2:
        Vampire.take_damage(20)
        Vampire.__str__()
    else:
        Geralt.take_damage(Vampire.damageAmount)
        print('Geralt was killed. Game over!')
        exit()

print('\nThe Vampire Strikes Geralt')
Geralt.take_damage(10)
Geralt.__str__()
print('Press (2) to attack the Vampire')
key4 = int(input())
if key4 == 2:
    Vampire.take_damage(10)
    Vampire.__str__()
    print('Gerlat drives a stake through the vampires heart wounding it fatally')
    Geralt.__str__()
    # Print “Inventory:” and then print the hero’s inventory by using the get_inventory method.
    print("Inventory: ")
    Geralt.add_inventory("gold coin")
    Geralt.add_inventory("Vampire Fangs")
    print(Geralt.get_inventory())
else:
    Geralt.take_damage(Vampire.damageAmount)
    print('Geralt was killed. Game over!')
    exit()



print("Geralt used his Bounty paid on the Vampire to fund some supplies for his journey westward, towards Jennefer. Hopefully he can make it there \n in one piece. The road to Novigrad is long and full of peril.....")
print("End part 1")


