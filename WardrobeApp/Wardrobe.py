import pyodbc
server = '(localdb)\Local'
database = 'Wardrobe_Project'
username = 'jason'
password = 'hrsdjr'
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()


#Insert, Update, Select, Delete
#https://www.microsoft.com/en-us/sql-server/developer-get-started/python/windows/step/2.html
insert = "INSERT INTO tablename (columnname, anothercolumn) VALUES (?,?);"
with cursor.execute(insert,'value, anothervalue'):
    print("Success")

update = "UPDATE tablename SET value1 = ? WHERE value2 = ?"
with cursor.execute(update,"value1",'value2"):
    print ("Success")

delete = "DELETE FROM tablename WHERE Name = ?"
with cursor.execute(delete,'value'):
    print ('Success')

select = "SELECT Name, Location FROM Employees;"
with cursor.execute(select):
    row = cursor.fetchone()
    while row:
        print (str(row[0]) + " " + str(row[1]))
        row = cursor.fetchone()


def insertDB():
    insert = "INSERT INTO tablename (columnname, anothercolumn) VALUES (?,?);"
    with cursor.execute(insert,'value, anothervalue'):
        print("Success")
    return(0)
    return fn_return_value


#cursor.execute('PantsSP')

#for i in cursor:
#    print(i)
 
#How can I let the user add to the columns? Ex: I only have 3 brands for 
#'PantsBrandID' but there are way more than that