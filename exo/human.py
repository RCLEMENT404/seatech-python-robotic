"""
    Human class
"""
class Human():
    """
    A Human
    """
    # Human class content here
    __stomach = []
    def __init__(self,sexe) -> None:
        self.__sexe = sexe

    def __str__(self) -> str:
        return "Sex : "+ self.__sexe + "\nStomach : "+ str(self.__stomach)

    def eat(self,food):
        """
        Human eats food, can be string or string list
        """
        if isinstance(food,str):
            self.__stomach.append(food)
        elif isinstance(food,list):
            self.__stomach += food
        print("Current stomach content: " + str(self.__stomach))

    def digest(self):
        """
        Clear the stomach content
        """
        self.__stomach.clear()
        print("All food has been digested !")
