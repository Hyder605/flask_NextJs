from flask import Flask, jsonify, request

app = Flask(__name__)

users = []

@app.route('/add-user', methods=['POST'])
def add_user():
    name = request.json['name']
    age = request.json['age']
    user = {'name': name, 'age': age}
    addd={user.name+user.age}
    # users.append(user)
    users.append(addd)

    return jsonify({'message': 'User added successfully'})

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})

if __name__ == '__main__':
    app.run(host="0.0.0.0")
