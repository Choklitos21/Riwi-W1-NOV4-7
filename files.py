import csv

inventory = [
    {
        "name": "Book",
        "price": 10.50,
        "amount": 10
    },
    {
        "name": "Laptop",
        "price": 59.99,
        "amount": 10
    },
    {
        "name": "Pencil",
        "price": 2.00,
        "amount": 10
    }
]

def saveCSV():
    # --- Para escribir datos ---
    # Abre el archivo en modo escritura ('w')
    with open('inventory.csv', 'w', newline='') as old_file_csv:
        # Crea un objeto writer
        saver = csv.writer(old_file_csv)
        # Escribe una lista de datos como una
        saver.writerow(["Name", "Price", "Amount"])
        for i in inventory:
            saver.writerows([i.values()])

def loadCSV():
    with open('inventory.csv', 'r') as file_csv:
        # Crea un objeto reader
        data = csv.reader(file_csv)
        # Itera sobre cada fila del archivo
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


loadCSV()