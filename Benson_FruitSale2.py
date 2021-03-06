# Imports
import pyodbc
from plotly.graph_objects import Bar, Layout
from plotly import offline

# Lists/Variables
item_total = []
total = []
frequencies = []
total_sold = 0
b = 0

# Connecting to the Driver
conn = pyodbc.connect\
    (r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=N:\Fruit Sale Project\2018AnthisFruit.accdb;')
cursor = conn.cursor()
cursor.execute('select * from FruitSale')

# This simply just gets the required index you provide and appends it to item_total
for rows in cursor.fetchall():
    item_total.append(rows[4])

# This now, this is the stuff. This ciphers out the Nones and ignores them, by placing the float/integers into a list.
for item in item_total:
    if item is not None:
        total.append(item)

# This adds up all the items in the index for the column. (amount sold)
for thing in total:
    total_sold = total_sold + thing


# This finds the largest amount sold in one sitting. This becomes our x or y highest coordinate.
for i in total:
    if i > b:
        b = i
    elif i < b:
        b = b
max_result = b

for value in list(range(1, int(30))):
    frequency = total.count(value)
    frequencies.append(value)
    frequencies.append(frequency)



# Visualization
x_values = list(range(1,30))
y_values = frequencies[1::2]


data = [{
    'type': 'bar',
    'x': x_values,
    'y': y_values,
    'marker': {
        'color': 'rgb(100, 100, 150)',
        'line': {'width': 4, 'color': 'rgb(100, 75, 185)'}
    },
    'opacity': 1
}]

my_layout = {
    'title': f'How many clementines sold per person',
    'title_x': 0.5,
    'xaxis': {
        'title': 'Amount of clementines sold',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'how many people sold that amount of clementines',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_fruit_sale.html')
