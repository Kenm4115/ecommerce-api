
# E-commerce Product API

This project is an E-commerce Product API built using **Django** and **Django REST Framework (DRF)**. The API supports product management (CRUD), user management, authentication, search functionality, and advanced filtering options.

## Features

1. **Product Management**
   - Create, Read, Update, and Delete (CRUD) products.
   - Product attributes include Name, Description, Price, Category, Stock Quantity, Image URL, and Created Date.

2. **User Management**
   - User registration, login, and authentication using **JWT**.
   - Only authenticated users can manage products.

3. **Search and Filters**
   - Search products by Name or Category.
   - Filter products by Category, Price Range, and Stock Availability.

4. **Pagination**
   - Paginated responses for product listings.

5. **Authentication**
   - Secure API access using **JWT Authentication**.

---

## Requirements

- Python 3.8+
- Django 4.0+
- Django REST Framework 3.13+
- django-filter

---

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/ecommerce-api.git
   cd ecommerce-api
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

### User Management

- **Register a new user**:
  ```
  POST /api/register/
  ```
  Payload:
  ```json
  {
      "username": "testuser",
      "email": "testuser@example.com",
      "password": "password123"
  }
  ```

- **Obtain a JWT token**:
  ```
  POST /api/token/
  ```
  Payload:
  ```json
  {
      "username": "testuser",
      "password": "password123"
  }
  ```

- **Refresh a JWT token**:
  ```
  POST /api/token/refresh/
  ```

---

### Product Management

- **List all products**:
  ```
  GET /api/products/
  ```

- **Retrieve a single product by ID**:
  ```
  GET /api/products/<product_id>/
  ```

- **Create a new product** (Authenticated):
  ```
  POST /api/products/
  ```
  Payload:
  ```json
  {
      "name": "Laptop",
      "description": "A high-performance laptop",
      "price": 1200.99,
      "category": "Electronics",
      "stock_quantity": 10,
      "image_url": "http://example.com/laptop.jpg"
  }
  ```

- **Update a product** (Authenticated):
  ```
  PUT /api/products/<product_id>/
  ```

- **Delete a product** (Authenticated):
  ```
  DELETE /api/products/<product_id>/
  ```

---

### Filtering and Searching

- **Search products by name or category**:
  ```
  GET /api/products/?search=<keyword>
  ```

- **Filter products by category**:
  ```
  GET /api/products/?category=Electronics
  ```

- **Filter products by price range**:
  ```
  GET /api/products/?min_price=100&max_price=500
  ```

- **Filter products by stock availability**:
  ```
  GET /api/products/?in_stock=true
  ```

---

## Configuration

### Pagination

Pagination is enabled by default with a page size of 10. You can adjust this in `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```

### Authentication

JWT authentication is used. Ensure you include the JWT token in the `Authorization` header for authenticated requests:

```
Authorization: Bearer <your_token>
```

---

## Running Tests

To run the test suite, use the following command:
```bash
python manage.py test
```

---

## Deployment

To deploy the API to production, follow these steps:

1. Set `DEBUG = False` in `settings.py`.
2. Configure the `ALLOWED_HOSTS` for your domain or IP.
3. Use a production server like **Gunicorn** with a web server like **Nginx**.
4. Configure a PostgreSQL database for production.
5. Deploy the project on a hosting platform like **Heroku**, **AWS**, or **PythonAnywhere**.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
