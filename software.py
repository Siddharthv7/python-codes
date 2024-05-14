class Book:
    def __init__(self, title, author, price):
        self.title = titless
        self.author = author
        self.price = price

class Inventory:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_author(self, author):
        return [book for book in self.books if book.author == author]

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, book, quantity):
        self.items.append({"book": book, "quantity": quantity})

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["book"].price * item["quantity"]
        return total

class Order:
    def __init__(self, cart):
        self.cart = cart
        self.order_status = "Pending"

    def process_order(self):
        self.order_status = "Processed"
        # Other order processing logic

# Sample data
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 12.50)

inventory = Inventory()
inventory.add_book(book1)
inventory.add_book(book2)

cart = ShoppingCart()
cart.add_item(book1, 2)
cart.add_item(book2, 1)

order = Order(cart)

def main():
    print("Welcome to the Online Bookstore!")

    while True:
        print("\n1. Browse Books")
        print("2. View Cart")
        print("3. Checkout")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            author = input("Enter author name: ")
            author_books = inventory.search_by_author(author)
            for book in author_books:
                print(f"{book.title} by {book.author} - ${book.price:.2f}")

        elif choice == "2":
            print("Shopping Cart:")
            for item in cart.items:
                print(f"{item['book'].title} - Quantity: {item['quantity']}")

        elif choice == "3":
            print(f"Total: ${cart.calculate_total():.2f}")
            confirm = input("Confirm order (yes/no): ")
            if confirm.lower() == "yes":
                order.process_order()
                print("Order processed!")

        elif choice == "4":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
