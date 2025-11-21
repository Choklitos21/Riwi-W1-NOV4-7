from files import loadCSV, saveCSV
from services import (addProduct,
                      printInventory,
                      searchOnInventory,
                      updateProduct,
                      deleteOneInventory,
                      calculateStatistics)

inventory = []

def menu():
    global inventory
    menuFlag = True
    while menuFlag:
        print("""
        MENU
        1. Add product
        2. Show inventory
        3. Search product
        4. Update product
        5. Delete product
        6. Calculate statistics
        7. Save CSV
        8. Load CSV
        9. EXIT
        """)

        option = str(input("Select and option from 1 to 9 only: "))
        match option:
            case "1":
                addProduct(inventory)
            case "2":
                printInventory(inventory)
            case "3":
                searchOnInventory(inventory, "")
            case "4":
                updateProduct(inventory)
            case "5":
                deleteOneInventory(inventory, "")
            case "6":
                calculateStatistics(inventory)
            case "7":
                saveCSV(inventory)
            case "8":
                inventory = loadCSV()
            case "9":
                print("Program finished")
                menuFlag = False
            case _:
                print("Invalid option, try again with numbers from 1 to 7 only")

menu()