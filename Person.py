class Person:
    def __init__(self, name, age, height):
        print("Constructing the Person object")
        self.__name = name
        self.__age = age
        self.__height = height
        self.public_prop = "I'm public"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def __del__(self):
        print("The garbage collector is automatically destroying the Person object")

    # Magic getter and setter for name property
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name