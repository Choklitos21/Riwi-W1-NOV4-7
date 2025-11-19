
def menu():
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

        option = str(input("Select and option from 1 to 0 only: "))
        match option:
            case "1":
                print("option")
            case "2":
                print("option")
            case "3":
                print("option")
            case "4":
                print("option")
            case "5":
                print("option")
            case "6":
                print("option")
            case "7":
                print("option")
            case "8":
                print("option")
            case "9":
                print("Program finished")
                menuFlag = False
            case _:
                print("Invalid option, try again with numbers from 1 to 7 only")

    pass