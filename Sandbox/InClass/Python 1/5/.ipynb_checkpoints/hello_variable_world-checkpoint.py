"""
Percent Increase Bonus Activity

- Coded Joe Geoghegan 14Feb2022

# Formulas used
# Increase = Current Price - Original Price
# Percent Increase = Increase / Original x 100
"""

original_price = None # float variable for original_price
current_price = None # float variable for current_price
increase = None # float variable = Current Price -- Original Price (this is an unneeded line)
percent_increase = None # Increase / Original x 100 -- Original Price (this is an unneeded line)

# Prompt Variables
original_price = int(input("Enter Original Price: $"))
current_price = int(input("Enter Current Price: $"))

# Calculate difference between current_price and original_price
increase = current_price - original_price

# Calculate percent_increase
percent_increase = (increase / original_price)*100

# Print original_price
print(f"\nApple's original stock price was ${original_price}")

# Print current_price
print(f"Apples current stock price is ${current_price}")

# Print percent_increase
print("Apple's stock price increased by", "{:.2f}%".format(percent_increase))