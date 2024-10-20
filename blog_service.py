from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database for blogs
blogs = []

@app.route('/blogs/create', methods=['POST'])
def create_blog():
    blog_data = request.get_json()
    blogs.append(blog_data)
    return jsonify({"message": "Blog created successfully"}), 201

@app.route('/blogs', methods=['GET'])
def get_blogs():
    return jsonify(blogs), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
