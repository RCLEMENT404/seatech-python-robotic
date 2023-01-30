from controller import Motor


class MotorController:
    __motor_speed = [0.0, 0.0, 0.0, 0.0]
    __max_speed = 2.0

    def __init__(self, robot) -> None:
        self.back_left_motor = robot.getDevice('back_left_wheel_joint')
        self.back_right_motor = robot.getDevice('back_right_wheel_joint')
        self.front_left_motor = robot.getDevice('front_left_wheel_joint')
        self.front_right_motor = robot.getDevice('front_right_wheel_joint')
        self.front_left_motor.setVelocity(0.0)
        self.front_right_motor.setVelocity(0.0)
        self.back_left_motor.setVelocity(0.0)
        self.back_right_motor.setVelocity(0.0)
        self.front_left_motor.setPosition(float('inf'))
        self.front_right_motor.setPosition(float('inf'))
        self.back_left_motor.setPosition(float('inf'))
        self.back_right_motor.setPosition(float('inf'))

    def __inverse_kinematics_velocity(self, target_speed):
        wheel_radius = 0.1
        lx = 0.238
        ly = 0.285
        self.__motor_speed[0] = 1 / wheel_radius * (target_speed[0] - target_speed[1] - (lx + ly) * target_speed[2])
        self.__motor_speed[1] = 1 / wheel_radius * (target_speed[0] + target_speed[1] + (lx + ly) * target_speed[2])
        self.__motor_speed[2] = 1 / wheel_radius * (target_speed[0] + target_speed[1] - (lx + ly) * target_speed[2])
        self.__motor_speed[3] = 1 / wheel_radius * (target_speed[0] - target_speed[1] + (lx + ly) * target_speed[2])
        self.front_left_motor.setVelocity(self.__motor_speed[0])
        self.front_right_motor.setVelocity(self.__motor_speed[1])
        self.back_left_motor.setVelocity(self.__motor_speed[2])
        self.back_right_motor.setVelocity(self.__motor_speed[3])

    def forward(self):
        """Go forward"""
        self.__inverse_kinematics_velocity([self.__max_speed, 0.0, 0.0])

    def backward(self):
        """Go backward"""
        self.__inverse_kinematics_velocity([-self.__max_speed, 0.0, 0.0])

    def turn_left(self):
        """Turn left"""
        self.__inverse_kinematics_velocity([0.0, 0.0, self.__max_speed])

    def turn_right(self):
        """Turn right"""
        self.__inverse_kinematics_velocity([0.0, 0.0, -self.__max_speed])

    def sideway_left(self):
        """Sideway left"""
        self.__inverse_kinematics_velocity([0.0, -self.__max_speed, 0.0])

    def sideway_right(self):
        """Sideway right"""
        self.__inverse_kinematics_velocity([0.0, self.__max_speed, 0.0])

    def diagonal_right(self):
        """diagonal right"""
        self.__inverse_kinematics_velocity([self.__max_speed, self.__max_speed, 0.0])

    def diagonal_left(self):
        """diagonal left"""
        self.__inverse_kinematics_velocity([-self.__max_speed, -self.__max_speed, 0.0])

    def stop(self):
        """Stop"""
        self.__inverse_kinematics_velocity([0.0, 0.0, 0.0])
