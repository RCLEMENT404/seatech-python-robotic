from controller import Lidar


class LidarController:
    def __init__(self, robot) -> None:
        self.__timestep = int(robot.getBasicTimeStep())
        self.front_lidar = robot.getDevice('Sick S300 Front')
        self.back_lidar = robot.getDevice('Sick S300 Back')
        self.front_lidar.enable(self.__timestep)
        self.back_lidar.enable(self.__timestep)
        self.front_lidar.enablePointCloud()
        self.back_lidar.enablePointCloud()
        self._ds = robot.getDevice("distance sensor")
        self._ds.enable(self.__timestep)
    
    def obstacle_avoidance(self):
        matrix =self.front_lidar.getRangeImage()
        return any(i < 0.20 for i in matrix)
            