class Account:
  def __init__(self, accNo, accHolderName, balance):
    self.accNo = accNo
    self.accHolderName = accHolderName
    self.balance = balance

  def display(self):
    print(f"--------Account details-------- \nAccount number: {self.accNo} \nAccount holder name: {self.accHolderName} \nbalance: {self.balance}")

  def deposit(self, amount):
    self.balance += amount
    print(f"{amount} added to your account.")

  def withdraw(self, amount):
    if self.balance < amount:
      print("Insufficient balance.")
    else:
      self.balance -= amount
      print(f"Withdraw of {amount} is successful.")
  

ac = Account(24680, "Wasim Akram", 1000)
ac.display()
ac.deposit(500)
ac.withdraw(1000)
ac.display()