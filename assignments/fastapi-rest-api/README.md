# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build and test RESTful APIs using the FastAPI framework in Python. You will design endpoints, handle requests, and return JSON responses for a simple data model.

## 📝 Tasks

### 🛠️ Task 1: Set Up FastAPI Project

#### Description
Create a new Python project and install FastAPI. Set up a basic FastAPI application with a single endpoint that returns a welcome message.

#### Requirements
Completed program should:
- Include a main FastAPI app file (e.g., `main.py`)
- Define a root endpoint (`/`) that returns `{"message": "Welcome to FastAPI!"}`
- Run the server locally

### 🛠️ Task 2: Create CRUD Endpoints

#### Description
Design RESTful endpoints for a simple resource (e.g., `items`). Implement Create, Read, Update, and Delete operations using FastAPI routes.

#### Requirements
Completed program should:
- Define an `Item` data model (e.g., with `id`, `name`, `price`)
- Implement endpoints for:
  - Creating a new item (`POST /items`)
  - Listing all items (`GET /items`)
  - Retrieving a single item by ID (`GET /items/{id}`)
  - Updating an item (`PUT /items/{id}`)
  - Deleting an item (`DELETE /items/{id}`)
- Return appropriate JSON responses
- Example input/output:
  ```json
  // POST /items
  {"name": "Book", "price": 12.99}
  // Response
  {"id": 1, "name": "Book", "price": 12.99}
  ```

### 🛠️ Task 3: Test Your API

#### Description
Write simple test cases using Python's `requests` library or FastAPI's built-in test client to verify your endpoints work as expected.

#### Requirements
Completed program should:
- Include a test file (e.g., `test_main.py`)
- Test creating, reading, updating, and deleting items
- Print results of each test case
