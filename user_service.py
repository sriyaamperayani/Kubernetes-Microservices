from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database (could be replaced with a database connection)
users = []

@app.route('/users/register', methods=['POST'])
def register_user():
    user_data = request.get_json()
    users.append(user_data)
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/users/login', methods=['POST'])
def login_user():
    user_data = request.get_json()
    for user in users:
        if user['username'] == user_data['username'] and user['password'] == user_data['password']:
            return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
