from controller import RangeFinder
class CameraController:
    def __init__(self,robot):
        self.__timestep = int(robot.getBasicTimeStep())
        self.__camera =robot.getDevice("Kinect color")
        self.__range =robot.getDevice("Kinect range")
        self.__range.enable(self.__timestep)
        self.__camera.enable(self.__timestep)

    def detect_void(self):
        matrix = RangeFinder.getRangeImage(self.__range)
        if matrix[48000]== float('inf'):
            return True
        else:
            return False
