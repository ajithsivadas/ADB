from flask import Flask, render_template
import pyodbc
import numpy as np
app = Flask(__name__)

import pymssql  
conn = pymssql.connect(server='dbserverdb1.database.windows.net', user='dbserverdb1admin', password='mYiphone1$13106', database='db12')

cursor = conn.cursor()


@app.route('/')
def index():

    arr=[]
    arr1=[]
    query = 'SELECT TOP 3 * FROM [dbo].[earthquakes]'
    cursor.execute(query)
    print(cursor)
    row = cursor.fetchone() 
    while row:  
        arr1 = np.asarray(row)
        arr.append(arr1) 
        row = cursor.fetchone() 
    return render_template('main.html', table=arr)
