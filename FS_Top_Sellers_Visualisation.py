import pyodbc


rooms = []
room_total = []

conn = pyodbc.connect\
    (r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=N:\Fruit Sale Project\2019AnthisFruit.accdb;')
cursor = conn.cursor()
cursor.execute('select * from FruitSale')

for rows in cursor.fetchall():
    rooms.append(rows[1])
    room_total.append(rows[4])

print(rooms)

item_sum = 0
for item in room_total:
    if item is not None:
        items = item_sum + item
    print(item)

count = 0
for item in rooms:
    if '502B' == item:
        count = count + 1

print(count)
print(item_sum)
