from random import randint
from robot import Robot
from human import Human

def SecurisedAction(f):
	
    def wrapper(*args):
	
        obj = args[0]
	
        if obj.safety_enabled:
	
            print('Robot is not allowed to do any action... ', str(f))
	
        else:
	
            return f(*args)
	
    return wrapper

class Cyborg(Robot, Human):   
    __nuke = False
    __safety = False
    @property
    def safety_enabled(self):
	
        return self.__safety
	
    def changeSafety(self):
        self.__safety = not(self.__safety)
        print("Safety changed to "+ str(self.__safety))
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
    @SecurisedAction
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
    cyborg.changeSafety()
    cyborg.changePayloadStatus()
    cyborg.changeSafety()
    cyborg.changePayloadStatus()
    del cyborg