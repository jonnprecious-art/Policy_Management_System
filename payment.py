
class Payment:
  def __init__(self, policyholder, product):
    self.policyholder = policyholder
    self.product = product

  def process_payment(self):
    self.policyholder.balance += self.product.price
    self.policyholder.add_product(self.product)
    print(f"{self.policyholder.name} paid {self.product.price} for {self.product.name}")

  def send_reminder(self):
    print(f"Reminder sent to {self.policyholder.name}")

  def apply_penalty(self, amount):
    self.policyholder.balance += amount
    print(f"Penalty of {amount} applied to {self.policyholder.name}")
