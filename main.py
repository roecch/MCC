import mysql
from flask import Flask, redirect, url_for, render_template, request, jsonify
from flask_mysqldb import MySQL
from python.Player import Player

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Iamc00l!rsb897h4'
app.config['MYSQL_DB'] = 'MCC'

mysql = MySQL(app)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/retrieve', methods=['GET', 'POST'])
def retrieve():
    name = request.args['name']
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        d = Player(name, cursor).calc_all_games()
        return jsonify(d)


if __name__ == '__main__':
    app.run(debug=True)
