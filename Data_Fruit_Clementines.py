import pyodbc

teacher_code = []
clementines_order = []
clementines_no_none = []
item_sum = 0
index_count = 0

conn = pyodbc.connect\
    (r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=N:\Fruit Sale Project\2019AnthisFruit.accdb;')
cursor = conn.cursor()
cursor.execute('select * from FruitSale')

for rows in cursor.fetchall():
    teacher_code.append(rows[1])
    clementines_order.append(rows[7])


for item in clementines_order:
    print(item)

for stuff in clementines_order:
    if stuff == None:
        clementines_order.pop(index_count)
    elif stuff != None:
        item_sum = item_sum + stuff
        clementines_no_none.append(stuff)




count = 0
for item in teacher_code:
    if '502B' == item:
        count = count + 1

print(count)
print(item_sum)
