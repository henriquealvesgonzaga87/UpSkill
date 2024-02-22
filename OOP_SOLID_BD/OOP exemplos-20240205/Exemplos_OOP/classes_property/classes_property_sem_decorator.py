# https://www.programiz.com/python-programming/decorator
# Basically, a decorator takes in a function, adds some functionality and returns it.

# https://www.programiz.com/python-programming/property
# Using @property decorator
# using property class
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    # o = property(fget=None, fset=None, fdel=None, doc=None)
        # fget is function to get value of the attribute
        # fset is function to set value of the attribute
        # fdel is function to delete the attribute
        # doc is a string (like a comment)
    # temperature = property(get_temperature)
    temperature = property(get_temperature, set_temperature)



human = Celsius(37)
print(human.temperature)
human.temperature = -200
print(human.to_fahrenheit())
human.temperature = -300

human = Celsius(-400)
