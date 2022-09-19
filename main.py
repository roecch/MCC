import mysql
from flask import Flask, render_template, request, jsonify, json
from flask_mysqldb import MySQL
from python.Player import Player
from python.constants import games

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


@app.route('/get_data', methods=['GET'])
def get_data():
    teams = json.loads(request.args['teams'])
    games.append('AVG')
    if teams and request.method == 'GET':
        print(teams)
        map = []
        for color, tmates in teams:
            teammates_map = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for tmate in tmates.split(','):
                if tmate != '':
                    cursor = mysql.connection.cursor()
                    p = Player(tmate, cursor)
                    d = p.calc_cur_games()
                    d.append(p.cal_player_avg())
                    teammates_map = [sum(x) for x in zip(*(teammates_map, d))]

            for i, game_avg in enumerate(teammates_map):
                print(game_avg)
                print(i)
                map.append({"color": color, "game": games[i], "pts": game_avg})
        return jsonify(map)


if __name__ == '__main__':
    app.run(debug=True)
