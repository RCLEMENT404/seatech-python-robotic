from controller import Lidar
class Lidar_Controller():
    def __init__(self, robot) -> None:
        self. timestep = int(robot.getBasicTimeStep())
        self.front_lidar =robot.getDevice('Sick S300 Front')
        self.back_lidar =robot.getDevice('Sick S300 Back')
        self.front_lidar.enable(self.timestep)
        self.back_lidar.enable(self.timestep)
        self.front_lidar.enablePointCloud()
        self.back_lidar.enablePointCloud()
