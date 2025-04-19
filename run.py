# run.py
from flask import Flask, request, jsonify
from app.models import db, User
from config import Config
from app import create_app

# Initialize the Flask app
app = create_app()

# Create tables in the database (if not already created)
with app.app_context():
    db.create_all()

# Create a simple route to verify the app works
@app.route('/')
def index():
    return '''
        <h1>Welcome to the Flask CRUD App!</h1>
        <a href="/users/">Go to Users CRUD</a>
    '''

# CRUD Routes for User model

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        image=data.get('image'),
        text=data.get('text')
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created", "user": data}), 201

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.username for user in users])

# Get a specific user by ID
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify({
        'username': user.username,
        'email': user.email,
        'image': user.image,
        'text': user.text
    })

# Update an existing user by ID
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)
    user.image = data.get('image', user.image)
    user.text = data.get('text', user.text)
    db.session.commit()
    return jsonify({"message": "User updated", "user": data})

# Delete a user by ID
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)