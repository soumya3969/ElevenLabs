"""
REST API with Flask - User Management System
A RESTful API for managing user data with CRUD operations.
"""

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage for users
users = {}
next_user_id = 1

# Helper function to generate user ID
def get_next_id():
    global next_user_id
    current_id = next_user_id
    next_user_id += 1
    return current_id

# Helper function to validate user data
def validate_user_data(data, required_fields=None):
    """Validate user data and return error message if invalid"""
    if required_fields is None:
        required_fields = ['name', 'email']
    
    if not data:
        return "Request body is required"
    
    for field in required_fields:
        if field not in data or not data[field]:
            return f"'{field}' is required"
    
    # Email validation (basic)
    if 'email' in data and '@' not in data['email']:
        return "Invalid email format"
    
    return None

@app.route('/')
def home():
    """Home endpoint with API documentation"""
    return jsonify({
        "message": "Welcome to User Management API",
        "version": "1.0.0",
        "endpoints": {
            "GET /users": "Retrieve all users",
            "GET /users/<id>": "Retrieve a specific user by ID",
            "POST /users": "Create a new user",
            "PUT /users/<id>": "Update an existing user",
            "DELETE /users/<id>": "Delete a user"
        },
        "example_user": {
            "name": "John Doe",
            "email": "john@example.com",
            "age": 30,
            "role": "developer"
        }
    }), 200

@app.route('/users', methods=['GET'])
def get_users():
    """GET /users - Retrieve all users"""
    return jsonify({
        "success": True,
        "count": len(users),
        "users": list(users.values())
    }), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """GET /users/<id> - Retrieve a specific user by ID"""
    if user_id not in users:
        return jsonify({
            "success": False,
            "error": f"User with ID {user_id} not found"
        }), 404
    
    return jsonify({
        "success": True,
        "user": users[user_id]
    }), 200

@app.route('/users', methods=['POST'])
def create_user():
    """POST /users - Create a new user"""
    data = request.get_json()
    
    # Validate input
    error = validate_user_data(data)
    if error:
        return jsonify({
            "success": False,
            "error": error
        }), 400
    
    # Check if email already exists
    for user in users.values():
        if user['email'] == data['email']:
            return jsonify({
                "success": False,
                "error": "Email already exists"
            }), 409
    
    # Create new user
    user_id = get_next_id()
    new_user = {
        "id": user_id,
        "name": data['name'],
        "email": data['email'],
        "age": data.get('age'),
        "role": data.get('role', 'user'),
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }
    
    users[user_id] = new_user
    
    return jsonify({
        "success": True,
        "message": "User created successfully",
        "user": new_user
    }), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """PUT /users/<id> - Update an existing user"""
    if user_id not in users:
        return jsonify({
            "success": False,
            "error": f"User with ID {user_id} not found"
        }), 404
    
    data = request.get_json()
    
    if not data:
        return jsonify({
            "success": False,
            "error": "Request body is required"
        }), 400
    
    # Check if email is being changed and already exists
    if 'email' in data and data['email'] != users[user_id]['email']:
        for uid, user in users.items():
            if uid != user_id and user['email'] == data['email']:
                return jsonify({
                    "success": False,
                    "error": "Email already exists"
                }), 409
    
    # Update user fields
    user = users[user_id]
    if 'name' in data:
        user['name'] = data['name']
    if 'email' in data:
        if '@' not in data['email']:
            return jsonify({
                "success": False,
                "error": "Invalid email format"
            }), 400
        user['email'] = data['email']
    if 'age' in data:
        user['age'] = data['age']
    if 'role' in data:
        user['role'] = data['role']
    
    user['updated_at'] = datetime.now().isoformat()
    
    return jsonify({
        "success": True,
        "message": "User updated successfully",
        "user": user
    }), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """DELETE /users/<id> - Delete a user"""
    if user_id not in users:
        return jsonify({
            "success": False,
            "error": f"User with ID {user_id} not found"
        }), 404
    
    deleted_user = users.pop(user_id)
    
    return jsonify({
        "success": True,
        "message": "User deleted successfully",
        "user": deleted_user
    }), 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        "success": False,
        "error": "Endpoint not found"
    }), 404

@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 errors"""
    return jsonify({
        "success": False,
        "error": "Method not allowed"
    }), 405

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        "success": False,
        "error": "Internal server error"
    }), 500

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 User Management API Server")
    print("="*60)
    print("📍 Running on: http://127.0.0.1:5000")
    print("📚 API Documentation: http://127.0.0.1:5000/")
    print("="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
