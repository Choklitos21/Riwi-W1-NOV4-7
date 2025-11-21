import csv

# inventory = [
#     {
#         "name": "Book",
#         "price": 10.50,
#         "amount": 10
#     },
#     {
#         "name": "Laptop",
#         "price": 59.99,
#         "amount": 10
#     },
#     {
#         "name": "Pencil",
#         "price": 2.00,
#         "amount": 10
#     }
# ]

def saveCSV(inventory):
    with open('inventory.csv', 'w', newline='') as old_file_csv:
        saver = csv.writer(old_file_csv)
        saver.writerow(["Name", "Price", "Amount"])
        # saver.writerows(inventory)
        for i in inventory:
            saver.writerow([i["name"], i["price"], i["amount"]])

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