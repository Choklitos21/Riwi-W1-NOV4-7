import csv

# Saves the info inside 'inventory' into the file inventory.csv
# It gave the option to the user to reemplace all inside inventory.csv with the current 'inventory'
# Or merge the current 'inventory' into the inventory.csv, modifying old elements and adding the new ones
def saveCSV(inventory):
    optionFlag = True
    while optionFlag:
        option = str(input("""
        Do you want to replace the information stored in the CSV or merge it?
         (Merging will keep the names but replace their prices and quantities with those of the new inventory)
         y/yes To replace it
         n/no To merge it
         ->: """)).lower()

        if option == "y" or option == "yes":
            with open('inventory.csv', 'w', newline='') as old_file_csv:
                saver = csv.writer(old_file_csv)
                saver.writerow(["Name", "Price", "Amount"])
                for i in inventory:
                    saver.writerow([i["name"], i["price"], i["amount"]])
            optionFlag = False

        elif option == "n" or option == "no":

            dataOnCSV = loadCSV()
            mergedInventory = []

            for old_item in dataOnCSV:
                found = False

                for new_item in inventory:
                    if old_item["name"] == new_item["name"]:
                        mergedInventory.append({
                            "name": old_item["name"],
                            "price": new_item["price"],
                            "amount": new_item["amount"]
                        })
                        found = True
                        break
                if not found:
                    mergedInventory.append(old_item)

            for new_item in inventory:
                if not any(i["name"] == new_item["name"] for i in dataOnCSV):
                    mergedInventory.append(new_item)

            with open('inventory.csv', 'w', newline='') as old_file_csv:
                saver = csv.writer(old_file_csv)
                saver.writerow(["Name", "Price", "Amount"])
                for item in mergedInventory:
                    saver.writerow([item["name"], item["price"], item["amount"]])

            optionFlag = False
        else:
            print("Option not valid, use only y/yes or n/no")

    print("************ PRODUCTS SAVED AS CSV ************")

# Take the info inside inventory.csv and upload it into 'inventory'
def loadCSV():
    with open('inventory.csv', 'r') as file_csv:
        data = csv.reader(file_csv)
        newList = []
        for i in data:
            newList.append({
                "name": i[0],
                "price": i[1],
                "amount": i[2]
            })

        newList.pop(0)
        return newList

# Show with format what it's saved in inventory.csv
def showCSV():
    with open('inventory.csv', 'r') as file_csv:
        # Crea un objeto reader
        data = csv.reader(file_csv)
        # Itera sobre cada fila del archivo
        print("********* PRODUCT *********")
        text = ""
        flag = False
        for i in data:
            if flag:
                text += f"""
                ********* PRODUCT *********
                Name: {i[0]}
                Price: {i[1]}
                Price: {i[2]}\n
                """
            flag = True
        print(text)
