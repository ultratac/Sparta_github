
from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

# HTML을 주는 부분


@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분


@app.route('/api/list', methods=['GET'])
def star_list():
    # 1. mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
    stars = list(db.mystar.find({},{'_id':False}).sort('like',-1))
    # 2. 성공하면 success 메시지와 함께 stars 목록을 클라이언트에 전달합니다.
    return jsonify({'result': 'success','star_list':stars})


@app.route('/api/like', methods=['POST'])
def add_like():
    name_receive = request.form['name_send'] ##받은배우이름을 name receive로 정의  
    moviestar = db.mystar.find_one({'name':name_receive}) ##name=name receive와 동일한 db를 하나 찾아 star로 정의 
    new_like = moviestar['like']+1  ##moviestar의 'like'에 1을 더한 것을 new like로 정의 
    db.mystar.update_one({'name':name_receive},{'$set':{'like':new_like}}) ##db d 업데이트 : 네임을 네임리시브로, 라이크를 뉴라이크로 
    return jsonify({'result': 'success'}) ##제이슨으로 결과값을 날려주기. 


@app.route('/api/delete', methods=['POST'])
def delete_star():
    name_receive = request.form['name_send'] 
    moviestar = db.mystar.find_one({'name':name_receive}) 
    deletMoviestar = db.mystar.delete_one({'name':name_receive})
    
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
