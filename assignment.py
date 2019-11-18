#-----------------------------------------------------------------------
#OOP Assignment 
#Ryelee McCoy
#November 8 2019
#
#--------------------------Functions/Lists------------------------------


#--------------------------Actual Code----------------------------------

class Minions:
    
    def __init__(self, level, health, attack):
        self.level = level
        self.health = health
        self.attack = attack
        
    def stats(self):
        print('{} {} {}'.format(self.level, self.health, self.attack))
        
        
class Guard(Minions):
        def __init__(self, level, health, attack, defence):
            super().__init__(level, health, attack)
            self.defence = defence
            
        def stats(self):
            print('{} {} {} {}'.format(self.level, self.health, self.attack, self.defence))

#MINION CLASS
Gremlin = Minions(1, 100, 15)
Brute = Minions(5, 200, 50)

#GUARD CLASS
BossGuard = Guard(10, 500, 75, 125)
AttackerGuard = Guard(12, 400, 150, 75)

Gremlin.stats()
Brute.stats()
BossGuard.stats()
AttackerGuard.stats()