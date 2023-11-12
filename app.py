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
            session['conta'] = account
            return redirect(url_for("user_profile"))
        else:
            return render_template("home.html")

    return render_template("home.html")

@app.route('/user', methods=["POST", "GET"])
def user_profile():
    current_user = session['conta']
    return render_template("user-profile.html", u = current_user)


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

# def get_current_user()

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