
# E-Commerce Product API

This project is a Django-based backend API for managing products and categories in an e-commerce platform.



# Authentication Setup for E-Commerce Product API


## Authentication Methods
The API uses **Token Authentication** via Django REST Framework.

### Setup Details
1. Token Authentication is implemented using DRF's `TokenAuthentication` class.
2. The `/api-token-auth/` endpoint is used to retrieve tokens for authenticated users.

## How to Test Authentication
### Step 1: Obtain a Token
Use the `/api-token-auth/` endpoint to retrieve a token:
```bash
curl -X POST http://localhost:8000/api-token-auth/ \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "password123"}'
