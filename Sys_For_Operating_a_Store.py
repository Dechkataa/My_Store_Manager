products = []


while True:
    command = int(input("1. Add product\n"
                        "2. Show products\n"
                        "3. Search product\n"
                        "4. Buy product\n"
                        "5. Total value\n"
                        "6. Exit\n"
                        "Enter number:"))
    if command == 6:
        break
    if command == 1:
        product = {}
        existing_product = False
        name = input("Name: ")
        for product in products:
            if name == product["name"]:
                quantity = int(input("There is existing product.Add quantity:"))
                product["quantity"] += quantity
                existing_product = True
                break
        if not existing_product:
            product["name"] = name
            price = float(input("price: "))
            quantity = int(input("quantity: "))
            product["price"] = price
            product["quantity"] = quantity
            products.append(product)
            print("Product has been added")
    elif command == 2:
        search_name = input("Enter product name: \n")

        for product in products:
            if product["name"] == search_name:
                print(f"Name: {product['name']}\n"
                      f"Price: {product['price']}\n"
                      f"Quantity: {product['quantity']}")
                break
            else:
                print("Not Found!")

    elif command == 3:

        search_name = input("Enter product name: ")

        for product in products:
            if product["name"] == search_name:
                print("Product is available!")
                break
            else:
                print("Product is not available!")
    elif command == 4:
        if products:

            search_name = input("Enter product to buy: ")
            quantity_to_delete = int(input("How much do you want (quantity):"))
            for product in products:
                if quantity_to_delete >= product["quantity"]:
                    products.remove(product)
                    print("You bought every last one!!")
                else:
                    product["quantity"] -= quantity_to_delete
                    print("Your set !")
                break
        else:
            print("\nNo products yet to buy!\n")
    elif command == 5:
        total_price = 0.0
        for product in products:
            total_price += product["price"] * product["quantity"]

        print(f"Sum of all products:{total_price}")
    else:
        print("Invalid input!")

