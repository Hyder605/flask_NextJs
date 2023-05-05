from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/')
def home():
    return jsonify({"lo":"Hello world"})

@app.route('/api')
def api():
    return jsonify({'message': 'KKDKD'})

if __name__ == '__main__':
    app.run(host="0.0.0.0")

