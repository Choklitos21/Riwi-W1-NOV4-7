#Functions imported from other files
from files import loadCSV, saveCSV
from services import (addProduct,
                      printInventory,
                      searchOnInventory,
                      updateProduct,
                      deleteOneInventory,
                      calculateStatistics)

#Variable to save products on memory while the program is running
inventory = []

#Main function to operate between files, giving options to the user
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

        #Variable to control when the user wants to exit or continue with the program
        option = str(input("Select and option from 1 to 9 only: "))
        match option:
            case "1":
                #Goes to services.py and add an element to 'inventory'
                addProduct(inventory)
            case "2":
                # Goes to services.py and print all element inside 'inventory'
                printInventory(inventory)
            case "3":
                # Goes to services.py search for an element and return the element if it exits
                searchOnInventory(inventory, "", True)
            case "4":
                # Goes to services.py search for an element and update price and amount
                updateProduct(inventory)
            case "5":
                # Goes to services.py, search for an element and deletes it if the element exits
                deleteOneInventory(inventory, "")
            case "6":
                # Goes to services.py to calculate statistics
                calculateStatistics(inventory)
            case "7":
                # Goes to files.py to save 'inventory' into the file inventory.scv
                saveCSV(inventory)
            case "8":
                # Goes to files.py to load the info inside inventory.csv into the 'inventory'
                inventory = loadCSV()
            case "9":
                # Last message before closing the program
                print("Program finished")
                menuFlag = False
            case _:
                # Message in case the user chose an option outside number 1 and number 7
                print("Invalid option, try again with numbers from 1 to 9 only")

menu()