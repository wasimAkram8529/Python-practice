class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed;
    self.is_sleeping = False

  def bark(self):
    return "Woof!"

  def sleep(self):
    self.is_sleeping = True
    print(f"{self.name} is sleeping.")

  def wake_up(self):
    self.is_sleeping = False
    print(f"{self.name} is now wakeup!")


my_dog = Dog("Buddy", "Golden retriver")
print(my_dog.bark())

my_dog.sleep()
my_dog.wake_up()