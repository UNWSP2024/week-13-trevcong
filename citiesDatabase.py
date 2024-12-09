import sqlite3
import tkinter as tk
from tkinter import ttk


# Main function
def main():
    connection = None
    try:
        connection = sqlite3.connect('cities.db')
        cursor = connection.cursor()

        setupCitiesTable(cursor)

        connection.commit()
        cities = fetchCities(cursor)

        displayGUI(cities)
        
    except sqlite3.Error as error:
        print(f"Database error: {error}")
    finally:
        if connection:
            connection.close()

# Cities Table Setup
# setup the cities table
# drop the table if it exists
# create the table
# insert the cities data    
def setupCitiesTable(cursor):
    cursor.execute("DROP TABLE IF EXISTS Cities")

    cursor.execute('''
        CREATE TABLE Cities (
            CityID INTEGER PRIMARY KEY AUTOINCREMENT,
            CityName TEXT NOT NULL,
            Population REAL NOT NULL
        )
    ''')

    citiesData = [
        ('New York', 18593220),
        ('Los Angeles', 13423451),
        ('Chicago', 9481473),
        ('Dallas-Fort Worth', 7604753),
        ('Houston', 7151120),
        ('Washington, D.C.', 6350423),
        ('Miami', 6316130),
        ('Philadelphia', 6248725),
        ('Atlanta', 6169264),
        ('Boston', 4897394),
        ('San Francisco', 4856324),
        ('Phoenix', 4933264),
        ('Seattle', 4018883),
        ('Minneapolis-St. Paul', 3620941),
        ('San Diego', 3338330),
        ('Tampa', 3249628),
        ('Denver', 3052580),
        ('St. Louis', 2829300),
        ('Orlando', 2806300),
        ('San Antonio', 2725242),
    ]
    cursor.executemany("INSERT INTO Cities (CityName, Population) VALUES (?, ?)", citiesData)

# Fetch Cities
# fetch the cities from the database
# return the cities
def fetchCities(cursor):
    cursor.execute("SELECT CityID, CityName, Population FROM Cities ORDER BY CityID")
    return cursor.fetchall()

# Display GUI
# display the cities in a GUI
def displayGUI(cities):
    root = tk.Tk()
    root.title("Cities Database Viewer")

    tree = ttk.Treeview(root, columns=("CityID", "CityName", "Population"), show="headings")
    tree.heading("CityID", text="ID")
    tree.heading("CityName", text="City Name")
    tree.heading("Population", text="Population")

    for city in cities:
        tree.insert("", tk.END, values=city)

    tree.pack(fill=tk.BOTH, expand=True)

    root.mainloop()

if __name__ == '__main__':
    main()
