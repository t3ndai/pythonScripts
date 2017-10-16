import os
import sqlite3
from flask import Flask, render_template, request, json
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)

conn = sqlite3.connect('database.db')
print('Opened database successfully')

conn.execute("DROP TABLE IF EXISTS Users")
conn.execute("""CREATE TABLE Users
			(user_id integer primary key autoincrement,
			user_name varchar(45) not null,
			user_username varchar(45) not null,
			user_password varchar(45) not null);""")

print('Table created successfully')
conn.close()

@app.route("/")
def main():
	'''entry page of application'''
	return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
	'''User sign up page'''
	return render_template('signup.html')

@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
	'''user sign up function from button'''
	try:
		#read the posted values from the UI
		_name = request.form['inputName']
		_email = request.form['inputEmail']
		_password = request.form['inputPassword']
		_hashed_password = generate_password_hash(_password)

		#validate the received values
		if _name and _email and _password:

			conn = sqlite3.connect('database.db')
			cursor = conn.cursor()

			cur.execute("INSERT INTO Users (user_name, user_username, user_password) VALUES (?, ?, ?)" (_name, _email, _hashed_password))

			conn.commit()

			return json.dumps({'html':'<span>All fields are good !!</span>'})


		else:
			return json.dumps({'html':'<span>Enter the required fields</span>'})

	
	except:
		conn.rollback()
		msg = 'error in insert operation'

	finally:
		return render_template("result.html", msg = msg)
		cursor.close()
		conn.close()


if __name__ == "__main__":
	app.run(debug=True)