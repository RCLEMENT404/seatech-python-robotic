from time import sleep


class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutdown', 'running']

    def __str__(self) -> str:
        return "New robot %s created and %s!"%(self.__name,self.currentState)
    def __init__(self, name):
        self.__name = name
        self.currentState = self.__states[0]
    def changeState(self):
        self.currentState =  self.__states[1] if self.__states[0] else self.__states[0]

    def chargeBattery(self):
        print(self.__name + " is charging ...")
        for i in range(101):
            sleep(0.1)
            self.__battery_level=i
            print(self.__name +" is charged at " + str(self.__battery_level) + " %")
        print(self.__name +" has been fully charged")

r1 = Robot('R2D2');
print(r1)
r1.changeState()
print(r1)
r1.chargeBattery()