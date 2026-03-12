
class Product:
  def __init__(self, product_id, name, price, status="Available"):
    self.product_id = product_id
    self.name = name
    self.price = price
    self.status = status

  def update_product(self, name=None, price=None):
    if name:
      self.name = name
    if price:
      self.price = price
    print("Product updated successfully.")

  def suspend_product(self):
    self.status = "Suspended"
    print(f"{self.name} product suspended")

  def activate_product(self):
    self.status = "Available"
    print(f"{self.name} product activated")
