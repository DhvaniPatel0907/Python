import pymysql

class InventoryDB:
    def __init__(self):
        # Connect to MySQL
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="inventory"
        )
        self.cursor = self.conn.cursor()

    # -------------------- MANAGER FUNCTIONS --------------------
    def add_product(self):
        print("\n--- Add Product ---")
        name = input("Enter product name: ").lower()
        try:
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
        except ValueError:
            print("Price and Quantity must be numbers!")
            return

        try:
            sql = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (name, price, quantity))
            self.conn.commit()
            print(f" {name} added successfully!")
        except:
            print(" Product already exists! Use update option.")

    def view_products(self):
        print("\n--- Current Inventory ---")
        self.cursor.execute("SELECT * FROM products")
        rows = self.cursor.fetchall()
        if not rows:
            print("⚠ No products available!")
        else:
            for row in rows:
                print(f"{row[1]} -> Price: {row[2]}, Quantity: {row[3]}")
        print("-------------------------\n")

    def update_product(self):
        print("\n--- Update Product ---")
        name = input("Enter product name to update: ").lower()
        self.cursor.execute("SELECT * FROM products WHERE name=%s", (name,))
        if not self.cursor.fetchone():
            print("Product not found!")
            return

        try:
            price = float(input("Enter new price: "))
            quantity = int(input("Enter new quantity: "))
        except ValueError:
            print(" Price and Quantity must be numbers!")
            return

        sql = "UPDATE products SET price=%s, quantity=%s WHERE name=%s"
        self.cursor.execute(sql, (price, quantity, name))
        self.conn.commit()
        print(f"{name} updated successfully!")

    def delete_product(self):
        print("\n--- Delete Product ---")
        name = input("Enter product name to delete: ").lower()
        sql = "DELETE FROM products WHERE name=%s"
        self.cursor.execute(sql, (name,))
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print(f" {name} deleted successfully!")
        else:
            print("⚠ Product not found!")

    # -------------------- CUSTOMER FUNCTIONS --------------------
    def purchase_product(self):
        print("\n--- Purchase Product ---")
        name = input("Enter product name: ").lower()

        # Fetch product
        self.cursor.execute("SELECT * FROM products WHERE name=%s", (name,))
        product = self.cursor.fetchone()
        if not product:
            print(" Product not available!")
            return

        _, pname, price, stock_qty = product

        if stock_qty == 0:
            print(" Out of stock!")
            return

        try:
            qty = int(input("Enter quantity to purchase: "))
        except ValueError:
            print("Quantity must be a number!")
            return

        if qty > stock_qty:
            print(f" Not enough stock! Available: {stock_qty}")
        else:
            # Update stock
            new_qty = stock_qty - qty
            self.cursor.execute("UPDATE products SET quantity=%s WHERE name=%s", (new_qty, name))

            # Calculate price with 2% margin
            total_price = price * qty
            final_price = total_price * 1.02

            # Save purchase in sales table
            self.cursor.execute(
                "INSERT INTO sales (product_name, quantity, final_price) VALUES (%s, %s, %s)",
                (name, qty, final_price)
            )
            self.conn.commit()

            print(f"You purchased {qty} {name}(s).")
            print(f"Final Price to Pay: {round(final_price,2)}")
            print("Stock updated successfully!")


# -------------------- MAIN PROGRAM --------------------
obj = InventoryDB()

while True:
    print("===== Inventory Management System =====")
    print("1. Manager")
    print("2. Customer")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if choice == 1:  # Manager Menu
        while True:
            print("\n--- Manager Menu ---")
            print("1. Add Product")
            print("2. View Products")
            print("3. Update Product")
            print("4. Delete Product")
            print("5. Back to Main Menu")

            try:
                m_choice = int(input("Enter your choice: "))
            except ValueError:
                print("⚠ Please enter a valid number!")
                continue

            if m_choice == 1:
                obj.add_product()
            elif m_choice == 2:
                obj.view_products()
            elif m_choice == 3:
                obj.update_product()
            elif m_choice == 4:
                obj.delete_product()
            elif m_choice == 5:
                break
            else:
                print(" Invalid choice!")

    elif choice == 2:  # Customer Menu
        while True:
            print("\n--- Customer Menu ---")
            print("1. Purchase Product")
            print("2. View Products")
            print("3. Back to Main Menu")

            try:
                c_choice = int(input("Enter your choice: "))
            except ValueError:
                print("⚠ Please enter a valid number!")
                continue

            if c_choice == 1:
                obj.purchase_product()
            elif c_choice == 2:
                obj.view_products()
            elif c_choice == 3:
                break
            else:
                print(" Invalid choice!")

    elif choice == 3:
        print(" Thank you! Exiting system.")
        break

    else:
        print(" Invalid choice! Try again.")
