from files import loadCSV

inventory = []

def addProduct(name: str, price: float, amount: int):
    if searchOnInventory(name) is not None:
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
        return inventory
    else:
        print("Product already exists.")
        return None

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

def searchOnInventory(name): #return dictionary or none
    for i in inventory:
        if i["name"] == name:
            print(f"""\n
            *********** PRODUCT FOUND ***********
            |------------------------------------
            |+ Name: {i["name"]}
            |+ Price: {i["price"]}
            |+ Amount: {i["amount"]}
            |------------------------------------
            """)
            return i
    print(f"'{name}' was not found in the inventory.")
    return None

def updateProduct(name, newPrice: float|None, newAmount: int|None):
    for i in inventory:
        if i["name"] == name:
            print(f"""\n
            *********** OLD PRODUCT ***********
            |------------------------------------
            |+ Name: {i["name"]}
            |+ Price: {i["price"]}
            |+ Amount: {i["amount"]}
            |------------------------------------
            """)
            i["price"] = newPrice
            i["amount"] = newAmount
            print(f"""\n
            *********** PRODUCT UPDATED ***********
            |------------------------------------
            |+ Name: {i["name"]}
            |+ Price: {i["price"]}
            |+ Amount: {i["amount"]}
            |------------------------------------
            """)
            return i
    print(f"{name} was not found in the inventory.")
    return None

def deleteOneInventory(name):
    for i in inventory:
        if i["name"] == name:
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
    print(f"{name} was not found in the inventory.")
    return None

# Implementa calcular_estadisticas(inventario) para obtener:
# unidades_totales = suma de cantidad
# valor_total = suma de precio * cantidad
# producto_mas_caro (nombre y precio)
# producto_mayor_stock (nombre y cantidad)
# Muestra las estadísticas con formato legible.
# (Opcional) Usa una lambda para calcular el subtotal de cada producto:
# subtotal = (lambda p: p["precio"] * p["cantidad"])

def calculateStatistics(): #return tuple with statistics
    total_units = 0
    total_value = 0
    most_expensive = {}
    most_stock = {}

    for i in inventory:
        total_units += i["amount"]
        total_value += i["amount"] * i["price"]
        if i["price"] > most_expensive.get("price", 0):
            most_expensive = i
        if i["amount"] > most_stock.get("amount", 0):
            most_stock = i

    statistics = (total_units, total_value, most_expensive, most_stock)

    print(f"""
    |+ Total units: {total_units}
    |+ Total value: ${total_value}
    |+ Most expensive product: {most_expensive["name"]}
    |+ Product with most stock: {most_stock["name"]}
    |+ 
    """)

    return statistics

def initializeData():
    global inventory
    inventory = loadCSV()
    print("************* Inventory initialized *************")

# Verify data
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


