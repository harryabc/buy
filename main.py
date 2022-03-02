from flask import Flask, request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/buy', methods=['POST'])
def buy():
    goods_id = request.values.get('id')
    data = {
            'status': 200,
            'message': '该功能待完善，请打开在线IDE进行编辑'
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
