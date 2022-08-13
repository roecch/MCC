import mysql
from flask import Flask, render_template, request, jsonify
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


@app.route('/retrieve', methods=['GET'])
def retrieve():
    name = request.args['name']
    if name and request.method == 'GET':
        cursor = mysql.connection.cursor()
        p = Player(name, cursor)
        d = p.calc_cur_games()
        d.append(p.cal_player_avg())
        return jsonify(d)


@app.route('/event', methods=['GET', 'POST'])
def event():
    return render_template('event.html')


@app.route('/get_data')
def get_data():
    return 0


if __name__ == '__main__':
    app.run(debug=True)
