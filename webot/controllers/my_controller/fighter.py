from controller import Robot,PositionSensor,Compass
from motor_controller import Motor_controller
from lidar_controller import Lidar_Controller
from gps_controller import Gps_controller

class Fighter(Robot):
    """Fighter"""

    def __init__(self):
        super().__init__()
        self.__motor = Motor_controller(self)
        self.__lidar=Lidar_Controller(self)
        self.__gps = Gps_controller(self)

    def run(self):
        """Run the robot"""
        self.__motor.stop()
        print(self.__gps.position)
