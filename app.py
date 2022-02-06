from flask import Flask, render_template
import pyodbc
import numpy as np
app = Flask(__name__)
# databaseName = 'db12'
# username = 'dbserverdb1admin'
# password = 'mYiphone1$13106'
# server = 'dbserverdb1.database.windows.net'
# driver= '{ODBC Driver 13 for SQL Server}'
# connstr = 'DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+databaseName+';UID='+username+';PWD='+ password
import pymssql  
conn = pymssql.connect(server='dbserverdb1.database.windows.net', user='dbserverdb1admin', password='mYiphone1$13106', database='db12')
# try:
# conn = pyodbc.connect(connstr)
cursor = conn.cursor()
# except Exception:
#     print("Error connecting DB")


@app.route('/')
def index():

    arr=[]
    arr1=[]
    # conn = pyodbc.connect(connstr)
    # cursor = conn.cursor()
    query = 'SELECT TOP 3 * FROM earthquakes'
    cursor.execute(query)
    print(cursor)
    row = cursor.fetchall() 
    print(type(row))
    while row:  
        arr1 = np.asarray(row)
        arr.append(arr1) 
        row = cursor.fetchone() 
    return render_template('main.html', table=arr)
