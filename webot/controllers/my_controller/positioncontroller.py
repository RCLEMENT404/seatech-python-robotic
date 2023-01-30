from controller import GPS, Compass
import math
import cartesian


class PositionController:

    def __init__(self, robot) -> None:
        self.__timestep = int(robot.getBasicTimeStep())
        self.__gps = robot.getDevice('gps')
        self.__compass = robot.getDevice('compass')
        self.__gps.enable(self.__timestep)
        self.__compass.enable(self.__timestep)

    @property
    def position(self):
        return GPS.getValues(self.__gps)

    def get_robot_bearing(self):
        # calculate bearing angle in degrees
        north = Compass.getValues(self.__compass)
        rad = math.atan2(north[0], north[1])
        bearing = (rad - math.pi / 2) / math.pi * 180
        if bearing < 0:
            bearing += 360
        return bearing

    def get_robot_coordinate(self):
        return cartesian.convert_vec3f_to_cartesian_vec2f(Compass.getValues(self.__gps))

    def get_robot_heading(self):
        return cartesian.convert_compass_bearing_to_heading(self.get_robot_bearing())

    def calc_distance_to_destination(self, destination_coordinate):
        current_coordinate = self.get_robot_coordinate()
        return cartesian.calc_distance(current_coordinate, destination_coordinate)

    def calc_theta_dot_to_destination(self, destination_coordinate):
        current_coordinate = self.get_robot_coordinate()
        robot_heading = self.get_robot_heading()
        destination_theta = cartesian.calc_destination_theta_in_degrees(current_coordinate, destination_coordinate)
        return cartesian.calc_theta_dot(robot_heading, destination_theta)
