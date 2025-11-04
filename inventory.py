#We create our variables
name = ""
price = 0.0
amount = 0
totalCost = 0.0

#This function checks if the input is a string containing only letters
def is_Str(text):
    result = text
    if not result.isalpha():
            result = is_Str(input("Invalid input. Please enter a valid name (letters only): "))
    return result

#This function checks if the input is a non-negative number
def is_valid(number):
    result = number
    try:
        result = float(number)
        if result >= 0:
            return result
        else:
            result = input("Invalid input. Please enter a valid number (Cannot be less than 0): ")
            result = is_valid(result)
    except ValueError:
        result = input("Invalid input. Please enter a valid input: ")
        result = is_valid(result)
    return result

#This funcition checks if the input is an integer (not a fraction)
def is_int(number):
    result = is_valid(int(number))
    while True:
        try:
            if not isinstance(result, float):
                return int(result)
            else:
                #print("Debug: result on else", result, "as ", str(type(number).__name__))
                result = input("Invalid input. Please enter a valid number (Cannot be fraction): ")
        except ValueError:
            result = input("Invalid input. Please enter a valid input: ")

#Here we set our variables using the functions above
name = is_Str(str(input("Enter the product name: ")))
price = is_valid(float(input("Enter the product price: ")))
amount = is_int(input("Enter the product amount: "))

#This function calculates the total cost that is price multiplied by amount
def total_cost(price, amount):
    return price * amount

#Here we call the function to calculate total cost
totalCost = total_cost(price, amount)

#Finally, we print the results
print(f"Product name: {name}, Price: {price}, Amount: {amount}, Total Cost: {totalCost}")

#The code avobe requests the user to input a product name, price, and amount. It validates the inputs to ensure the name contains only letters and that the price and amount are non-negative. It then calculates the total cost by multiplying the price by the amount and prints out all the details