#We create our variables


#Create a list with a dictionary inside
inventory = []

def addProduct(newName, newPrice, newAmount):
    inventory.append({
        "name": newName,
        "price": newPrice,
        "amount": newAmount
    })
    print(f"""\n
    *********** CREATED ***********
    -------------------------
    |+ Name: {newName}
    |+ Price: {newPrice}
    |+ Amount: {newAmount}
    |-------------------------
    """)

def printInventory():
    count = 1
    if len(inventory) > 0:
        for i in inventory:
            print(f"""\n
            |+ PRODUCTO #{count}
            --------------------------
            |+ Name: {i["name"]}
            |+ Price: {i["price"]}
            |+ Amount: {i["amount"]}
            |-------------------------
            """)
            count += 1
    else:
        print("""\n
        *** No products have been saved yet ***
        """)

def calculateStatistics():
    total_inventory_value = 0
    total_items_saved = 0

    if len(inventory) > 0:
        for i in inventory:
            total_items_saved += 1
            total_inventory_value += i["amount"] * i["price"]

        print(f"""
        ****************** STATISTICS ******************
        |-----------------------------------------------
        |+ Total number of registered products: {total_items_saved}
        |+ Total inventory value: {total_inventory_value}
        |-----------------------------------------------
        """)
    else:
        print("""\n
        *** No products saved, unable to create statistics ***
        """)

#This function checks if the input is a string containing only letters
def isStr(text):
    result = text
    if not result.isalpha():
            result = isStr(input("Invalid input. Please enter a valid name (letters only): "))
    return result

#This function checks if the input is a non-negative number
def isValid(number):
    result = number
    try:
        result = float(number)
        if result >= 0:
            return result
        else:
            result = input("Invalid input. Please enter a valid number (Cannot be less than 0): ")
            result = isValid(result)
    except ValueError:
        result = input("Invalid input. Please enter a valid input: ")
        result = isValid(result)
    return result

#This function checks if the input is an integer (not a fraction)
def isInt(number):
    result = isValid(int(number))
    while True:
        result = int(result)
        try:
            if not isinstance(result, float):
                return int(result)
            else:
                result = input("Invalid input. Please enter a valid number (Cannot be fraction): ")
        except ValueError:
            result = input("Invalid input. Please enter a valid input: ")



