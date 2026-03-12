
class Policyholder:
  def __init__(self, policyholder_id, name, status="Active"):
    self.policyholder_id = policyholder_id
    self.name = name
    self.status = status
    self.products = []
    self.balance = 0

  def register(self):
    print(f"{self.name} registered successfully.")

  def suspend(self):
    self.status = "Suspended"
    print(f"{self.name}'s account has been suspended.")

  def reactivate(self):
    self.status = "Active"
    print(f"{self.name}'s account has been reactivated.")

  def add_product(self, product):
    self.products.append(product)

  def display_details(self):
    print("\nPolicyholder Details")
    print("______________________")
    print("ID:", self.policyholder_id)
    print("Name:", self.name)
    print("Status:", self.status)
    print("Products:",[p.name for p in self.products])
    print("Balance:", self.balance)
