print("Welcome to the Gift Registry!")

print("1. Add a gift")
print("2. View gift registry")
print("3. Mark a gift as purchased")
print("4. Remove a gift")
print("5. Exit")

choice = input('Enter your choice: ')
if choice == '1':
    gift_name = input('Enter the name of the gift: ')
    gift_price = float(input('Enter the gift price: $'))

print(gift_name, "was added for $", gift_price)

