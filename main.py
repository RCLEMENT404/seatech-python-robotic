class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutdown', 'running']

    def __str__(self) -> str:
        return "New robot %s created and %s!"%(self.name,self.currentState)
    def __init__(self, name):
        self.name = name
        self.currentState = self.__states[0]
    def changeState(self):
        self.currentState =  self.__states[1] if self.__states[0] else self.__states[0]


r1 = Robot('R2D2');
print(r1)
r1.changeState()
print(r1)