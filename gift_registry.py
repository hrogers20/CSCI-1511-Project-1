gifts = []

print("Welcome to the Gift Registry!")

while True:
    print("1. Add a gift")
    print("2. View gift registry")
    print("3. Mark a gift as purchased")
    print("4. Remove a gift")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        gift_name = input("Enter the name of the gift: ")
        gift_price = float(input("Enter the gift price: $"))

        gift = {
            "name": gift_name,
            "price": gift_price,
            "purchased": False
        }

        gifts.append(gift)
        print(gift_name, "was added for $", gift_price)

    elif choice == "2":
        for gift in gifts:
            if gift["purchased"] == True:
                print(gift["name"], "-", "$", gift["price"], "- Purchased")
            else:
                print(gift["name"], "-", "$", gift["price"], "- Not Purchased")

    elif choice == "3":
        gift_name = input("Enter the name of the gift that was purchased: ")

        for gift in gifts:
            if gift["name"] == gift_name:
                gift["purchased"] = True
                print(gift_name, "has been marked as purchased!")
                break

    elif choice == "4":
        gift_name = input("Enter the name of the gift you'd like to remove: ")

        for gift in gifts:
            if gift["name"] == gift_name:
                gifts.remove(gift)
                print(gift_name, "has been removed from the registry.")
                break