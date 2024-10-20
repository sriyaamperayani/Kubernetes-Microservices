from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database for comments
comments = []

@app.route('/comments/add', methods=['POST'])
def add_comment():
    comment_data = request.get_json()
    comments.append(comment_data)
    return jsonify({"message": "Comment added successfully"}), 201

@app.route('/comments', methods=['GET'])
def get_comments():
    return jsonify(comments), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
