from inventory import *
mydb = pymysql.connect(host="localhost",user="root",password = "",database="Inventory")
mycursor=mydb.cursor()

class Inventory:
    def add_product(self, name, price, quantity):
        try:
            self.cursor.execute("INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)", 
                                (name, price, quantity))
            self.conn.commit()
            print(f"Product '{name}' added successfully!")
        except Exception as e:
            print(" Error adding product:", e)
   
   
    def view_product(self):
        self.cursor.execute("SELECT * FROM products")
        query = self.cursor.fetchall()
        if query:
            print("\nProduct List:")
            for row in query:
                print(f"ID: {row[0]} | Name: {row[1]} | Price: ₹{row[2]} | Qty: {row[3]}")
        else:
            print(" No products available.")

    def update_product(self, product_id, name, price, quantity):
        product_id = int(input("Enter a ID:"))
        name= input("enter a Product Name:")
        price=input("Enter a Price:")
        quantity=int(input("Enter a Quantity:"))
        query = "update  data set name='%s' where id = '%s' "
        args = (name,price,quantity)

        mycursor.execute(query%args)
        mydb.commit()
        print("Data Updated!!")

    def delete_product(self,product_id):
        product_id = int(input("Enter a Product ID:"))
        query = "delete from data where id = '%s'"
        args = (id)
        mycursor.execute(query%args)
        mydb.commit()
        print("Data Deleted!!")
    
    def purchase_product(self, product_id, quantity):
        try:
            self.cursor.execute("SELECT name, price, quantity FROM products WHERE id=%s", (product_id,))
            product = self.cursor.fetchone()
            if not product:
                raise Exception("Product not found!")
            name, price, stock = product

            if stock < quantity:
                raise Exception(" Out of stock!")

            
            sell_price = price + (price * 0.20)
            total_price = sell_price * quantity

            
            cursor.execute("UPDATE products SET quantity = quantity - %s WHERE id = %s", 
                                (quantity, product_id))
            conn.commit()
            print(f"Purchased {quantity} x {name} for ₹{total_price:.2f} (incl. 20% margin).")
        except Exception as e:
            print("Error:", e)


while True:
        print("\n Inventory Management")
        print("1. Manager")
        print("2. Customer")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1": 
            while True:
                print("\n Manager Menu ")
                print("1. Add Product")
                print("2. View Products")
                print("3. Update Product")
                print("4. Delete Product")
                print("5. Back to Main Menu")
                choice = input("Enter choice: ")

                if choice == 1:
                    name = input("Enter product name: ")
                    price = float(input("Enter product price: "))
                    qty = int(input("Enter quantity: "))
                    inv.add_product(name, price, qty)
                elif choice == 2:
                    inv.view_products()
                elif choice == 3:
                    pid = int(input("Enter product ID to update: "))
                    name = input("Enter new name (leave blank if no change): ") or None
                    price = input("Enter new price (leave blank if no change): ")
                    price = float(price) if price else None
                    qty = input("Enter new quantity (leave blank if no change): ")
                    qty = int(qty) if qty else None
                    inv.update_product(pid, name, price, qty)
                elif choice == 4:
                    pid = int(input("Enter product ID to delete: "))
                    inv.delete_product(pid)
                elif choice == "5":
                    break
                else:
                    print("Invalid choice!")

        elif choice == 2:  
            while True:
                print("\nCustomer Menu ")
                print("1. View Products")
                print("2. Purchase Product")
                print("3. Back to Main Menu")
                ch = input("Enter choice: ")

                if choice ==1:
                    inv.view_products()
                elif choice == 2:
                    pid = int(input("Enter product ID: "))
                    qty = int(input("Enter quantity: "))
                    inv.purchase_product(pid, qty)
                elif choice == 3:
                    break
                else:
                    print("Invalid choice!")

        elif choice == 3:
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")



