class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutdown', 'running']

    def __str__(self) -> str:
        return "New robot %s created !"%self.name
    def __init__(self, name,currentState):
        self.name = name
        
r1 = Robot('R2D2');
print(r1)