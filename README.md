# Django CRUD Operations 🚀

A simple yet powerful Django REST API project demonstrating full CRUD (Create, Read, Update, Delete) operations for user management. This is my first Django project showcasing fundamental web development concepts and RESTful API design.

## 📋 Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Usage Examples](#usage-examples)
- [Code Overview](#code-overview)
- [Learning Outcomes](#learning-outcomes)
- [Contributing](#contributing)
- [Author](#author)

## ✨ Features

- **Complete CRUD Operations**: Create, Read, Update, and Delete users
- **RESTful API Design**: Clean and intuitive API endpoints
- **Django REST Framework**: Powerful toolkit for building Web APIs
- **Data Serialization**: Proper JSON serialization for API responses
- **Error Handling**: Comprehensive error handling with appropriate HTTP status codes
- **Database Integration**: Seamless integration with Django ORM

## 🛠 Technologies Used

- **Python 3.12.2**
- **Django** - High-level Python web framework
- **Django REST Framework** - Powerful toolkit for building Web APIs
- **SQLite** - Default database (can be configured for other databases)

## 📁 Project Structure

```
django-crud-project/
│
├── manage.py
├── README.md
│
├── CRUD/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
|   └── views.py
|   └── view_generics.py
|   └── views_APIView.py
│
└── api/
    ├── __init__.py
    ├── models.py
    ├── serializer.py
    ├── views.py
    ├── urls.py
    └── migrations/
```

## 🚀 Installation

### Prerequisites
- Python 3.12.2 installed on your system
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Prince200510/Django_CRUD_Operation.git
   cd Django_CRUD_Operation
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django djangorestframework
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## 🔗 API Endpoints

The API provides the same functionality through different implementation approaches:

### Function-Based Views
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/users/` | Retrieve all users |
| `POST` | `/api/users/` | Create a new user |
| `GET` | `/api/users/{id}/` | Retrieve a specific user |
| `PUT` | `/api/users/{id}/` | Update a specific user |
| `DELETE` | `/api/users/{id}/` | Delete a specific user |

### Class-Based Views (APIView)
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/users/` | Retrieve all users using APIView |
| `GET` | `/api/users/{id}/` | Retrieve a specific user |
| `PUT` | `/api/users/{id}/` | Update a specific user |
| `DELETE` | `/api/users/{id}/` | Delete a specific user |

### Generic Views
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/users/` | List all users |
| `POST` | `/api/users/` | Create a new user |
| `GET` | `/api/users/{id}/` | Retrieve a specific user |
| `PUT` | `/api/users/{id}/` | Update a specific user |
| `DELETE` | `/api/users/{id}/` | Delete a specific user |

## 💡 Usage Examples

### Get All Users
```bash
curl -X GET http://127.0.0.1:8000/api/users/
```

### Create a New User
```bash
curl -X POST http://127.0.0.1:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "age": 25}'
```

### Get User by ID
```bash
curl -X GET http://127.0.0.1:8000/api/users/1/
```

### Update User
```bash
curl -X PUT http://127.0.0.1:8000/api/users/1/ \
  -H "Content-Type: application/json" \
  -d '{"name": "John Smith", "age": 26}'
```

### Delete User
```bash
curl -X DELETE http://127.0.0.1:8000/api/users/1/
```

## 🔧 Code Overview

This project demonstrates multiple approaches to building Django REST APIs, showcasing different levels of abstraction and customization:

### 1. Function-Based Views (FBV) with `@api_view`
- **`get_user()`**: Retrieves all users from the database
- **`create_user()`**: Creates a new user with POST data
- **`user_details()`**: Handles GET, PUT, and DELETE operations for individual users

### 2. Class-Based Views (CBV) with `APIView`
- **`UserAPIView`**: Handles listing all users with custom logic
- **`UserOperation`**: Manages individual user operations (GET, PUT, DELETE) with proper error handling using `get_object_or_404`

### 3. Generic Views with Built-in CRUD Operations
- **`UserGenerics`**: Extends `ListCreateAPIView` for listing and creating users
- **`UserDetails`**: Extends `RetrieveUpdateDestroyAPIView` for individual user operations

### Key Features of the Implementation:
- **Multiple API Approaches**: Demonstrates function-based views, class-based views, and generic views
- **DRY Principle**: Generic views reduce code duplication significantly
- **Error Handling**: Comprehensive error handling with try-catch blocks and `get_object_or_404`
- **HTTP Status Codes**: Returns appropriate status codes (200, 201, 400, 404, 204)
- **Django ORM Integration**: Seamless database operations with Django's ORM
- **Data Validation**: Implements validation through serializers
- **Code Reusability**: Demonstrates different levels of abstraction for various use cases

### Sample Response Format:
```json
{
  "id": 1,
  "name": "Prince Maurya",
  "age": 19
}
```

## 📚 Learning Outcomes

Through this project, I gained hands-on experience with:

- **Django Framework**: Understanding MVC architecture and Django's MVT pattern
- **REST API Development**: Creating RESTful endpoints following best practices
- **Multiple API Approaches**: Function-based views, Class-based views, and Generic views
- **DRF Generic Views**: Leveraging built-in generic views for rapid development
- **Class-Based Views**: Object-oriented approach to API development
- **Database Operations**: Using Django ORM for CRUD operations
- **Serialization**: Converting Python objects to JSON and vice versa
- **HTTP Methods**: Implementing GET, POST, PUT, and DELETE operations
- **Error Handling**: Managing exceptions with `get_object_or_404` and try-catch blocks
- **Code Organization**: Different patterns for organizing API logic
- **API Testing**: Testing endpoints using various tools and methods

## 🚦 Getting Started with Django

If you're new to Django, here are the basic commands used in this project:

```bash
# Create a new Django project
django-admin startproject <project-name>

# Navigate to project directory
cd <project-name>

# Create a new Django app
python manage.py startapp <app-name>

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Run development server
python manage.py runserver
```

## 🤝 Contributing

This being my first Django project, I welcome suggestions and improvements! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some improvement'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 🐛 Issues

If you find any bugs or have suggestions for improvements, please open an issue on GitHub.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Prince Maurya** ([@Prince200510](https://github.com/Prince200510))

- 🔗 GitHub: [Prince200510](https://github.com/Prince200510)
- 📧 Feel free to reach out for any questions or collaborations!

---

## 🌟 Acknowledgments

- Django Documentation for excellent learning resources
- Django REST Framework for making API development seamless
- The Django community for continuous support and resources

---

*This project represents my first step into Django development and web APIs. I'm excited to continue learning and building more complex applications!*

## 📈 Next Steps

- Add user authentication and authorization
- Implement pagination for large datasets
- Add input validation and custom error messages
- Deploy the application to a cloud platform
- Add comprehensive testing suite
- Implement logging and monitoring
