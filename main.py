
from policyholder import Policyholder
from product import Product
from payment import Payment

# Create products
health = Product(101, "Health Insurance", 500)
car = Product(102, "Car Insurance", 300)

# Create policyholders
policyholder1 = Policyholder(1, "John Doe")
policyholder2 = Policyholder(2, "Jane Smith")

# Register policyholders
policyholder1.register()
policyholder2.register()

# Process payments
payment1 = Payment(policyholder1, health)
payment1.process_payment()

payment2 = Payment(policyholder2, car)
payment2.process_payment()

# Display account details
policyholder1.display_details()
policyholder2.display_details()
