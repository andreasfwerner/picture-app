from flask import Flask, jsonify, session, request, Response
from flask_cors import CORS, cross_origin
import sqlite3

#DATABASE 

#TABLE users(id, username, password, profile_pic)

#TABLE posts(post_id, user_id, image, comment, likes)

#TABLE test(id, image)

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
    print(rows)
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

@app.route("/register", methods=["POST"])
def register():
    conn = db_connection()
    cur = conn.cursor()
    
    data = request.get_json()

    cur.execute("SELECT username FROM users")
    users = cur.fetchall()
    
    response= {
        "unique": False
    }
    
    for user in users:
        if user[0] == data["username"]:
            return jsonify(response)
    
    cur.execute("INSERT INTO users VALUES(NULL,'{}','{}')".format(data["username"],data["password"]))
    conn.commit()
    
    response["unique"]=True
    
    return jsonify(response)

@app.route("/post_posts", methods=["POST"])
def post_posts():
    conn = db_connection()
    cur = conn.cursor()
    
    file = request.files['image']

    img = file.read()
    
    cur.execute("INSERT INTO test(id,image) VALUES(?,?)",(1,img))
    
    
    conn.commit()
    return jsonify({"response":True})
    



@app.route("/images")
def images():
    conn = db_connection()
    
    return jsonify("ja")



if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)