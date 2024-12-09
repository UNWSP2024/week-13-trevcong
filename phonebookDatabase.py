#AUTHOR: Trevor Conger
#DATE: 12/8/24
#TITLE: Phonebook database!

import sqlite3

connection = sqlite3.connect('phonebook.db')
cursor = connection.cursor()

# Main function
def main():
    while True:
        print("\nPhonebook CRUD Application")
        print("1. Add Entry")
        print("2. Look Up Number")
        print("3. Update Number")
        print("4. Delete Entry")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phoneNumber = input("Enter phone number: ")
            addEntry(name, phoneNumber)
        elif choice == '2':
            name = input("Enter name to look up: ")
            lookupNumber(name)
        elif choice == '3':
            name = input("Enter name to update: ")
            newPhoneNumber = input("Enter new phone number: ")
            updateNumber(name, newPhoneNumber)
        elif choice == '4':
            name = input("Enter name to delete: ")
            deleteEntry(name)
        elif choice == '5':
            print("Exiting the phonebook.")
            break
        else:
            print("Invalid choice. Please try again.")

#Phonebook Table Setup
#cursor is the connection to the database
def setupPhonebookTable(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS Entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone_number TEXT NOT NULL)''')
#Add Entry
#insert the name and phone number into the database
def addEntry(name, phoneNumber):
    cursor.execute('INSERT INTO Entries (name, phone_number) VALUES (?, ?)', (name, phoneNumber))
    connection.commit()
    print(f"Added {name} with phone number {phoneNumber}.")

#Lookup Number
#select the phone number from the database
def lookupNumber(name):
    cursor.execute('SELECT phone_number FROM Entries WHERE name = ?', (name,))
    result = cursor.fetchone()
    if result:
        print(f"{name}'s phone number is {result[0]}.")
    else:
        print(f"{name} not found in the phonebook.")

#Update Number
#update the phone number in the database
def updateNumber(name, newPhoneNumber):
    cursor.execute('UPDATE Entries SET phone_number = ? WHERE name = ?', (newPhoneNumber, name))
    connection.commit()
    if cursor.rowcount > 0:
        print(f"Updated {name}'s phone number to {newPhoneNumber}.")
    else:
        print(f"{name} not found in the phonebook.")

#Delete Entry
#delete the name from the database
def deleteEntry(name):
    cursor.execute('DELETE FROM Entries WHERE name = ?', (name,))
    connection.commit()
    if cursor.rowcount > 0:
        print(f"Deleted {name} from the phonebook.")
    else:
        print(f"{name} not found in the phonebook.")



if __name__ == '__main__':
    main()

connection.close()