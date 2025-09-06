class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species

  def speak(self):
    print("Some generic sound.")

  def info(self):
    print(f"{self.name} is a {self.species}")


class Dog(Animal):
  def __init__(self, name, breed):
    super().__init__(name, "Dog")
    self.breed = breed

  def speak(self):
    print(f"Woof!")

  def info(self):
    print(f"{self.name} is a {self.species}")

dog = Dog("Buddy", "Unknown")
dog.speak()
dog.info()