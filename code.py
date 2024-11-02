import csv
import os
# import matplotlib as pyplot

# Function to load inventory data from CSV file
import csv
import os


def load_inventory():
    inventory = []
    if os.path.exists("inventory.csv"):
        with open("inventory.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                # Check if the row has the expected number of elements
                if len(row) == 3:
                    try:
                        item = {
                            "name": row[0],
                            "price": float(row[1]),
                            "quantity": int(row[2])
                        }
                        inventory.append(item)
                    except ValueError as e:
                        print(f"Error converting data: {e}")
                        # Handle the error (skip the row, log the issue, etc.)
                else:
                    print(
                        "Invalid row format: Each row should have 3 elements.")
                    # Handle the error (skip the row, log the issue, etc.)
    return inventory


# Function to save inventory data to CSV file
def save_inventory(inventory):
    with open("inventory.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for item in inventory:
            writer.writerow([item["name"], item["price"], item["quantity"]])


# Function to display the current inventory
def view_inventory(inventory):
    if not inventory:
        print("The inventory is empty.")
    else:
        print("Inventory:")
        for item in inventory:
            print(
                f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}"
            )

            # # Bar Graph
            # plt.figure(figsize=(8, 6))
            # plt.bar(item["name"], item["quantity"], color='blue')
            # plt.title("Inventory Quantity")
            # plt.xlabel("Item")
            # plt.ylabel("Quantity")
            # plt.show()

            # # Line Chart
            # quantity_history = [entry["quantity"] for entry in inventory]
            # plt.figure(figsize=(8, 6))
            # plt.plot(quantity_history,
            #          marker='o',
            #          linestyle='-',
            #          color='purple')
            # plt.title("Quantity Over Time")
            # plt.xlabel("Item Index")
            # plt.ylabel("Quantity")
            # plt.show()

            # # Histogram
            # plt.figure(figsize=(8, 6))
            # plt.hist(item["price"], bins=10, color='green', edgecolor='black')
            # plt.title("Price Distribution")
            # plt.xlabel("Price")
            # plt.ylabel("Frequency")
            # plt.show()


# Function for the boss interface
def boss_interface(inventory):
    while True:
        print("\nBoss Interface")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Delete Item")
        print("4. View Inventory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            update_item(inventory)
        elif choice == "3":
            delete_item(inventory)
        elif choice == "4":
            view_inventory(inventory)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose a valid option.")


# Function to add a new item to the inventory
def add_item(inventory):
    name = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    quantity = int(input("Enter the item quantity:"))

    item = {"name": name, "price": price, "quantity": quantity}
    inventory.append(item)
    save_inventory(inventory)
    print(f"{name} added to the inventory.")


# Function to update an existing item in the inventory
def update_item(inventory):
    name = input("Enter the name of the item to update: ")
    for item in inventory:
        if item["name"] == name:
            item["price"] = float(input("Enter the new price: "))
            item["quantity"] = int(input("Enter the new quantity: "))
            save_inventory(inventory)
            print(f"{name} updated in the inventory.")
            return
    print(f"{name} not found in the inventory.")


# Function to delete an item from the inventory
def delete_item(inventory):
    name = input("Enter the name of the item to delete: ")
    for item in inventory:
        if item["name"] == name:
            inventory.remove(item)
            save_inventory(inventory)
            print(f"{name} deleted from the inventory.")
            return
    print(f"{name} not found in the inventory.")


# Function for the employee interface
def employee_interface(inventory):
    while True:
        print("\nEmployee Interface")
        print("1. View Inventory")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_inventory(inventory)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please choose a valid option.")


# Main program
inventory = load_inventory()

while True:
    print("\nInventory Management System")
    print("1. Boss Interface")
    print("2. Employee Interface")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        boss_interface(inventory)
    elif choice == "2":
        employee_interface(inventory)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please choose a valid option.")

print("Thank you for using the Inventory Management System.")