from controller import Robot,Motor,PositionSensor,Compass,Gyro,Lidar

class Fighter(Robot):
    """Fighter"""
    

    __motor_speed = [0.0, 0.0, 0.0, 0.0]

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
    def __init__(self):
        super().__init__()
        self.back_left_motor= self.getDevice('back_left_wheel_joint')
        self.back_right_motor= self.getDevice('back_right_wheel_joint')
        self.front_left_motor= self.getDevice('front_left_wheel_joint')
        self.front_right_motor= self.getDevice('front_right_wheel_joint')
        self.front_left_motor.setVelocity(0.0)
        self.front_right_motor.setVelocity(0.0)
        self.back_left_motor.setVelocity(0.0)
        self.back_right_motor.setVelocity(0.0)
        self.front_left_motor.setPosition(float('inf'))
        self.front_right_motor.setPosition(float('inf'))
        self.back_left_motor.setPosition(float('inf'))
        self.back_right_motor.setPosition(float('inf'))
        self.ps1 = self.getDevice('back_left_wheel_joint_sensor')
        self.ps2 = self.getDevice('back_right_wheel_joint_sensor')
        self.ps3= self.getDevice('front_left_wheel_joint_sensor')
        self.ps4 = self.getDevice('front_right_wheel_joint_sensor')
        self. ld1 = self.getDevice('Sick S300 Front')
        self.ld2 = self.getDevice('Sick S300 Back')

    def forward(self):
        """Go forward"""
        self.__inverse_kinematics_velocity([5.0,0.0,0])
    def backward(self):
        """Go backward"""

        self.front_left_motor.setVelocity(-10.0)
        self.front_right_motor.setVelocity(-10.0)
        self.back_left_motor.setVelocity(-10.0)
        self.back_right_motor.setVelocity(-10.0)
    def turn_left(self):
        """Turn left"""
        self.front_left_motor.setVelocity(20.0)
        self.front_right_motor.setVelocity(-15.0)
        self.back_left_motor.setVelocity(20.0)
        self.back_right_motor.setVelocity(-15.0)
    def turn_right(self):
        """Turn right"""
        self.front_left_motor.setVelocity(-15.0)
        self.front_right_motor.setVelocity(20.0)
        self.back_left_motor.setVelocity(-15.0)
        self.back_right_motor.setVelocity(20.0)
    def sideway_left(self):
        """Turn right"""
        self.front_left_motor.setVelocity(-20.0)
        self.front_right_motor.setVelocity(20.0)
        self.back_left_motor.setVelocity(20.0)
        self.back_right_motor.setVelocity(-20.0)
    def sideway_right(self):
        """Turn right"""
        self.front_left_motor.setVelocity(20.0)
        self.front_right_motor.setVelocity(-20.0)
        self.back_left_motor.setVelocity(-20.0)
        self.back_right_motor.setVelocity(20.0)
    def diagonal_right(self):
        """diagonal right"""
        self.front_left_motor.setVelocity(20.0)
        self.front_right_motor.setVelocity(0.0)
        self.back_left_motor.setVelocity(0.0)
        self.back_right_motor.setVelocity(20.0)

    def diagonal_left(self):
        """diagonal left"""
        self.front_left_motor.setVelocity(0.0)
        self.front_right_motor.setVelocity(-50.0)
        self.back_left_motor.setVelocity(-50.0)
        self.back_right_motor.setVelocity(0.0)
    def stop(self):
        """Stop"""
        self.front_left_motor.setVelocity(0.0)
        self.front_right_motor.setVelocity(0.0)
        self.back_left_motor.setVelocity(0.0)
        self.back_right_motor.setVelocity(0.0)
    def run(self):
        self.forward()
