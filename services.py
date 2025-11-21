
def addProduct(inventory):
    addProductFlag = True
    while addProductFlag:
        name = isStr(str(input("\nEnter the product name: "))).lower()
        price = isValid(input("\nEnter the product price: "))
        amount = isInt(input("\nEnter the product amount: "))
        if not searchOnInventory(inventory, name, False):
            inventory.append({
                "name": name[0],
                "price": price,
                "amount": amount
            })
            print(f"""\n
                *********** CREATED ***********
                -------------------------
                |+ Name: {name[0]}
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

def updateProduct(inventory):
    name, newPrice, newAmount = updatedInfoCheck()
    for i in inventory:
        if i["name"] == name:
            print(f"""\n
            *********** OLD PRODUCT ***********
            |------------------------------------
            |+ Name: {i["name"].capitalize()}
            |+ Price: {i["price"]}
            |+ Amount: {i["amount"]}
            |------------------------------------
            """)
            i["price"] = newPrice
            i["amount"] = newAmount
            print(f"""\n
            *********** PRODUCT UPDATED ***********
            |------------------------------------
            |+ Name: {i["name"].capitalize()}
            |+ Price: {i["price"]}
            |+ Amount: {i["amount"]}
            |------------------------------------
            """)
            return i
    print(f"{name} was not found in the inventory.")
    return None

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

def deleteOneInventory(inventory, name):
    newName = name
    if not newName:
        newName = isStr(str(input("\nEnter the product name: "))).lower(),
    for i in inventory:
        if i["name"] == newName:
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
    print(f"{newName} was not found in the inventory.")
    return None

# Implementa calcular_estadisticas(inventario) para obtener:
# unidades_totales = suma de cantidad
# valor_total = suma de precio * cantidad
# producto_mas_caro (nombre y precio)
# producto_mayor_stock (nombre y cantidad)
# Muestra las estadísticas con formato legible.
# (Opcional) Usa una lambda para calcular el subtotal de cada producto:
# subtotal = (lambda p: p["precio"] * p["cantidad"])

def calculateStatistics(inventory): #return tuple with statistics
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

#This function checks if the input is a string containing only letters
def isStr(text):
    result = text
    if not result.isalpha():
        result = isStr(input("Invalid input. Please enter a valid name (letters only): "))
    return str(result)

#This function checks if the input is a non-negative number
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
def isInt(number):
    result = isValid(number)
    while True:
        try:
            if not isinstance(result, float):
                return int(result)
            else:
                result = input("Invalid input. Please enter a valid number (Cannot be fraction): ")
        except ValueError:
            result = input("Invalid input. Please enter a valid input: ")


