# Task 4: User Management REST API with Flask

## 📋 Overview
A RESTful API built with Flask that provides complete CRUD (Create, Read, Update, Delete) operations for managing user data. The API follows REST principles and includes comprehensive error handling, input validation, and proper HTTP status codes.

## ✨ Features Implemented

### Core Functionality
- ✅ **GET /users** - Retrieve all users
- ✅ **GET /users/<id>** - Retrieve a specific user by ID
- ✅ **POST /users** - Create a new user
- ✅ **PUT /users/<id>** - Update an existing user
- ✅ **DELETE /users/<id>** - Delete a user
- ✅ **GET /** - API documentation endpoint

### Technical Features
- ✅ **RESTful Design** - Follows REST API best practices
- ✅ **Input Validation** - Validates all incoming data
- ✅ **Error Handling** - Comprehensive error responses with proper HTTP codes
- ✅ **JSON Responses** - All responses in JSON format
- ✅ **Email Validation** - Basic email format checking
- ✅ **Duplicate Prevention** - Prevents duplicate email addresses
- ✅ **Timestamps** - Automatic created_at and updated_at timestamps
- ✅ **Auto-incrementing IDs** - Unique ID generation for each user
- ✅ **In-memory Storage** - Fast dictionary-based storage
- ✅ **CORS Ready** - Can be extended with CORS support

## 🛠️ Technologies Used
- **Framework**: Flask 3.0.0
- **Language**: Python 3.12
- **Storage**: In-memory dictionary
- **Testing Tools**: cURL, Postman

## 📁 Project Structure
```
Task 4/
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── test_api.sh          # Bash script for testing all endpoints
├── POSTMAN_GUIDE.md     # Postman collection and usage guide
├── requirement.md       # Task requirements
└── README.md            # This file
```

## 🚀 How to Run

### 1. Install Dependencies
```bash
cd "/workspaces/ElevenLabs/Task 4"
pip install -r requirements.txt
```

Or install Flask directly:
```bash
pip install flask
```

### 2. Start the Server
```bash
python app.py
```

The server will start on `http://127.0.0.1:5000`

### 3. Test the API

#### Option A: Using the Test Script
```bash
./test_api.sh
```

#### Option B: Using cURL manually
```bash
# Get all users
curl http://127.0.0.1:5000/users

# Create a user
curl -X POST http://127.0.0.1:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com", "age": 30}'
```

#### Option C: Using Postman
See `POSTMAN_GUIDE.md` for detailed Postman instructions and collection.

> [!NOTE] 
> **Note** This is an educational project. All data is stored in run time so data will be lost when the server stops or restarts. For production use, consider adding authentication, database persistence, proper logging, and security measures.

## 💡 API Endpoints Documentation

### Base URL
```
http://127.0.0.1:5000
```

### 1. Get API Documentation
```http
GET /
```

**Response (200 OK):**
```json
{
  "message": "Welcome to User Management API",
  "version": "1.0.0",
  "endpoints": {
    "GET /users": "Retrieve all users",
    "GET /users/<id>": "Retrieve a specific user by ID",
    "POST /users": "Create a new user",
    "PUT /users/<id>": "Update an existing user",
    "DELETE /users/<id>": "Delete a user"
  }
}
```

### 2. Get All Users
```http
GET /users
```

**Response (200 OK):**
```json
{
  "success": true,
  "count": 2,
  "users": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "age": 30,
      "role": "developer",
      "created_at": "2025-11-18T10:30:00.123456",
      "updated_at": "2025-11-18T10:30:00.123456"
    }
  ]
}
```

### 3. Get User by ID
```http
GET /users/{id}
```

**Response (200 OK):**
```json
{
  "success": true,
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30,
    "role": "developer",
    "created_at": "2025-11-18T10:30:00.123456",
    "updated_at": "2025-11-18T10:30:00.123456"
  }
}
```

**Response (404 Not Found):**
```json
{
  "success": false,
  "error": "User with ID 999 not found"
}
```

### 4. Create New User
```http
POST /users
Content-Type: application/json
```

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "age": 30,
  "role": "developer"
}
```

**Required Fields:** `name`, `email`  
**Optional Fields:** `age`, `role`

**Response (201 Created):**
```json
{
  "success": true,
  "message": "User created successfully",
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30,
    "role": "developer",
    "created_at": "2025-11-18T10:30:00.123456",
    "updated_at": "2025-11-18T10:30:00.123456"
  }
}
```

**Response (400 Bad Request):**
```json
{
  "success": false,
  "error": "'email' is required"
}
```

**Response (409 Conflict):**
```json
{
  "success": false,
  "error": "Email already exists"
}
```

### 5. Update User
```http
PUT /users/{id}
Content-Type: application/json
```

**Request Body (all fields optional):**
```json
{
  "name": "John Doe Updated",
  "email": "john.new@example.com",
  "age": 31,
  "role": "senior developer"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "User updated successfully",
  "user": {
    "id": 1,
    "name": "John Doe Updated",
    "email": "john.new@example.com",
    "age": 31,
    "role": "senior developer",
    "created_at": "2025-11-18T10:30:00.123456",
    "updated_at": "2025-11-18T11:45:00.789012"
  }
}
```

**Response (404 Not Found):**
```json
{
  "success": false,
  "error": "User with ID 999 not found"
}
```

### 6. Delete User
```http
DELETE /users/{id}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "User deleted successfully",
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  }
}
```

**Response (404 Not Found):**
```json
{
  "success": false,
  "error": "User with ID 999 not found"
}
```

## 🔧 Implementation Details

### User Data Model
```python
{
  "id": int,              # Auto-generated unique identifier
  "name": str,            # Required: User's full name
  "email": str,           # Required: User's email (must be unique)
  "age": int,             # Optional: User's age
  "role": str,            # Optional: User's role (default: "user")
  "created_at": str,      # Auto-generated: ISO format timestamp
  "updated_at": str       # Auto-updated: ISO format timestamp
}
```

### HTTP Status Codes Used

| Status Code | Meaning | Used For |
|------------|---------|----------|
| 200 OK | Success | GET, PUT, DELETE operations |
| 201 Created | Resource created | POST (user created) |
| 400 Bad Request | Invalid input | Validation errors |
| 404 Not Found | Resource not found | User ID doesn't exist |
| 405 Method Not Allowed | Wrong HTTP method | Invalid method for endpoint |
| 409 Conflict | Resource conflict | Duplicate email |
| 500 Internal Server Error | Server error | Unexpected errors |

### Key Design Decisions

1. **In-Memory Storage**
   ```python
   users = {}  # Dictionary with user_id as key
   ```
   - Fast access and manipulation
   - Simple for demonstration
   - Data persists during server runtime
   - Lost on server restart (can be extended with database)

2. **Auto-Incrementing IDs**
   ```python
   next_user_id = 1
   def get_next_id():
       global next_user_id
       current_id = next_user_id
       next_user_id += 1
       return current_id
   ```
   - Ensures unique IDs for each user
   - Simple and predictable

3. **Input Validation**
   ```python
   def validate_user_data(data, required_fields=['name', 'email']):
       # Check required fields
       # Validate email format
       # Return error message if invalid
   ```
   - Validates all incoming data
   - Provides clear error messages
   - Prevents invalid data entry

4. **Email Uniqueness**
   - Checks for duplicate emails on creation
   - Checks for conflicts when updating email
   - Returns 409 Conflict status code

5. **Timestamps**
   - Automatic `created_at` on user creation
   - Automatic `updated_at` on user update
   - ISO format for compatibility

6. **Error Handlers**
   - Global error handlers for 404, 405, 500
   - Consistent JSON error responses
   - Helpful error messages

## 🎯 Learning Outcomes

Through this project, the following concepts were practiced:
- ✅ REST API design principles
- ✅ Flask framework and routing
- ✅ HTTP methods (GET, POST, PUT, DELETE)
- ✅ HTTP status codes
- ✅ JSON request/response handling
- ✅ Input validation and sanitization
- ✅ Error handling and custom error responses
- ✅ API endpoint design
- ✅ CRUD operations implementation
- ✅ In-memory data storage
- ✅ API testing with cURL and Postman

## 🧪 Testing Examples

### Using cURL

#### Create Multiple Users
```bash
# User 1
curl -X POST http://127.0.0.1:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "email": "alice@example.com", "age": 28, "role": "developer"}'

# User 2
curl -X POST http://127.0.0.1:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Bob", "email": "bob@example.com", "age": 35, "role": "manager"}'
```

#### Get All Users
```bash
curl http://127.0.0.1:5000/users
```

#### Get Specific User
```bash
curl http://127.0.0.1:5000/users/1
```

#### Update User
```bash
curl -X PUT http://127.0.0.1:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"age": 29, "role": "senior developer"}'
```

#### Delete User
```bash
curl -X DELETE http://127.0.0.1:5000/users/1
```

### Using the Test Script
The included `test_api.sh` script tests all endpoints automatically:
```bash
./test_api.sh
```

It performs:
- ✅ API documentation retrieval
- ✅ Creating multiple users
- ✅ Retrieving all users
- ✅ Retrieving specific users
- ✅ Updating users
- ✅ Deleting users
- ✅ Error cases (duplicate email, missing fields, non-existent user)

## 📊 Response Format

All API responses follow this consistent structure:

### Success Response
```json
{
  "success": true,
  "message": "Optional success message",
  "user": { /* user object */ },
  "users": [ /* array of users */ ],
  "count": 0
}
```

### Error Response
```json
{
  "success": false,
  "error": "Detailed error message"
}
```

## 🔒 Validation Rules

### Email Validation
- Must contain `@` symbol
- Must be unique across all users
- Required field for user creation

### Required Fields
- **POST /users**: `name`, `email` are required
- **PUT /users/<id>**: All fields optional (partial update supported)

### Default Values
- `role`: Defaults to `"user"` if not provided
- `age`: Optional, can be null

## 🔮 Future Enhancements (Optional)

Potential features that could be added:
- Database integration (SQLite, PostgreSQL, MongoDB)
- User authentication and JWT tokens
- Password hashing and security
- Pagination for large user lists
- Search and filtering capabilities
- Field-level validation (age range, name length)
- Rate limiting
- API versioning
- Logging and monitoring
- CORS support for frontend integration
- OpenAPI/Swagger documentation
- Unit tests and integration tests
- Docker containerization

## 🐛 Troubleshooting

### Port Already in Use
```
Error: Address already in use
```
**Solution**: Change the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Flask Not Found
```
ModuleNotFoundError: No module named 'flask'
```
**Solution**: Install Flask:
```bash
pip install flask
```

### JSON Parsing Error
```
Error: Failed to decode JSON object
```
**Solution**: Ensure you're sending valid JSON with proper Content-Type header:
```bash
-H "Content-Type: application/json"
```

### Connection Refused
```
curl: (7) Failed to connect to 127.0.0.1 port 5000
```
**Solution**: Make sure the Flask server is running:
```bash
python app.py
```

## 📝 API Testing Checklist

- [ ] Server starts without errors
- [ ] GET / returns API documentation
- [ ] GET /users returns empty list initially
- [ ] POST /users creates a new user
- [ ] POST /users validates required fields
- [ ] POST /users prevents duplicate emails
- [ ] GET /users returns created users
- [ ] GET /users/<id> returns specific user
- [ ] GET /users/<id> returns 404 for non-existent user
- [ ] PUT /users/<id> updates user information
- [ ] PUT /users/<id> prevents duplicate email on update
- [ ] DELETE /users/<id> removes user
- [ ] DELETE /users/<id> returns 404 for non-existent user

## 📄 Dependencies

### requirements.txt
```
flask==3.0.0
```

## 👨‍💻 Author

Developed as part of the ElevenLabs coding assessment - Task 4

## 📄 License

This project is created for educational purposes.

---

## 🎓 REST API Best Practices Implemented

1. ✅ **Resource-based URLs** - `/users` instead of `/getUsers`
2. ✅ **HTTP Methods** - Proper use of GET, POST, PUT, DELETE
3. ✅ **Status Codes** - Appropriate HTTP status codes
4. ✅ **JSON Format** - Consistent JSON responses
5. ✅ **Error Handling** - Meaningful error messages
6. ✅ **Validation** - Input validation and sanitization
7. ✅ **Idempotency** - PUT and DELETE are idempotent
8. ✅ **Documentation** - API documentation endpoint

**Note**: This is an educational project. All data is stored in run time, so data will be lost when the server stops or restarts. For production use, consider adding authentication, database persistence, proper logging, and security measures.
