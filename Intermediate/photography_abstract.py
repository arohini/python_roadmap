from abc import ABC, abstractmethod

class Photography(ABC):
    """This class represents abstract methods for all the child methods which inherit"""

    @abstractmethod
    def set_shutter_speed(self, speed):
        """_summary_

        Args:
            speed (_type_): _description_
        """
        pass

    @abstractmethod
    def set_iso(self, iso):
        """_summary_

        Args:
            iso (bool): _description_
        """
        pass

class MobilePhotography(Photography):
    """_summary_

    Args:
        Photography (_type_): _description_
    """

    def set_shutter_speed(self, speed):
        print(f"Setting shutter speed to {speed} for mobile photography")
    
    def set_iso(self, iso):
        print(f"Setting ISO to {iso} for mobile photography")


class DslrPhotography(Photography):
    """_summary_

    Args:
        Photography (_type_): _description_
    """

    def set_shutter_speed(self, speed):
        print(f"Setting shutter speed to {speed} for DSLR photography")
    
    def set_iso(self, iso):
        print(f"Setting ISO to {iso} for DSLR photography")


# Example usage

mobile = MobilePhotography()
mobile.set_shutter_speed(1/50)
mobile.set_iso(100)

dslr = DslrPhotography()
dslr.set_shutter_speed(1/125)
dslr.set_iso(200)
