from time import sleep


class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutdown', 'running']
    __currentState = __states[0]

    def __str__(self) -> str:
        return "My name is %s and i'm currently %s with a battery level of %s %% and  my current speed is %d km/h !"%(self.__name,self.__currentState,self.__battery_level,self.__current_speed)
    def __init__(self, name):
        if not name =="":
            self.__name = name

    def changeState(self):
        self.__currentState =  self.__states[1] if self.__states[0] else self.__states[0]
        self.__power = not(self.__power)

    def chargeBattery(self):
        if not self.__battery_level == 100:
            print(self.__name + " is charging ...")
            for i in range(101):
                sleep(0.1)
                self.__battery_level=i
                print(self.__name +" is charged at " + str(self.__battery_level) + " %")
            print(self.__name +" has been fully charged")
        else:
            print(self.__name +" is already fully charged !")

    def setCurrentSpeed(self,speed):
        if self.__power:
            self.__current_speed= speed
            print("Speed set at "+ str(self.__current_speed) + " km/h !")
        else:
            print(self.__name + " is not powered on !")

    def getCurrentSpeed(self):
        print("Current speed of " + self.__name + " is " + str(self.__current_speed) + " km/h !")
        return self.__current_speed
    def stop(self):
        print("STOP !!")
        self.__current_speed =0
        self.__power = False;
        self.__currentState = self.__states[0]


def wait_until_valid_input():
    try:
        speed = int(input("Enter wanted speed :\n"))
    except ValueError:
        print("Provide an integer value...")
        return wait_until_valid_input()
    return speed
# ---------------------------------------------
# Main
# ---------------------------------------------
if __name__ =='__main__':
    r1 = Robot(input('Enter robot\'s name :\n'));
    print(r1)
    r1.changeState()
    print(r1)
    r1.chargeBattery()
    print(r1)
    r1.setCurrentSpeed(wait_until_valid_input())
    print(r1)
    r1.stop()
    print(r1)
    r1.chargeBattery()