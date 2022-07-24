from flask import Flask, jsonify, request
from _helper import tensor_helper
import numpy as np
import json

app = Flask(__name__)
t = tensor_helper.TensorHelper('./')

def run():
    app.run(host='0.0.0.0', port=8888, debug=True)

'''
API動いてるか見る用
Hellowを返すだけ
'''
@app.route('/')
def hellow():
    return jsonify({'message': 'Hellow'})


'''
推論用APIエンドポイント

'''
@app.route('/inference', methods=["post"])
def inference():
    # 送信データをJSONデコード
    d = json.loads(request.form['data'])
    # 推測用モデルデータを読み込み
    t.loadModel()
    # [data] の形状になっているNumpy配列を作る必要があるので再変換
    img = np.asarray(json.loads(d['tensor']))
    # 推論
    _r = t.predict(np.asarray([img]))
    print(_r)
    return json.dumps({'inference' : _r.tolist()})
    
