restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

print()
print(restaurant_menu)
print()
# - Add a new category called "Beverages" with at least two items. 
# - Update the price of "Steak" to 17.99. 
# - Remove "Bruschetta" from "Starters". ---

beverage_menu = restaurant_menu.update({"Soft Drinks": {"100% Pinneaple juice : 2.99", "100% Orange juice : 2.99"}})
print(beverage_menu)

# the following code is not working, I am not sure why:
# beverage_menu = restaurant_menu.update({"Soft Drinks": {"100% Pinneaple juice : 2.99", "100% Orange juice : 2.99"}})
# print(beverage_menu)  this 


service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

#  Demonstrate your ability to use nested collections and loops 
#  by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket  to "closed".
# Display all tickets.
#   (Bonus) filter by status
# Initialize with some sample tickets and include functionality for additional ticket entry.


for ti