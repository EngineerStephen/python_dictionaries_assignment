
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
# print(beverage_menu)  
# 

# Demonstrate your ability to use nested collections and loops 
#  by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket  to "closed".
# Display all tickets.
#   (Bonus) filter by status
# Initialize with some sample tickets and include functionality for additional ticket entry.


service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Tracking customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
alice_ticket = service_tickets["Ticket001"]
bob_ticket = service_tickets["Ticket002"]   
print()
# print(alice_ticket)
# print(bob_ticket)
print("Here are the organized tickets Tracking customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed):    ")
print()
for detail in alice_ticket:
    print(detail,":", alice_ticket[detail])
print()
print()
for detail in bob_ticket:
    print(detail,":", bob_ticket[detail])
    
# Implementing a functions open a new service ticket.
new_ticket = []
def add_new_ticket():
    new_ticket.append(service_tickets)
    print()
    

    while True:
    
        user_name = input("Welcome to the support ticket system, please enter your name:   " )
        user_issue = input("Please enter the issue you are experiencing:   ")
        ticket_status = input("Do you want your ticket to be open or closed:   ")
        if ticket_status == "open" or ticket_status == "closed":
            print ()
        break
    print("Hi,",user_name, "Thank you for contacting us, we will be happy to help you with your issue:",user_issue, "Your ticket status is:",ticket_status,".")
    service_tickets.update({"Ticket 003" : {"Customer" : user_name, "Issue" : user_issue, "Status" : ticket_status}})
    fresh_ticket = service_tickets["Ticket 003"]
    print()
    print("Here are the NEWLY organized tickets Tracking customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed):    ")
    print()
    for detail in alice_ticket:
        print(detail,":", alice_ticket[detail])
    print()
    for detail in bob_ticket:
        print(detail,":", bob_ticket[detail])
    print() 
    for detail in fresh_ticket:
        print(detail,":", fresh_ticket[detail])   
        
    print()
    print("Thank you for using our service, Have a great day!")


add_new_ticket()