from distutils.log import debug
from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from config import host, database, user, password
import json
import psycopg2.extras
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

connection = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = database
)
connection.autocommit = True

@app.route("/")
def ReaderFiles():
    try:
        crus = connection.cursor()
        with crus as cursor:
            cursor.execute (
                    """CREATE TABLE basicForm (
                    ids SERIAL PRIMARY KEY,
                    hotel VARCHAR(500) NOT NULL,
                    topics VARCHAR(500) NOT NULL,
                    timesal VARCHAR(500) NOT NULL,
                    hotelName VARCHAR(500) NOT NULL
                ) ;"""
            )
        return render_template('index.html')
                   
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated')
    
    return render_template('index.html')

@app.route("/results", methods=['POST'])
def Results():
    try:
        crsr = connection.cursor()
        with crsr as cursor:
            cursor.execute (
                """SELECT * FROM basicForm ;"""
        )                
                
            return f"Server : {cursor.fetchall()}"
                               
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)


@app.route("/Base", methods=['POST'])
def Base(): 
    cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        hotel = request.form['hotel']
        topics = request.form['topics']
        timesal = request.form['timesal']
        hotelName = request.form['hname']
        cur.execute (
                """INSERT INTO basicForm (hotel,topics,timesal,hotelName) VALUES (%s,%s,%s,%s)""", (hotel, topics, timesal,hotelName)
                )  
        connection.commit()
        return render_template('index.html')
    

if __name__ == "__main__":  
    app.run(debug=True)