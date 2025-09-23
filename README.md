# PA3_MUSONG_2ECEA

#### What is this about?

This project is all about using Pandas, a Python library, to handle data like a table in Excel but with code. We practice:

Loading a dataset (like opening an Excel file in Python)

Previewing the data (first and last rows)

Picking out specific rows and columns using codes like .iloc and .loc.

#### Problem 1 — Surname_Pandas-P1.py

Code:

````
import pandas as pd

# Load the CSV file into a table called 'cars'
cars = pd.read_csv("http://bit.ly/Cars_file")

# Show the first 5 rows
print(cars.head())

# Show the last 5 rows
print(cars.tail())
````
I loaded the dataset from a CSV link using ````pd.read_csv()````, then used ````.head()```` and ````.tail()```` to quickly preview the first 5 rows and last 5 rows. This is better than printing the whole table.

#### How it Works?

```` import pandas as pd ```` - Turns on the Pandas tool in Python.

````pd.read_csv(...) ```` - Opens the CSV file and puts it into a table called cars.

````.head() ````- Shows the first 5 rows of the table.

````.tail()```` - Shows the last 5 rows of the table.

Think of this part as “opening the file and peeking at the top and bottom of the list.”

#### Problem 2 — Surname_Pandas-P2.py
Code:
````
import pandas as pd
cars = pd.read_csv("http://bit.ly/Cars_file")

# a) First 5 rows with odd-numbered columns
print(cars.iloc[:5, ::2])

# b) Row for Mazda RX4
print(cars.loc[cars["Model"] == "Mazda RX4"])

# c) Cylinders of Camaro Z28
print(cars.loc[cars["Model"] == "Camaro Z28", ["Model", "cyl"]])

# d) Cyl & gear for Mazda RX4 Wag, Ford Pantera L, Honda Civic
sel = (cars["Model"] == "Mazda RX4 Wag") | (cars["Model"] == "Ford Pantera L") | (cars["Model"] == "Honda Civic")
print(cars.loc[sel, ["Model", "cyl", "gear"]])
````
I practiced different ways of selecting data. Using ````.iloc````, I showed the first 5 rows with odd-numbered columns. Using ````.loc````, I filtered rows based on conditions like when the Model is Mazda RX4 or Camaro Z28, and displayed only the needed columns such as cylinders or gears. For multiple cars, I made a combined filter (````sel````) using OR (````|````) conditions.
#### How it Works?

````cars.iloc[:5, ::2]```` - iloc means “pick by position (row/column number).”

```` :5 = first 5 rows.````

````::2 = every other column (1, 3, 5…).```` Result: A small table of the first 5 rows with odd-numbered columns.

````cars.loc[cars["Model"] == "Mazda RX4"]````

````loc means “pick by label or condition.”````

````cars["Model"] == "Mazda RX4" ```` - finds the row where the model is Mazda RX4. Result: Full details of the Mazda RX4 row.

````cars.loc[cars["Model"] == "Camaro Z28", ["Model", "cyl"]]````
- This looks for the row with Model = Camaro Z28.
- Only shows the Model and cyl (cylinders) columns.

Result: Tells us how many cylinders Camaro Z28 has.

````sel = (cars["Model"] == "Mazda RX4 Wag") | (cars["Model"] == "Ford Pantera L") | (cars["Model"] == "Honda Civic") cars.loc[sel, ["Model", "cyl", "gear"]] ```` - This creates a filter (sel) that selects rows if the Model matches one of the three.

Only shows Model, cyl, and gear columns.
Result: A small table with cylinders and gear type for Mazda RX4 Wag, Ford Pantera L, and Honda Civic.
