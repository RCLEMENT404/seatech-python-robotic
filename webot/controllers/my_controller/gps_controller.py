from controller import GPS
class Gps_controller():
    def __init__(self,robot) -> None:
        self.gps =robot.getDevice('gps')
        self.gps.enable(int(robot.getBasicTimeStep()))
    @property
    def position(self):
        return self.gps.getValues()
    