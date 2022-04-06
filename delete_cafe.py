import csv


def delete_cafe():

    updatedlist = []

    def updatefile(updatedlist):
        with open('cafe-data.csv', "w", newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(updatedlist)
            print("Cafe list has been updated.")

    needs_deleting = True
    while needs_deleting:
        with open('cafe-data.csv', newline='') as csv_file:
            csv_data = csv.reader(csv_file)
            cafe_name = input("What cafe would you like to remove from the list? (if necessary)\n"
                              "Or just press enter to skip. ").title()

            for row in csv_data:
                if row[0] != cafe_name:
                    updatedlist.append(row)

            print(updatedlist)
            updatefile(updatedlist)

            delete_more = input("Are there more cafes you need to remove? (Y / N) ").lower()
            if delete_more == "n":
                needs_deleting = False
            elif delete_more == "y":
                needs_deleting = True
            elif delete_more != "y" or delete_more != "no":
                input("Please enter Y or N. ").lower()

