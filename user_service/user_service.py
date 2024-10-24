import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, jsonify
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)



'''from flask import Flask, request, jsonify

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
    return jsonify({"message": "Invalid credentials"}), 401'''


