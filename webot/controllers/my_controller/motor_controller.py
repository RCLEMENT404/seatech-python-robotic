from controller import Motor
class Motor_controller():

    __motor_speed = [0.0, 0.0, 0.0, 0.0]

    def __init__(self, robot) -> None:
        self.back_left_motor= robot.getDevice('back_left_wheel_joint')
        self.back_right_motor= robot.getDevice('back_right_wheel_joint')
        self.front_left_motor= robot.getDevice('front_left_wheel_joint')
        self.front_right_motor= robot.getDevice('front_right_wheel_joint')
        self.front_left_motor.setVelocity(0.0)
        self.front_right_motor.setVelocity(0.0)
        self.back_left_motor.setVelocity(0.0)
        self.back_right_motor.setVelocity(0.0)
        self.front_left_motor.setPosition(float('inf'))
        self.front_right_motor.setPosition(float('inf'))
        self.back_left_motor.setPosition(float('inf'))
        self.back_right_motor.setPosition(float('inf'))
        self.ps1 = robot.getDevice('back_left_wheel_joint_sensor')
        self.ps2 = robot.getDevice('back_right_wheel_joint_sensor')
        self.ps3= robot.getDevice('front_left_wheel_joint_sensor')
        self.ps4 = robot.getDevice('front_right_wheel_joint_sensor')

    def __inverse_kinematics_velocity(self, target_speed):
        WHEEL_RADIUS= 0.1
        LX=0.238
        LY=0.285
        self.__motor_speed[0] = 1 / WHEEL_RADIUS * (target_speed[0] - target_speed[1] - (LX + LY) * target_speed[2])
        self.__motor_speed[1] = 1 / WHEEL_RADIUS * (target_speed[0] + target_speed[1] + (LX + LY) * target_speed[2])
        self.__motor_speed[2] = 1 / WHEEL_RADIUS * (target_speed[0] + target_speed[1] - (LX + LY) * target_speed[2])
        self.__motor_speed[3] = 1 / WHEEL_RADIUS * (target_speed[0] - target_speed[1] + (LX + LY) * target_speed[2])
        self.front_left_motor.setVelocity(self.__motor_speed[0])
        self.front_right_motor.setVelocity(self.__motor_speed[1])
        self.back_left_motor.setVelocity(self.__motor_speed[2])
        self.back_right_motor.setVelocity(self.__motor_speed[3])

    def forward(self):
        """Go forward"""
        self.__inverse_kinematics_velocity([5.0,0.0,0.0])
    def backward(self):
        """Go backward"""
        self.__inverse_kinematics_velocity([-5.0,0.0,0.0])
    def turn_left(self):
        """Turn left"""
        self.__inverse_kinematics_velocity([0.0,0.0,5.0])
    def turn_right(self):
        """Turn right"""
        self.__inverse_kinematics_velocity([0.0,0.0,-5.0])
    def sideway_left(self):
        """Sideway left"""
        self.__inverse_kinematics_velocity([0.0,-5.0,0.0])
    def sideway_right(self):
        """Sideway right"""
        self.__inverse_kinematics_velocity([0.0,5.0,0.0])
    def diagonal_right(self):
        """diagonal right"""
        self.__inverse_kinematics_velocity([5.0,5.0,0.0])
    def diagonal_left(self):
        """diagonal left"""
        self.__inverse_kinematics_velocity([-5.0,-5.0,0.0])
    def stop(self):
        """Stop"""
        self.__inverse_kinematics_velocity([0.0,0.0,0.0])
        