from flask import Flask, session, render_template, request, g, url_for, redirect, session, flash, abort
import os
import sqlite3

app = Flask(__name__)
app.secret_key = "code_review123" # encrypt the secret via file

###########################################################
#####################   MAIN STUFF   ######################
###########################################################

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'POST' and 'user' in request.form and 'pass' in request.form:
        username = request.form["user"]
        password = request.form["pass"]

        # Account Verification
        account = user_login(username, password)

        if account != "None":
            #return redirect(url_for("admin"))
            return "<h1>SUCCESS</h1>"
        else:
            return render_template("home.html")

    return render_template("home.html")


###########################################################
####################   HELPER STUFF   #####################
###########################################################

def user_login(user, pwd):
    db = sqlite3.connect("database.db")

    cursor = db.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (user, pwd))
    account = cursor.fetchone()
    if account:
        return account
    else:
        return "None"

def create_database():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)')
    cursor.execute('INSERT INTO users (username, password) VALUES ("admin", "123")')

    connection.commit()
    connection.close()

if __name__ == "__main__":
    #create_database()
    app.run()