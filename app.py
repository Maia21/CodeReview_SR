from flask import Flask, session, render_template, request, g, url_for, redirect, session, flash, abort
import os
import sqlite3

app = Flask(__name__)
app.secret_key = "code_review123"

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

@app.route('/user/<uid>', methods=["POST", "GET"])
def see_user_profile(uid):
    current_user = session['conta']
    return render_template("profile.html", u = current_user)

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST' and 'name' in request.form and 'username' in request.form and 'password' in request.form:
        name = request.form["name"]
        username = request.form["username"]
        pwd = request.form["password"]

        if name != "" and username != "" and pwd != "":
            db = sqlite3.connect("database.db")
            cursor = db.cursor()
            cursor.execute('INSERT INTO users (username, password, name) VALUES (?, ?, ?);', (username, pwd, name))
            db.commit()
            db.close()

            return render_template("home.html")

    return render_template("register.html")

@app.route('/logout', methods=['POST'])
def logout():
    return redirect(url_for("home"))


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

if __name__ == "__main__":
    #create_database()
    app.run()