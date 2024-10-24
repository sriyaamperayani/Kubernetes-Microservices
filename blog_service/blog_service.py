import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, jsonify
from werkzeug.exceptions import abort

# In-memory database for blogs
blogs = []

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

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5002)


#@app.route('/blogs/create', methods=['POST'])
#def create_blog():
#    blog_data = request.get_json()
#    blogs.append(blog_data)
#    return jsonify({"message": "Blog created successfully"}), 201

#@app.route('/blogs', methods=['GET'])
#def get_blogs():
#    return jsonify(blogs), 200

#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5002)
