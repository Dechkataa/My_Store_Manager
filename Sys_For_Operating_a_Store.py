import json


def purchase_history(purchase):
    try:
        with open("purchase_history.json", "r") as file:
            history = json.load(file)
    except FileNotFoundError:
        history = []
    except json.JSONDecodeError:
        history = []
    history.append(purchase)

    with open("purchase_history.json", "w") as file:
        json.dump(history, file, indent=4)


def show_purchase_history():
    try:
        with open("purchase_history.json", "r") as file:
            history = json.load(file)
        if not history:
            print("No purchases yet!")
            return
        print("\n--- Purchase History ---")
        for p in history:
            print(f"{p['name']} - {p['quantity']}")
        print("------------------------\n")
    except (FileNotFoundError, json.JSONDecodeError):
        print("No purchases yet!")


def load_products():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def new_product(products_):
    with open("products.json", "w") as file:
        json.dump(products_, file, indent=4)


products = load_products()
while True:
    command = int(input("1. Add product\n"
                        "2. Show product\n"
                        "3. Show All products\n"
                        "4. Buy product\n"
                        "5. Total value\n"
                        "6. Purchase history\n"
                        "7. Exit\n"
                        "Enter number:"))
    if command == 7:
        break
    if command == 1:
        new_product_dict = {}
        existing_product = False
        name = input("Name: ")

        for prod in products:
            if name == prod["name"]:
                quantity = int(input("There is existing product. Add quantity: "))
                prod["quantity"] += quantity
                existing_product = True
                new_product(products)
                break
        if not existing_product:
            new_product_dict["name"] = name
            new_product_dict["price"] = float(input("price: "))
            new_product_dict["quantity"] = int(input("quantity: "))
            products.append(new_product_dict)
            new_product(products)
            print("Product has been added")
    elif command == 2:
        search_name = input("Enter product name: \n")
        found = False
        for product in products:
            if product["name"] == search_name:
                print(f"Name: {product['name']}\n"
                      f"Price: {product['price']}\n"
                      f"Quantity: {product['quantity']}")
                found = True
                break
        if not found:
            print("Not Found!")

    elif command == 3:
        for product in products:
            print(f"Name: {product['name']}\n"
                  f"Price: {product['price']}\n"
                  f"Quantity: {product['quantity']}\n"
                  f"-------------------------------\n"
                  f"-------------------------------")
    elif command == 4:
        if products:

            search_name = input("Enter product to buy: ")
            quantity_to_delete = int(input("How much do you want (quantity):"))
            found = False
            for product in products:
                deleted_product = {"name": product["name"], "quantity": quantity_to_delete}
                if product["name"] == search_name:
                    found = True
                    if quantity_to_delete >= product["quantity"]:
                        purchase_history(deleted_product)
                        products.remove(product)
                        print("You bought every last one!!")
                    else:
                        purchase_history(deleted_product)
                        product["quantity"] -= quantity_to_delete
                        print("Your set!")
                    new_product(products)
                    break
            if not found:
                print("Product not found!")
        else:
            print("\nNo products yet to buy!\n")

    elif command == 5:
        total_price = 0.0
        for product in products:
            total_price += product["price"] * product["quantity"]

        print(f"Sum of all products:{total_price}")
    elif command == 6:
        show_purchase_history()
    else:
        print("Invalid input!")
