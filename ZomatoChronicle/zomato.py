class Dish:
    def __init__(self, dish_id, name, price, availability):
        self.dish_id = dish_id
        self.name = name
        self.price = price
        self.availability = availability

class Order:
    def __init__(self, order_id, customer_name, dishes):
        self.order_id = order_id
        self.customer_name = customer_name
        self.dishes = dishes
        self.status = "received"

class ZestyZomato:
    def __init__(self):
        self.menu = []
        self.orders = []
        self.current_order_id = 1

    def add_dish(self, dish_id, name, price, availability):
        dish = Dish(dish_id, name, price, availability)
        self.menu.append(dish)
        print("Dish added successfully!")

    def remove_dish(self, dish_id):
        for dish in self.menu:
            if dish.dish_id == dish_id:
                self.menu.remove(dish)
                print("Dish removed successfully!")
                return
        print("Dish not found!")

    def update_dish_availability(self, dish_id, availability):
        for dish in self.menu:
            if dish.dish_id == dish_id:
                dish.availability = availability
                print("Dish availability updated successfully!")
                return
        print("Dish not found!")

    def take_order(self, customer_name, dish_ids):
        dishes = []
        for dish_id in dish_ids:
            dish = self.find_dish_by_id(dish_id)
            if dish is None:
                print(f"Dish with ID {dish_id} not found!")
                return
            
            if not dish.availability:
                print(f"Dish '{dish.name}' is not available!")
                return
            dishes.append(dish)
            
        order = Order(self.current_order_id, customer_name, dishes)
        self.orders.append(order)
        self.current_order_id += 1
        print("Order placed successfully!")

    def update_order_status(self, order_id, status):
        for order in self.orders:
            if order.order_id == order_id:
                order.status = status
                print("Order status updated successfully!")
                return
        print("Order not found!")

    def find_dish_by_id(self, dish_id):
        for dish in self.menu:
            if dish.dish_id == dish_id:
                return dish
        return None

    def print_menu(self):
        print("Menu:")
        for dish in self.menu:
            print(f"ID: {dish.dish_id}, Name: {dish.name}, Price: {dish.price}, Availability: {'Yes' if dish.availability else 'No'}")

    def print_orders(self):
        print("Orders:")
        for order in self.orders:
            print(f"Order ID: {order.order_id}, Customer: {order.customer_name}, Status: {order.status}")

    def run(self):
        print("Welcome to Zesty Zomato!")
        while True:
            print("\n--- Main Menu ---")
            print("1. Add Dish")
            print("2. Remove Dish")
            print("3. Update Dish Availability")
            print("4. Take Order")
            print("5. Update Order Status")
            print("6. Review Orders")
            print("7. Exit")
            choice = input("Enter your choice (1-7): ")

            if choice == "1":
                dish_id = input("Enter dish ID: ")
                name = input("Enter dish name: ")
                price = float(input("Enter dish price: "))
                availability = input("Enter dish availability (yes/no): ")
                self.add_dish(dish_id, name, price, availability.lower() == "yes")

            elif choice == "2":
                dish_id = input("Enter dish ID to remove: ")
                self.remove_dish(dish_id)

            elif choice == "3":
                dish_id = input("Enter dish ID to update availability: ")
                availability = input("Enter new availability (yes/no): ")
                self.update_dish_availability(dish_id, availability.lower() == "yes")
                
            elif choice == "4":
                customer_name = input("Enter customer name: ")
                dish_ids = input("Enter dish IDs (comma-separated): ").split(",")
                self.take_order(customer_name, dish_ids)

            elif choice == "5":
                order_id = input("Enter order ID: ")
                status = input("Enter new status: ")
                self.update_order_status(order_id, status)

            elif choice == "6":
                self.print_orders()

            elif choice == "7":
                print("Thank you for using Zesty Zomato. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


zesty_zomato = ZestyZomato()
zesty_zomato.run()
