
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