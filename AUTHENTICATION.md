
# Authentication for E-commerce Product API

This API uses **JWT (JSON Web Token)** authentication for secure access to protected endpoints. Users must obtain a token upon login and include it in the `Authorization` header of each request to interact with protected resources like managing products.

---

## Endpoints for Authentication

### 1. **Register a New User**
- **Endpoint**: `/api/register/`
- **Method**: `POST`
- **Description**: Allows users to register by providing their username, email, and password.
- **Request Payload**:
  ```json
  {
      "username": "testuser",
      "email": "testuser@example.com",
      "password": "password123"
  }
  ```
- **Response**:
  ```json
  {
      "id": 1,
      "username": "testuser",
      "email": "testuser@example.com"
  }
  ```

---

### 2. **Obtain JWT Token**
- **Endpoint**: `/api/token/`
- **Method**: `POST`
- **Description**: Authenticates a user and provides a JWT token to access protected endpoints.
- **Request Payload**:
  ```json
  {
      "username": "testuser",
      "password": "password123"
  }
  ```
- **Response**:
  ```json
  {
      "access": "<access_token>",
      "refresh": "<refresh_token>"
  }
  ```
  - `access`: Token used to authenticate API requests.
  - `refresh`: Token used to obtain a new access token when it expires.

---

### 3. **Refresh JWT Token**
- **Endpoint**: `/api/token/refresh/`
- **Method**: `POST`
- **Description**: Refreshes the access token when it expires using the refresh token.
- **Request Payload**:
  ```json
  {
      "refresh": "<refresh_token>"
  }
  ```
- **Response**:
  ```json
  {
      "access": "<new_access_token>"
  }
  ```

---

## Using the JWT Token

### Include the Token in the `Authorization` Header
For all protected endpoints, include the JWT token in the `Authorization` header as follows:

```
Authorization: Bearer <access_token>
```

### Example: Create a New Product
- **Endpoint**: `/api/products/`
- **Method**: `POST`
- **Headers**:
  ```
  Authorization: Bearer <access_token>
  Content-Type: application/json
  ```
- **Request Payload**:
  ```json
  {
      "name": "Smartphone",
      "description": "A high-end smartphone",
      "price": 999.99,
      "category": "Electronics",
      "stock_quantity": 15,
      "image_url": "http://example.com/smartphone.jpg"
  }
  ```
- **Response**:
  ```json
  {
      "id": 1,
      "name": "Smartphone",
      "description": "A high-end smartphone",
      "price": 999.99,
      "category": "Electronics",
      "stock_quantity": 15,
      "image_url": "http://example.com/smartphone.jpg",
      "created_date": "2025-01-07T12:00:00Z"
  }
  ```

---

## Token Expiry and Refresh

- **Access Token**: Short-lived and must be included in every API request.
- **Refresh Token**: Long-lived and used to obtain a new access token without re-authenticating.

If the access token has expired, you will receive a `401 Unauthorized` response. Use the refresh token to generate a new access token by calling the `/api/token/refresh/` endpoint.

---

## Error Handling

### Invalid Credentials
- **Status Code**: `401 Unauthorized`
- **Response**:
  ```json
  {
      "detail": "No active account found with the given credentials"
  }
  ```

### Expired Token
- **Status Code**: `401 Unauthorized`
- **Response**:
  ```json
  {
      "detail": "Token is invalid or expired",
      "code": "token_not_valid"
  }
  ```

### Missing Token
- **Status Code**: `401 Unauthorized`
- **Response**:
  ```json
  {
      "detail": "Authentication credentials were not provided."
  }
  ```

---

## Configuration in `settings.py`

Make sure the following configuration is added in your `settings.py` to enable JWT authentication:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}
```

---

## Summary

- Use `/api/token/` to obtain a JWT token.
- Include the `Authorization: Bearer <access_token>` header for all protected endpoints.
- Use `/api/token/refresh/` to refresh expired access tokens.

This ensures secure API access while allowing authenticated users to manage products and perform other restricted operations.
