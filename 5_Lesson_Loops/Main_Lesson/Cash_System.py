# --- Solution 1: build invoice as a single string incrementally ---
print("Welcome to Smart Cashier System")
print("Enter product name (or 'done' to finish):")

username = "Abdullah"
password = '1234567890'
subtotal = 0.0
invoice = ""
prodectCount = 1

while True:
    currentusername = input("Enter the usernmae: ")
    currentpassword = input("Enter the password: ")
    if currentpassword == username and currentpassword == password:
        product = input("Product name: ")
        if product == "":
            print("The prodect can't be null!")
            break
        if product.lower().strip() == 'done':
            break
        price = input("Price: ")
        if price=="" or not price.isdigit():
            print("The price most be a number can't be string!")
            break
        price = float(price)
        subtotal += price
        # Add a formatted line for this product
        invoice += f"{prodectCount}.{product.capitalize():<15} ${price:>8.2f}\n"
        prodectCount += 1
    else:
        print("Fail to sign in please enter a correct username or a correct password")

# Tax and discount
tax = subtotal * 0.15
discount = 0.0
if subtotal > 1000:
    discount = subtotal * 0.10   # 10% discount on large purchases

final_total = subtotal + tax - discount

# Append summary lines to the invoice
invoice += "-" * 30 + "\n"
invoice += f"Subtotal:          ${subtotal:>8.2f}\n"
invoice += f"Tax (15%):         ${tax:>8.2f}\n"
if discount > 0:
    invoice += f"Discount (10%):   -${discount:>8.2f}\n"
invoice += f"Total:             ${final_total:>8.2f}\n"

print("\n===== FINAL INVOICE =====")
print(invoice)