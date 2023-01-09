class Human():   
    # Human class content here
    __stomach = []
    def __init__(self,sexe) -> None:
        self.__sexe = sexe

    def __str__(self) -> str:
        return "Sex : "+ self.__sexe + "\nStomach : "+ str(self.__stomach)

    def eat(self,food):
        if type(food) is str: 
            self.__stomach.append(food)
        elif type(food) is list:
            self.__stomach += food
        print("Current stomach content: " + str(self.__stomach))

    def digest(self):
        self.__stomach.clear()