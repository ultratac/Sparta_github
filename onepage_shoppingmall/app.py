
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.onepageshoppingmall           # 'dbsparta'라는 이름의 db를 만듭니다.


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/cart', methods=['POST'])
def saving():
	# 클라이언트로부터 데이터를 받는 부분
    name_from_client = request.form['name_send']
    quantity_from_client = request.form['quantity_send']
    address_from_client = request.form['address_send']
    phone_from_client = request.form['phone_send']
	# mongoDB에 넣을 데이터를 딕셔너리 형태로 정의 
    order = {'name': name_from_client, 'quantity': quantity_from_client, 'address': address_from_client,'phone': phone_from_client }
    # mongoDB에 데이터 인서트 
    db.orders.insert_one(order)

    return jsonify({'result': 'success', 'msg': '주문이 완료되었습니다.'})


@app.route('/cart', methods=['GET'])
def listing():
    result = list(db.orders.find({},{'_id':0}))
    return jsonify({'result':'success', 'order_list':result})


if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)

