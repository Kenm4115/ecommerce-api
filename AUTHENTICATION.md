
# Authentication Setup

## Description
The E-commerce API uses **Django REST Framework** with **Token-Based Authentication** to secure endpoints.

### Steps to Use Authentication

1. **Obtain a Token**
   - Endpoint: `/api/token-auth/`
   - Method: POST
   - Request Body:
     ```json
     {
         "username": "your_username",
         "password": "your_password"
     }
     ```
   - Response:
     ```json
     {
         "token": "your_token"
     }
     ```

2. **Access Protected Endpoints**
   - Include the token in the `Authorization` header:
     ```
     Authorization: Token <your_token>
     ```

   Example:
   ```bash
   curl -X GET http://127.0.0.1:8000/api/products/ \
        -H "Authorization: Token your_token"
