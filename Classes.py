class Hero():
    # class to create hero for our game

    def __init__ (self, name, level, race):
    # initiate our hero

        self.name = name
        self. level = level
        self.race = race
        self.health = 100

    def ShowHero(self):
        # print all parametra of the hero
        discription  = (self.name + "" + " Level - " + str(self.level) + " Race - " + self.race + " Health - " +
                        str(self.health)).title()
        print(discription)

    def LevelUp(self):
        #Upgrade level of Hero
        self.level = self.level + 1

    def Move(self):
        #Start moving hero
        print (self.name + " start moving...")


#_-----------------------------------------------------

#Creating child class from class Hero

class SuperHero(Hero):
    #class to create super hero
    def __init__(self, name, level, race, magiclevel):
        # initiate our superhero
        super().__init__(name, level, race)
# taking from parent(super) class its argumens and add new arguments
        self.magiclevel = magiclevel
        self.magic = 100

    def MakeMagic(self):
      #use magic
        self.magic = self.magic - 10
    def ShowHero(self):
        discription = (self.name + "" + " Level - " + str(self.level) + " Race - " + self.race + " Health - " +
                       str(self.health) + " Magic = " + str(self.magic)).title()

        print(discription)




# Creating objects of the class Hero

#
# myhero1 = Hero("Andruha", 5, "ruzzke")
#
# myhero2 = Hero("Sanya", 1, "orc")
#
# mysuperhero = SuperHero("Deadpool", 100500, "Marvel", 146)
#
#
# myhero1.ShowHero()
# myhero2.ShowHero()
# myhero1.LevelUp()
# myhero1.ShowHero()
# myhero2.Move()
# mysuperhero.ShowHero()