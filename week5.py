class Superhero:
    def __init__(self, name, power, strength):
        self.name = name
        self.power = power
        self.__strength = strength  # encapsulated (private) attribute

    def show_identity(self):
        print(f"I am {self.name}, my power is {self.power}!")

    def get_strength(self):
        return self.__strength

    def train(self):
        self.__strength += 10
        print(f"{self.name}'s strength increased to {self.__strength}!")

class FlyingSuperhero(Superhero):  # Inheritance
    def __init__(self, name, power, strength, flight_speed):
        super().__init__(name, power, strength)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} mph!")

hero1 = Superhero("ShadowMan", "Invisibility", 70)
hero1.show_identity()
hero1.train()
print("Strength:", hero1.get_strength())

hero2 = FlyingSuperhero("SkyQueen", "Wind Control", 90, 300)
hero2.show_identity()
hero2.fly()

# Activity 2: Polymorphism Challenge

class Vehicle:
    def move(self):
        pass  # General method, to be overridden

class Car(Vehicle):
    def move(self):
        print("The car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("The plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing on water.")

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
class Superhero:
    def __init__(self, name, power, strength):
        self.name = name
        self.power = power
        self.__strength = strength  # encapsulated (private) attribute

    def show_identity(self):
        print(f"I am {self.name}, my power is {self.power}!")

    def get_strength(self):
        return self.__strength

    def train(self):
        self.__strength += 10
        print(f"{self.name}'s strength increased to {self.__strength}!")

    def __str__(self):
        return f"Name: {self.name}, Power: {self.power}, Strength: {self.__strength}"

class FlyingSuperhero(Superhero):  # Inheritance
    def __init__(self, name, power, strength, flight_speed):
        super().__init__(name, power, strength)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} mph!")

    def __str__(self):
        return super().__str__() + f", Flight Speed: {self.flight_speed}"

hero1 = Superhero("ShadowMan", "Invisibility", 70)
print(hero1)
hero1.show_identity()
hero1.train()
print(hero1)

hero2 = FlyingSuperhero("SkyQueen", "Wind Control", 90, 300)
print(hero2)
hero2.show_identity()
hero2.fly()
print(hero2)

class Vehicle:
    def move(self):
        pass  # General method, to be overridden

    def __str__(self):
        return f"{type(self).__name__}"

class Car(Vehicle):
    def move(self):
        print("The car is driving on the road.")

    def __str__(self):
        return super().__str__() + " - Car"

class Plane(Vehicle):
    def move(self):
        print("The plane is flying in the sky.")

    def __str__(self):
        return super().__str__() + " - Plane"

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing on water.")

    def __str__(self):
        return super().__str__() + " - Boat"

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v)
    v.move()