#!/bin/bash

# Test script for User Management API
# Make sure the Flask server is running before executing this script

API_URL="http://127.0.0.1:5000"

echo "=================================="
echo "Testing User Management API"
echo "=================================="
echo ""

# Test 1: Get API Documentation
echo "1️⃣  Testing GET / (API Documentation)"
curl -s $API_URL/ | python -m json.tool
echo -e "\n"

# Test 2: Get all users (should be empty initially)
echo "2️⃣  Testing GET /users (Initial - should be empty)"
curl -s $API_URL/users | python -m json.tool
echo -e "\n"

# Test 3: Create first user
echo "3️⃣  Testing POST /users (Create user 1)"
curl -s -X POST $API_URL/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "age": 28,
    "role": "developer"
  }' | python -m json.tool
echo -e "\n"

# Test 4: Create second user
echo "4️⃣  Testing POST /users (Create user 2)"
curl -s -X POST $API_URL/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Bob Smith",
    "email": "bob@example.com",
    "age": 35,
    "role": "manager"
  }' | python -m json.tool
echo -e "\n"

# Test 5: Create third user
echo "5️⃣  Testing POST /users (Create user 3)"
curl -s -X POST $API_URL/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Charlie Brown",
    "email": "charlie@example.com",
    "age": 42
  }' | python -m json.tool
echo -e "\n"

# Test 6: Get all users
echo "6️⃣  Testing GET /users (Should show 3 users)"
curl -s $API_URL/users | python -m json.tool
echo -e "\n"

# Test 7: Get specific user
echo "7️⃣  Testing GET /users/1 (Get user by ID)"
curl -s $API_URL/users/1 | python -m json.tool
echo -e "\n"

# Test 8: Update user
echo "8️⃣  Testing PUT /users/1 (Update user)"
curl -s -X PUT $API_URL/users/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice Johnson Updated",
    "age": 29,
    "role": "senior developer"
  }' | python -m json.tool
echo -e "\n"

# Test 9: Delete user
echo "9️⃣  Testing DELETE /users/2 (Delete user)"
curl -s -X DELETE $API_URL/users/2 | python -m json.tool
echo -e "\n"

# Test 10: Get all users after deletion
echo "🔟 Testing GET /users (After deletion - should show 2 users)"
curl -s $API_URL/users | python -m json.tool
echo -e "\n"

# Test 11: Try to create user with duplicate email
echo "1️⃣1️⃣  Testing POST /users (Duplicate email - should fail)"
curl -s -X POST $API_URL/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Another Alice",
    "email": "alice@example.com",
    "age": 25
  }' | python -m json.tool
echo -e "\n"

# Test 12: Try to get non-existent user
echo "1️⃣2️⃣  Testing GET /users/999 (Non-existent user - should return 404)"
curl -s $API_URL/users/999 | python -m json.tool
echo -e "\n"

# Test 13: Try to create user without required fields
echo "1️⃣3️⃣  Testing POST /users (Missing required fields - should fail)"
curl -s -X POST $API_URL/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Incomplete User"
  }' | python -m json.tool
echo -e "\n"

echo "=================================="
echo "✅ All API tests completed!"
echo "=================================="
