# User Management REST API - Postman Collection

This collection contains all the API endpoints for testing the User Management REST API.

## Import Instructions

1. Open Postman
2. Click "Import" button
3. Select this file (`postman_collection.json`)
4. The collection will be imported with all endpoints ready to test

## Base URL
```
http://127.0.0.1:5000
```

---

## Postman Collection JSON

Copy the JSON below and save it as `postman_collection.json`:

```json
{
  "info": {
    "name": "User Management API",
    "description": "REST API for managing user data with CRUD operations",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Get API Documentation",
      "request": {
        "method": "GET",
        "header": [],
        "url": {
          "raw": "http://127.0.0.1:5000/",
          "protocol": "http",
          "host": ["127", "0", "0", "1"],
          "port": "5000",
          "path": [""]
        },
        "description": "Get API documentation and available endpoints"
      }
    },
    {
      "name": "Get All Users",
      "request": {
        "method": "GET",
        "header": [],
        "url": {
          "raw": "http://127.0.0.1:5000/users",
          "protocol": "http",
          "host": ["127", "0", "0", "1"],
          "port": "5000",
          "path": ["users"]
        },
        "description": "Retrieve all users from the system"
      }
    },
    {
      "name": "Get User by ID",
      "request": {
        "method": "GET",
        "header": [],
        "url": {
          "raw": "http://127.0.0.1:5000/users/1",
          "protocol": "http",
          "host": ["127", "0", "0", "1"],
          "port": "5000",
          "path": ["users", "1"]
        },
        "description": "Retrieve a specific user by their ID"
      }
    },
    {
      "name": "Create New User",
      "request": {
        "method": "POST",
        "header": [
          {
            "key": "Content-Type",
            "value": "application/json"
          }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n  \"name\": \"John Doe\",\n  \"email\": \"john@example.com\",\n  \"age\": 30,\n  \"role\": \"developer\"\n}"
        },
        "url": {
          "raw": "http://127.0.0.1:5000/users",
          "protocol": "http",
          "host": ["127", "0", "0", "1"],
          "port": "5000",
          "path": ["users"]
        },
        "description": "Create a new user with name, email, age, and role"
      }
    },
    {
      "name": "Update User",
      "request": {
        "method": "PUT",
        "header": [
          {
            "key": "Content-Type",
            "value": "application/json"
          }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n  \"name\": \"John Doe Updated\",\n  \"age\": 31,\n  \"role\": \"senior developer\"\n}"
        },
        "url": {
          "raw": "http://127.0.0.1:5000/users/1",
          "protocol": "http",
          "host": ["127", "0", "0", "1"],
          "port": "5000",
          "path": ["users", "1"]
        },
        "description": "Update an existing user's information"
      }
    },
    {
      "name": "Delete User",
      "request": {
        "method": "DELETE",
        "header": [],
        "url": {
          "raw": "http://127.0.0.1:5000/users/1",
          "protocol": "http",
          "host": ["127", "0", "0", "1"],
          "port": "5000",
          "path": ["users", "1"]
        },
        "description": "Delete a user by their ID"
      }
    }
  ]
}
```

## Quick Test Sequence

1. **Get API Documentation** - Verify the API is running
2. **Get All Users** - Check initial state (empty)
3. **Create New User** - Add a user
4. **Get All Users** - Verify user was created
5. **Get User by ID** - Retrieve specific user
6. **Update User** - Modify user information
7. **Delete User** - Remove user
8. **Get All Users** - Confirm deletion

## Example Request Bodies

### Create User (Minimal)
```json
{
  "name": "Jane Doe",
  "email": "jane@example.com"
}
```

### Create User (Full)
```json
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "age": 28,
  "role": "designer"
}
```

### Update User (Partial)
```json
{
  "age": 29
}
```

### Update User (Full)
```json
{
  "name": "Jane Doe Updated",
  "email": "jane.new@example.com",
  "age": 29,
  "role": "senior designer"
}
```
