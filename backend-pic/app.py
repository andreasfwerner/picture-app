from flask import Flask, jsonify, session, request, Response
from flask_cors import CORS, cross_origin
import sqlite3

#DATABASE 

#TABLE users(id, username, password, profile_pic)

#posts(post_id INTEGER PRIMARY KEY NOT NULL, user_id INTEGER NOT NULL, image BLOB NOT NULL, description TEXT, likes INTEGER)

#comments(comment_id INTEGER PRIMARY KEY NOT NULL, user_id INTEGER NOT NULL, post_id INTEGER NOT NULL, comment TEXTR)
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
    #connect to database
    conn = db_connection()
    cur = conn.cursor()

    #get username and password from the POST request
    username = request.form['username']
    password = request.form['password']

    #get all usernames from the database
    cur.execute("SELECT username FROM users")
    users = cur.fetchall()
    
    #make a response
    response= {
        "unique": False
    }
    
    #check in username is unique
    for user in users:
        
        #if username is not unique, return a response 
        if user[0] == username:
            return jsonify(response)
    
    #get the image from the post request
    file = request.files['image']
    
    #turn image into binary
    img = file.read()
    
    #insert username, password and image into database. ID is generated automaticly
    cur.execute("INSERT INTO users(username,password,profile_pic) VALUES(?,?,?)",(username,password, img))
    conn.commit()
    
    #since username is unique change the response
    response["unique"]=True
    
    #return the response
    return jsonify(response)

@app.route("/post_posts", methods=["POST"])
def post_posts():
    #connect to database
    conn = db_connection()
    cur = conn.cursor()
        
    #get picture, id, description form POST request
    file = request.files['image']
    id = request.form['id']
    description = request.form['description']
    date = request.form['date']
    #turn image into binary
    img = file.read()
    
    #insert user_id, image, description, amout of likes into posts
    cur.execute("INSERT INTO posts(user_id,image,description,likes,date) VALUES(?,?,?,?,?)",(id,img,description,0,date))
    conn.commit()
    
    
    return jsonify({"response":True})
    



@app.route("/images")
def images():
    conn = db_connection()
    
    return jsonify("ja")



if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)