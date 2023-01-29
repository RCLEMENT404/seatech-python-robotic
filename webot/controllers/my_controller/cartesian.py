from typing import List
import math

COORDINATE_MATCHING_ACCURACY = 0.01
THETA_MATCHING_ACCURACY = 1


def convert_vec3f_to_cartesian_vec2f(coordinate3f):
    coordinate2f = [0, 0]
    coordinate2f[0] = coordinate3f[0]
    coordinate2f[1] = -coordinate3f[2]
    return coordinate2f


def convert_cartesian_vec2f_to_vec3f(coordinate2f: List[float]) -> List[float]:
    coordinate3f = [coordinate2f[0], 0, -coordinate2f[1]]
    return coordinate3f


def convert_compass_bearing_to_heading(heading):
    heading = 360 - heading
    heading = heading + 90
    if heading > 360.0:
        heading = heading - 360.0
    return heading


def is_coordinate_equal(coordinate1, coordinate2):
    if abs(coordinate1[0] - coordinate2[0]) < COORDINATE_MATCHING_ACCURACY and abs(
            coordinate1[1] - coordinate2[1]) < COORDINATE_MATCHING_ACCURACY:
        return True
    else:
        return False


def is_coordinate_vector_equal(coordinate_vector1, coordinate_vector2):
    if abs(coordinate_vector1 - coordinate_vector2) < COORDINATE_MATCHING_ACCURACY:
        return True
    else:
        return False


def is_theta_equal(theta, theta2):
    if abs(theta - theta2) < THETA_MATCHING_ACCURACY:
        return True
    else:
        return False


def calc_destination_theta_in_degrees(current_coordinate, destination_coordinate):
    return math.atan2(destination_coordinate[1] - current_coordinate[1],
                      destination_coordinate[0] - current_coordinate[0]) * 180 / math.pi


def calc_theta_dot(heading, destination_theta):
    theta_dot = destination_theta - heading

    if theta_dot > 180:
        theta_dot = -(360 - theta_dot)
    elif theta_dot < -180:
        theta_dot = (360 + theta_dot)

    return theta_dot


def calc_rotated_theta_by_theta_dot(theta, theta_dot):
    if theta_dot == 0:
        return theta

    theta += theta_dot

    if theta < 0:
        theta = theta + 360
    elif theta >= 360:
        theta = theta - 360

    return theta


def calc_distance(current_coordinate, destination_coordinate):
    return math.sqrt(
        pow(destination_coordinate[0] - current_coordinate[0], 2) + pow(
            destination_coordinate[1] - current_coordinate[1],
            2))
