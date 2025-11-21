import csv

def saveCSV(inventory):
    dataOnCSV = loadCSV()
    with open('inventory.csv', 'w', newline='') as old_file_csv:
        saver = csv.writer(old_file_csv)
        saver.writerow(["Name", "Price", "Amount"])
        for i in inventory:
            for j in dataOnCSV:
                if i["name"] == j["name"]:
                    saver.writerow([j["name"], i["price"], i["amount"]])
                    break
                else:
                    saver.writerow([i["name"], i["price"], i["amount"]])
                    break

    print("************ PRODUCTS SAVED AS CSV ************")

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

# def initializeData():
#     inventory = loadCSV()
#     print("************* Inventory initialized *************")