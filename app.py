from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Flask App!'

@app.route('/about')
def about():
    return 'This is a simple Flask web application.'

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    result = a + b
    return jsonify({'result': result})


@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    assert 1 == 1
    # data = request.get_json()
    # a = data.get('a')
    # b = data.get('b')
    # result = a * b
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)