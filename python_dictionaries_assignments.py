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