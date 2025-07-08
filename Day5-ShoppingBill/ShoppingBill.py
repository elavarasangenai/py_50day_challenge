# ShoppingBill.py

def calculate_total_with_tax(prices, tax_percent):
    subtotal = sum(prices)
    tax = subtotal * (tax_percent / 100)
    total = subtotal + tax
    return subtotal, tax, total

def main():
    prices = []
    for i in range(1, 4):
        while True:
            try:
                price = float(input(f"Enter price of item {i}: "))
                if price < 0:
                    print("Price cannot be negative. Please enter again.")
                    continue
                prices.append(price)
                break
            except ValueError:
                print("Please enter a valid number.")
    while True:
        try:
            tax_percent = float(input("Enter tax percentage: "))
            if tax_percent < 0:
                print("Tax percentage cannot be negative. Please enter again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    subtotal, tax, total = calculate_total_with_tax(prices, tax_percent)
    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total Bill: ${total:.2f}")

if __name__ == "__main__":
    main()
