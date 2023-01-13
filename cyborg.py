"""
Cyborg Class
"""
from random import randint
from robot import Robot
from human import Human
def securised_action(f):
    """
    A Robot with a battery
    """
    def wrapper(*args):
        obj = args[0]
        if obj.safety_enabled:
            print('Robot is not allowed to do any action... ', str(f))
        else:
            return f(*args)
    return wrapper

class Cyborg(Robot, Human):
    """
    A Robot with a battery
    """
    __nuke = False
    __safety = False
    @property
    def safety_enabled(self):
        """
        Get the safety status
        """
        return self.__safety
    def change_safety(self):
        """
        Change safety status
        """
        self.__safety = not self.__safety
        print("Safety changed to "+ str(self.__safety))
    def __init__(self, name, sexe, nuke=False):
        Robot.__init__(self, name)
        Human.__init__(self, sexe)
        self.__nuke = nuke
        self.name = name
        self.sexe = sexe
    def __del__(self):
        if self.__nuke:
            print("AUTODESTRUCTION COMPLETE")
            print("CASUALTIES: "+ str(randint(1000,10000000)))
        else:
            print("NUKE PAYLOAD HASN'T BEEN FOUND, AUTODESTRUCTION CANCELED")
    def charge(self):
        """
        Charge the cyborg to maximum
        """
        Robot.charge_battery(self)

    def status(self):
        """
        Get status of the cyborg
        """
        print(Robot.__str__(self))
        print(Human.__str__(self))
    @securised_action
    def change_payload_status(self):
        """
        Attach/Detach payload
        """
        self.__nuke = not self.__nuke
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
    cyborg.change_safety()
    cyborg.change_payload_status()
    cyborg.change_safety()
    cyborg.change_payload_status()
    del cyborg
