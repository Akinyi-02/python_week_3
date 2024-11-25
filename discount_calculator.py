# Step 1: Define the function to calculate the discount
def calculate_discount(price, discount_percent):
    # Step 2: Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Apply the discount and calculate the final price
        final_price = price * (1 - discount_percent / 100)
        return final_price
    else:
        # If discount is less than 20%, return the original price
        return price

# Step 3: Prompt the user to enter the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Step 4: Call the function and print the final price
final_price = calculate_discount(price, discount_percent)
print(f"The final price is: {final_price:.2f}")
