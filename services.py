# This function add a product to the 'inventory'
def addProduct(inventory):
    addProductFlag = True
    while addProductFlag:
        name = isStr(str(input("\nEnter the product name: "))).lower()
        price = isValid(input("\nEnter the product price: "))
        amount = isInt(input("\nEnter the product amount: "))
        if not searchOnInventory(inventory, name, False):
            inventory.append({
                "name": name,
                "price": price,
                "amount": amount
            })
            print(f"""\n
                *********** CREATED ***********
                -------------------------
                |+ Name: {name}
                |+ Price: {price}
                |+ Amount: {amount}
                |-------------------------
                """)
        else:
            print("Product already exists.")

        answerFlag = True
        while answerFlag:
            answer = str(input("Do you want to add another product?: y/n ")).strip().lower()
            if answer == "y" or answer == "yes":
                answerFlag = False
            elif answer == "n" or answer == "no":
                answerFlag = False
                addProductFlag = False
                print("********** End of product addition **********")
            else:
                print("Option not valid, use only y/yes or n/no")

# This functions print all the items inside 'inventory' with an especial format
def printInventory(inventory):
    count = 1
    if len(inventory) > 0:
        for i in inventory:
            print(f"""\n
                |+ PRODUCTO #{count}
                --------------------------
                |+ Name: {i["name"].capitalize()}
                |+ Price: {i["price"]}
                |+ Amount: {i["amount"]}
                |-------------------------
                """)
            count += 1
    else:
        print("""\n
            **** No products have been saved yet ****
            """)

# This function search for a specific item inside 'inventory'
# Returns the product if its found, or None if it doesn't exist
def searchOnInventory(inventory, name, flag):
    newName = name
    if not newName:
        newName = isStr(str(input("\nEnter the product name: ")))
    for i in inventory:
        if i["name"] == newName[0]:
            print(f"""\n
            *********** PRODUCT FOUND ***********
            |------------------------------------
            |+ Name: {i["name"].capitalize()}
            |+ Price: {i["price"]}
            |+ Amount: {i["amount"]}
            |------------------------------------
            """)
            return i
    if flag:
        print(f"********* {newName[0]} was not found in the inventory *********")
    return None

# This functions checks if the item exists in the 'inventory' and updates its price and/or amount
# Returns the product updated if its found, or None if it doesn't exist
def updateProduct(inventory):
    name, newPrice, newAmount = updatedInfoCheck()
    for i in inventory:
        if i["name"] == name[0]:
            print(f"""\n
            *********** OLD PRODUCT ***********
            |------------------------------------
            |+ Name: {i["name"].capitalize()}
            |+ Price: {i["price"]}
            |+ Amount: {i["amount"]}
            |------------------------------------
            """)
            i["price"] = newPrice if newPrice != None else i["price"]
            i["amount"] = newAmount if newAmount != None else i["amount"]
            print(f"""\n
            *********** PRODUCT UPDATED ***********
            |------------------------------------
            |+ Name: {i["name"].capitalize()}
            |+ Price: {i["price"]}
            |+ Amount: {i["amount"]}
            |------------------------------------
            """)
            return i
    print(f"delete {name[0]} was not found in the inventory.")
    return None

# This functions check if the user wants to update the price and/or the amount of the product
# Return the name, price and amount that the user just enter
def updatedInfoCheck():
    name = isStr(str(input("\nEnter the product name: "))).lower()

    priceFlag = True
    while priceFlag:
        updatePrice = str(input("Do you wish to update the price?: y/n")).strip().lower()
        if updatePrice == "y" or updatePrice == "yes":
            price = isValid(float(input("\nEnter the product price: ")))
            priceFlag = False
        elif updatePrice == "n" or updatePrice == "no":
            price = None
            priceFlag = False
        else:
            print("Option not valid, use only y/yes or n/no")

    amountFlag = True
    while amountFlag:
        updateAmount = str(input("Do you wish to update the amount?: y/n")).strip().lower()
        if updateAmount == "y" or updateAmount == "yes":
            amount = isInt(input("\nEnter the product amount: "))
            amountFlag = False
        elif updateAmount == "n" or updateAmount == "no":
            amount = None
            amountFlag = False
        else:
            print("Option not valid, use only y/yes or n/no")

    return name, price, amount

# This functions search for an element and deletes the element if it exists
# Returns the product that was deleted if its found, or None if it doesn't exist
def deleteOneInventory(inventory, name):
    newName = name
    if not newName:
        newName = isStr(str(input("\nEnter the product name: "))).lower(),
    for i in inventory:
        if i["name"] == newName[0]:
            print(f"""
            *********** DELETED ***********
            -------------------------------
            |+ Name: {i["name"]}
            |+ Price: {i["price"]}
            |+ Amount: {i["amount"]}
            |------------------------------
            """)
            inventory.pop(inventory.index(i))
            return inventory
    print(f"{newName[0]} was not found in the inventory.")
    return None

# This function calculate the next statistics
# total_units: The total of units between all products in the 'inventory'
# total_value: The total value of between all products in the 'inventory'
# most_expensive: The product that has the higher cost
# most_stock: The product with more units (amount) in the 'inventory'
# Return a tuple with all the previous variables
def calculateStatistics(inventory):
    total_units = 0
    total_value = 0
    most_expensive = {
        "name": "",
        "price": 0,
        "amount": 0
    }
    most_stock = {
        "name": "",
        "price": 0,
        "amount": 0
    }

    if inventory:
        for i in inventory:
            total_units += int(i["amount"])
            total_value += float(i["amount"]) * float(i["price"])
            if float(i["price"]) > float(most_expensive["price"]):
                most_expensive = i
            if int(i["amount"]) > int(most_stock["amount"]):
                most_stock = i
    else:
        print("""\n
            **** No products have been saved yet ****
            """)
        return inventory

    statistics = (total_units, total_value, most_expensive, most_stock)

    print(f"""
    |+ Total units: {total_units}
    |+ Total value: ${total_value:.2f}
    |+ Most expensive product: {most_expensive["name"]}
    |+ Product with most stock: {most_stock["name"]}
    """)

    return statistics

# Verify data

# This function checks if the input is a string containing only letters
# Return the text if it's correct
def isStr(text):
    result = text
    if not result.isalpha():
        result = isStr(input("Invalid input. Please enter a valid name (letters only): "))
    return str(result)

#This function checks if the input is a non-negative number
# Return the number if it's correct
def isValid(number):
    result = number
    try:
        result = float(number)
        if result >= 0:
            return float(result)
        else:
            result = input("Invalid input. Please enter a valid number (Cannot be less than 0): ")
            result = isValid(result)
    except ValueError:
        result = input("Invalid input. Please enter a valid input: ")
        result = isValid(result)
    return float(result)

#This function checks if the input is an integer (not a fraction)
# Return the text if it's correct
def isInt(number):
    result = int(isValid(number))
    while True:
        try:
            if not isinstance(result, float):
                return int(result)
            else:
                result = input("Invalid input. Please enter a valid number (Cannot be fraction): ")
        except ValueError:
            result = input("Invalid input. Please enter a valid input: ")


