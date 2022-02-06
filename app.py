from flask import Flask, render_template
import pyodbc
app = Flask(__name__)
databaseName = 'db12'
username = 'dbserverdb1admin'
password = 'mYiphone1$13106'
server = 'dbserverdb1.database.windows.net'
driver= '{ODBC Driver 13 for SQL Server}'
connstr = 'DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+databaseName+';UID='+username+';PWD='+ password
try:
 
    conn = pyodbc.connect(connstr)
    cursor = conn.cursor()
except Exception:
    print("Error connecting DB")


@app.route('/')
def index():
    arr=[]
    query = "SELECT * FROM EARTHQUAKE LIMIT 10"
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)
    while data:
        arr.append(data)
        data = cursor.fetchone()
    return render_template('main.html', table=arr)
