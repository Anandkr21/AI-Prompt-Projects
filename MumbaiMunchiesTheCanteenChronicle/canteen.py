class Snack:
    def __init__(self, snack_id, name, price, availability):
        self.snack_id = snack_id
        self.name = name
        self.price = price
        self.availability = availability

class Canteen:
    def __init__(self):
        self.inventory = []
        self.sales = []

    def add_snack(self, snack_id, name, price, availability):
        snack = Snack(snack_id, name, price, availability)
        self.inventory.append(snack)
        print("Snack added successfully!")

    def remove_snack(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                self.inventory.remove(snack)
                print("Snack removed successfully!")
                return
        print("Snack not found!")

    def update_snack_availability(self, snack_id, availability):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                snack.availability = availability
                print("Snack availability updated successfully!")
                return
        print("Snack not found!")

    def sell_snack(self, snack_id):
        snack = self.find_snack_by_id(snack_id)
        if snack is None:
            print(f"Snack with ID {snack_id} not found!")
            return
        if not snack.availability:
            print(f"Snack '{snack.name}' is not available!")
            return
        self.sales.append(snack)
        self.inventory.remove(snack)
        print("Snack sold successfully!")

    def find_snack_by_id(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                return snack
        return None

    def print_inventory(self):
        print("Inventory:")
        for snack in self.inventory:
            print(f"ID: {snack.snack_id}, Name: {snack.name}, Price: {snack.price}, Availability: {'Yes' if snack.availability else 'No'}")

    def print_sales(self):
        print("Sales:")
        for snack in self.sales:
            print(f"ID: {snack.snack_id}, Name: {snack.name}, Price: {snack.price}")

    def run(self):
        print("Welcome to the Canteen Inventory Management!")
        while True:
            print("\n--- Main Menu ---")
            print("1. Add Snack")
            print("2. Remove Snack")
            print("3. Update Snack Availability")
            print("4. Sell Snack")
            print("5. Inventory")
            print("6. Sales")
            print("7. Exit")
            choice = input("Enter your choice (1-7): ")

            if choice == "1":
                snack_id = input("Enter snack ID: ")
                name = input("Enter snack name: ")
                price = float(input("Enter snack price: "))
                availability = input("Enter snack availability (yes/no): ")
                self.add_snack(snack_id, name, price, availability.lower() == "yes")

            elif choice == "2":
                snack_id = input("Enter snack ID to remove: ")
                self.remove_snack(snack_id)

            elif choice == "3":
                snack_id = input("Enter snack ID to update availability: ")
                availability = input("Enter new availability (yes/no): ")
                self.update_snack_availability(snack_id, availability.lower() == "yes")

            elif choice == "4":
                snack_id = input("Enter snack ID to sell: ")
                self.sell_snack(snack_id)

            elif choice == "5":
                self.print_inventory()

            elif choice == "6":
                self.print_sales()

            elif choice == "7":
                print("Thank you for using Canteen Inventory Management. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                

canteen = Canteen()
canteen.run()
