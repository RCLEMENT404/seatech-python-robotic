from random import randint
from robot import Robot
from human import Human

class Cyborg(Robot, Human):   
    __nuke = False
    def __init__(self, name, sexe, nuke=False):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)
        self.__nuke = nuke
        self.name = name
        self.sexe = sexe
    def __del__(self):
        if self.__nuke == True:
            print("AUTODESTRUCTION COMPLETE")
            print("CASUALTIES: "+ str(randint(1000,10000000)))
        else:
            print("NUKE PAYLOAD HASN'T BEEN FOUND, AUTODESTRUCTION CANCELED")
    def charge(self):
        Robot.chargeBattery(self)

    def status(self):
        print(Robot.__str__(self))
        print(Human.__str__(self))
    def changePayloadStatus(self):
        self.__nuke = not(self.__nuke)
# ---------------------------------------------
# Main
# ---------------------------------------------
if __name__ =='__main__':
    cyborg = Cyborg('Deux Ex Machina', 'M')

    print(cyborg.name, 'sexe', cyborg.sexe)
    print('Charging battery...')
    cyborg.charge()
    cyborg.status()
    cyborg.eat('banana')
    cyborg.eat(['coca', 'chips'])
    cyborg.digest()
    cyborg.changePayloadStatus()
    del cyborg