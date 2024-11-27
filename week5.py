class Smartphone:
    def __init__(self, brand, model, color, storage):
        self.brand = brand
        self.model = model
        self.color = color
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

    def take_picture(self):
        print("Taking a picture...")

    def browse_internet(self, website):
        print(f"Browsing {website}...")


phone1 = Smartphone("Apple", "iPhone 15", "Midnight", 256)
phone2 = Smartphone("Samsung", "Galaxy S24", "Phantom Black", 512)

phone1.make_call("123-456-7890")
phone2.send_message("987-654-3210", "Hello, world!")
phone1.take_picture()
phone2.browse_internet("google.com")


class Animal:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("Running on four legs ")

class Bird(Animal):
    def move(self):
        print("Flying through the sky ")

class Fish(Animal):
    def move(self):
        print("Swimming underwater ")

# Example usage:
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()