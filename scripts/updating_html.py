from bs4 import BeautifulSoup as bs
import os
import re
from flask import Flask, render_template, url_for, request, jsonify
from flask import make_response

app = Flask(__name__)

# with open("../templates/index.html") as fp:
#     soup = bs(fp, "html.parser")
#
# for item in soup.select(".pc"):
#     print(item['id'])
#
# print('here')

# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/retrieve', methods=['GET', 'POST'])
# def retrieve(data):
#     if data:
#         return jsonify({'valid' + data})
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
