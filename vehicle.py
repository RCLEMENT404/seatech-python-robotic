"""
Vehicles classes
"""
from abc import ABCMeta, abstractmethod


class UnmannedVehicle(metaclass=ABCMeta):
    """
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """
    @abstractmethod
    def select_mission(self,mission):
        """
        Select the mission
        """


class AerialVehicle(UnmannedVehicle,metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def take_off(self):
        """
        Take off from the ground
        """
    @abstractmethod
    def land(self):
        """
        Land on the ground
        """

class GroundVehicle(UnmannedVehicle,metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def accelerate(self):
        """
        Push the accelerator pedal
        """
    @abstractmethod
    def stop(self):
        """
        Push the break pedal
        """

class UnderseaVehicle(UnmannedVehicle,metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def dive(self):
        """
        Dive underwater
        """
    @abstractmethod
    def return_to_surface(self):
        """
        Go back to the surface
        """

class UAV(AerialVehicle):
    """Unmanned Aerial Vehicle"""
    def select_mission(self,mission):
        print("UAV mission " + mission+ " selected !")
    def land(self):
        print("Landing...")
    def take_off(self):
        print("Taking off ...")

class UUV(UnderseaVehicle):
    """Unmanned Undersea Vehicle"""
    def select_mission(self,mission):
        print("UUV mission " + mission+ " selected !")
    def dive(self):
        print("Diving ...")
    def return_to_surface(self):
        print("Returning to surface ...")

class UGV(GroundVehicle):
    """Unmanned Ground Vehicle"""
    def select_mission(self,mission):
        print("UGV mission " + mission+ " selected !")
    def accelerate(self):
        print("Accelerating ....")
    def stop(self):
        print("Stop !!")

if __name__ =='__main__':
    uav = UAV()
    uav.select_mission("Observation")
    uav.take_off()

    ugv = UGV()
    ugv.select_mission("Analyse")
    ugv.accelerate()

    uuv = UUV()
    uuv.select_mission("Exploration")
    uuv.dive()
