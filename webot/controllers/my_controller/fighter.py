from controller import Robot
from motorcontroller import MotorController
from lidarcontroller import LidarController
from positioncontroller import PositionController
from cartesian import is_theta_equal, is_coordinate_equal
from cameracontroller import CameraController


class Fighter(Robot):
    """Fighter"""
    ROBOT_ANGULAR_SPEED_IN_DEGREES = 200.915590
    TANGENSIAL_SPEED = 2.0

    def __init__(self):
        super().__init__()
        self.__motor = MotorController(self)
        self.__lidar = LidarController(self)
        self.__position = PositionController(self)
        self.__camera = CameraController(self)

    def __rotate_heading(self, theta_dot):
        if not is_theta_equal(theta_dot, 0):
            duration = abs(theta_dot) / self.ROBOT_ANGULAR_SPEED_IN_DEGREES
            print("duration to face the destination: " + str(duration) + "\n")

            if theta_dot > 0:
                self.__motor.turn_left()
            elif theta_dot < 0:
                self.__motor.turn_right()
            start_time = self.getTime()
            while True:
                self.step()
                if self.getTime() > start_time + duration:
                    break

    def __move_forward(self, distance):
        duration = distance / self.TANGENSIAL_SPEED
        print("duration to reach target location: " + str(duration) + "\n")

        self.__motor.forward()
        start_time = self.getTime()
        while True:
            #if self.__camera.detect_void():

            self.step()
            if self.getTime() > start_time + duration:
                break
            
        self.__motor.stop()
        self.step()

    def move_to_destination(self, destination_coordinate):
        current_coordinate = self.__position.get_robot_coordinate()
        print("Initial Coordinate: " + str(current_coordinate[0]) + " " + str(current_coordinate[1]) + "\n")
        print("Destination Coordinate: " + str(destination_coordinate[0]) + " " + str(destination_coordinate[1]))

        if is_coordinate_equal(self.__position.get_robot_coordinate(), destination_coordinate):
            print("Robot is already at the destination location\n")
            return

        theta_dot_to_destination = self.__position.calc_theta_dot_to_destination(destination_coordinate)
        print("thetaDotToDestination: " + str(theta_dot_to_destination) + "\n", )

        self.__rotate_heading(theta_dot_to_destination)

        distance_to_destination = self.__position.calc_theta_dot_to_destination(destination_coordinate)
        print("distanceToDestination: " + str(distance_to_destination) + "\n")

        self.__move_forward(distance_to_destination)

        current_coordinate = self.__position.get_robot_coordinate()
        print("Stop Coordinate: " + str(current_coordinate[0]) + " " + str(current_coordinate[1]) + "\n")

    def run(self):
        """Run the robot"""
        if self.__camera.detect_void() or  self.__lidar.obstacle_avoidance():
            self.__motor.turn_right()
        else:
            self.__motor.forward()
        #self.move_to_destination([0.0, 0.0])
