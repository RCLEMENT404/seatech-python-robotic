"""
    Robot class
    """
from time import sleep
from operator import add

class Robot():
    """
    A Robot with a battery
    """
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutdown', 'running']
    __current_state = __states[0]

    def __str__(self) -> str:
        return f"My name is {self.__name} and i'm currently {self.__current_state} with a battery level of {self.__battery_level} % and  my current speed is {self.__current_speed} km/h !"
    def __init__(self, name):
        if name !="":
            self.__name = name

    def change_state(self):
        """
        Change robot's state from shutdown to running and from running to shutdown
        """
        self.__current_state =  self.__states[1] if self.__states[0] else self.__states[0]
        self.__power = not self.__power

    def charge_battery(self):
        """
        Charge robot's battery to the maximum
        """
        if self.__battery_level != 100:
            print(self.__name + " is charging ...")
            for i in range(101):
                sleep(0.1)
                self.__battery_level=i
                print(self.__name +" is charged at " + str(self.__battery_level) + " %")
            print(self.__name +" has been fully charged")
        else:
            print(self.__name +" is already fully charged !")

    def set_current_speed(self,speed):
        """
        Define the speed of the robot
        """
        if self.__power:
            self.__current_speed= speed
            print("Speed set at "+ str(self.__current_speed) + " km/h !")
        else:
            print(self.__name + " is not powered on !")

    def get_current_speed(self):
        """
        Get the speed of the robot
        """
        print("Current speed of " + self.__name + " is " + str(self.__current_speed) + " km/h !")
        return self.__current_speed
    def stop(self):
        """
        Emergency stop
        """
        print("STOP !!")
        self.__current_speed =0
        self.__power = False
        self.__current_state = self.__states[0]
    @classmethod
    def get_original_name(cls):
        """
        Get the default name of a robot
        """
        print("Original name is "+cls.__name)

    @staticmethod
    def compute_binary(bin1,bin2):
        """
        Compute the sum of 2 binaries
        """
        print("La réponse est " + bin(add(int(bin1,2),int(bin2,2))))

def wait_until_valid_input():
    """
    Function to forbid to enter a string in the asked speed value
    """
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
    r1 = Robot(input('Enter robot\'s name :\n'))
    print(r1)
    r1.change_state()
    print(r1)
    r1.charge_battery()
    print(r1)
    r1.set_current_speed(wait_until_valid_input())
    print(r1)
    r1.stop()
    print(r1)
    r1.charge_battery()
    r1.get_original_name()
    Robot.compute_binary("1101","100")
