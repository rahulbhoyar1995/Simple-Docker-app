"""Car class"""


class Car:
    """Car class"""
    def __init__(self, make, model, year):
        """display model company name"""
        self._make = make          # protected attribute
        self._model = model        # protected attribute
        self.__year = year         # private attribute

    def display_make_model(self):
        """display model company name"""
        return f"Make: {self._make}, Model: {self._model}"

    def _display_year(self):
        """display model company name"""
        return f"Year: {self.__year}"    # protected method

    def get_year(self):
        """display model company name"""
        return self.__year               # public method

class SportsCar(Car):
    """display model company name"""
    def __init__(self, make, model, year, top_speed):
        super().__init__(make, model, year)
        self._top_speed = top_speed          # protected attribute

    def display_car_details(self):
        """display model company name"""
        make_model = self.display_make_model()
        top_speed = f"Top Speed: {self._top_speed} mph"
        year = self._display_year()
        return f"{make_model}, {top_speed}, {year}"

car1 = Car("Honda", "Civic", 2022)
print(car1.display_make_model())         # public method call
# Output: Make: Honda, Model: Civic

print(car1.get_year())                   # public method call
# Output: 2022

# accessing protected method and attribute using object of Car class
print(car1._display_year())              # protected method call
# Output: Year: 2022

print(car1._make)                        # protected attribute access
# Output: Honda

sports_car1 = SportsCar("Ferrari", "488 GTB", 2022, 205)
print(sports_car1.display_car_details()) # public method call of subclass
# Output: Make: Ferrari, Model: 488 GTB, Top Speed: 205 mph, Year: 2022

print(sports_car1._top_speed)            # protected attribute access of subclass
# Output: 205

print(sports_car1._make)                 # protected attribute access of parent class
# Output: Ferrari

print(sports_car1.get_year())            # public method call of parent class
# Output: 2022

print(sports_car1._display_year())       # error as it's private method
# Output: AttributeError: 'SportsCar' object has no attribute '_display_year'

print(sports_car1.__year)                # error as it's private attribute
