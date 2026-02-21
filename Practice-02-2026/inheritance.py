class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species

  def speak(self):
    return "Some Generic animal sound"

  def info(self):
    return f"{self.name} is a {self.species}"
  
class Dog(Animal):
  def __init__(self, name, species, breed):
    super().__init__(name, species)
    self.breed = breed

  def speak(self):
    return "Woof!"
  
  def info(self):
    # return f"{self.name} is a {self.breed} {self.species}"
    return "wasim"


dog = Dog("Buddy", "Dog","Golden Retriver")
print(dog.speak())
print(dog.info())