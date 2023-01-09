from abc import ABCMeta, abstractmethod

""" You can use classes below or create your own 👍️"""

class UnmannedVehicle(metaclass=ABCMeta):
    """ 
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """
    @abstractmethod
    def selectMission(self,mission):
        pass


class AerialVehicle(UnmannedVehicle,metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def takeOff(self):
        pass
    @abstractmethod
    def land(self):
        pass

class GroundVehicle(UnmannedVehicle,metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class UnderseaVehicle(UnmannedVehicle,metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def dive(self):
        pass
    @abstractmethod
    def returnToSurface(self):
        pass

class UAV(AerialVehicle):
    """Unmanned Aerial Vehicle"""
    def selectMission(self,mission):
        print("UAV mission " + mission+ " selected !")
    def land(self):
        print("Landing...")
    def takeOff(self):
        print("Taking off ...")   
    pass

class UUV(UnderseaVehicle):
    """Unmanned Undersea Vehicle"""
    def selectMission(self,mission):
        print("UUV mission " + mission+ " selected !")
    def dive(self):
        print("Diving ...")
    def returnToSurface(self):
        print("Returning to surface ...")
    pass

class UGV(GroundVehicle):
    """Unmanned Ground Vehicle"""
    def selectMission(self,mission):
        print("UGV mission " + mission+ " selected !")
    def accelerate(self):
        print("Accelerating ....")
    def stop(self):
        print("Stop !!")
    pass


uav = UAV()
uav.selectMission("Observation")
uav.takeOff()

ugv = UGV()
ugv.selectMission("Analyse")
ugv.accelerate()

uuv = UUV()
uuv.selectMission("Exploration")
uuv.dive()