# Policy_Management_System
Project Overview
This system is a Python-based management tool designed for an insurance company to streamline the administration of policyholders, insurance products, and payments. It follows Object-Oriented Programming (OOP) principles, ensuring modularity and scalability.

File Structure
The project is divided into separate modules for better organization:
product.py: Contains the Product class to manage insurance plans.
policyholder.py: Contains the Policyholder class for member registration and status management.
payment.py: Contains the Payment class for processing transactions, reminders, and penalties.
main.py: The entry point of the application that demonstrates the system's functionality.

Features
1. Policyholder Management
Register Members: Add new policyholders to the system.
Status Control: Suspend or reactivate policyholder accounts.
Product Assignment: Link policyholders to specific insurance products.

2. Product Management
Create Products: Define new insurance plans with unique IDs and premiums.
Update & Suspend: Modify premium amounts or temporarily disable products from being sold.

3. Payment Processing
Transaction Handling: Track and process monthly premiums.
Reminders: Automated static methods to alert users of due dates.
Penalties: Support for adding late fees to existing payment records.

How to Run the System
Ensure Python is installed: You will need Python 3.x to run this code.
Download/Clone the repository: Unzip the files into a single directory.
Run the Demonstration: Open your terminal or command prompt, navigate to the folder, and run: python main.py

Demonstration Details
The main.py script performs the following actions:
Creates two products: Car Insurance and Health Insurance
Registers two policyholders: Jane Smith and John Doe.
Processes a standard payment for Jane and John.
Displays the final account details and status for both users.

[Author: Precious Donald]
