from flask import Flask, jsonify, session, request
from flask_cors import CORS, cross_origin
import sqlite3

from sqlalchemy import false



app = Flask(__name__)
app.config.from_object(__name__)


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def db_connection():
    conn = None
    try: 
        conn = sqlite3.connect("database.db")
    except sqlite3.error as e:
        print(e)
    return conn


@app.route("/")
def index():
    return
    
@app.route("/login",methods=["POST"])
def login():
    conn = db_connection()
    cur = conn.cursor()
    
    data = request.get_json()
    
    cur.execute("SELECT * FROM users WHERE username='{}'".format(data["username"]))
    
    #returns data, format [amout of users with username][0=id,1=username,2=password]
    rows = cur.fetchall()
    
    
    
    response={
                "loggedIn": False,
                "id": None,
                "username": None
            }
    
    if len(rows)!=0:
        #checks if password matches
        if rows[0][2]==data["password"]:
            response={
                "loggedIn": True,
                "id": rows[0][0],
                "username": rows[0][1]
            }
    return jsonify(response)

@app.route("/images")
def images():
    conn = db_connection()
    
    return jsonify("ja")

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)