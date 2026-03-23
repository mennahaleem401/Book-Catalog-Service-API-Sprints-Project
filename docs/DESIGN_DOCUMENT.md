# 📄 DESIGN_DOCUMENT.md

# Book Management API – Design Document

## 1. Overview

The Book Management API is a RESTful service that allows users to manage a collection of books.  
The system provides endpoints to create, retrieve, update, and delete books.

This document explains the architecture, system components, API endpoints, and design decisions used in the project.

---

# 2. System Architecture

The system follows a **Layered Architecture** to separate concerns and improve maintainability.

Layers:

Client Layer  
API Controller Layer  
Service Layer  
Repository Layer  
Database Layer

### Architecture Flow

Client → Controller → Service → Repository → Database

Each layer has a specific responsibility.

---

# 3. Component Responsibilities

## 3.1 Client

The client can be:

- Web application
- Mobile application
- API testing tool (Postman)

The client sends HTTP requests to the API.

Example request:

POST /books

---

## 3.2 API Controller

The controller handles incoming HTTP requests.

Responsibilities:

- Receive requests
- Validate input data
- Call the appropriate service
- Return HTTP responses

Example function:

```

createBook(bookData)

```

---

## 3.3 Service Layer

The service layer contains the **business logic** of the application.

Responsibilities:

- Process application rules
- Handle validations
- Coordinate operations between controller and repository

Example:

```

addBook(book)

```

---

## 3.4 Repository Layer

The repository is responsible for **data access**.

Responsibilities:

- Communicate with the database
- Execute queries
- Store and retrieve data

Example:

```

save(book)

````

---

## 3.5 Database

The database stores book records.

Example table:

| id | title | author | isbn |
|----|------|------|------|
| 1 | Clean Code | Robert Martin | 9780132350884 |

---

# 4. Sequence Diagram – Add Book

This sequence describes the process when a user adds a new book.

### Flow

1. Client sends POST request to API.
2. Controller receives request.
3. Controller calls BookService.
4. BookService validates the data.
5. BookService calls BookRepository.
6. Repository stores the book in the database.
7. Database returns confirmation.
8. Response is returned to the client.

### Interaction

Client → Controller: POST /books  
Controller → Service: addBook(book)  
Service → Repository: save(book)  
Repository → Database: insert record  
Database → Repository: success  
Repository → Service: bookSaved  
Service → Controller: successResponse  
Controller → Client: 201 Created

---

# 5. API Endpoints

## 5.1 Create Book

POST /books

Adds a new book to the system.

### Request

```json
{
"title": "Clean Code",
"author": "Robert Martin",
"isbn": "9780132350884"
}
````

### Response

```json
{
"message": "Book created successfully",
"status": 201
}
```

---

## 5.2 Get All Books

GET /books

Returns a list of all books.

### Response

```json
[
{
"id": 1,
"title": "Clean Code",
"author": "Robert Martin",
"isbn": "9780132350884"
}
]
```

---

## 5.3 Get Book By ID

GET /books/{id}

Returns a single book.

### Response

```json
{
"id": 1,
"title": "Clean Code",
"author": "Robert Martin",
"isbn": "9780132350884"
}
```

---

## 5.4 Update Book

PUT /books/{id}

Updates book information.

### Request

```json
{
"title": "Clean Code Updated",
"author": "Robert Martin",
"isbn": "9780132350884"
}
```

### Response

```json
{
"message": "Book updated successfully"
}
```

---

## 5.5 Delete Book

DELETE /books/{id}

Deletes a book.

### Response

```json
{
"message": "Book deleted successfully"
}
```

---

# 6. Design Principles Applied

## Separation of Concerns

Each layer has a dedicated responsibility.

* Controllers handle HTTP requests.
* Services contain business logic.
* Repositories manage database operations.

This makes the system easier to maintain and test.

---

## Single Responsibility Principle (SRP)

Each class has one responsibility.

Example:

* Controller → request handling
* Service → business logic
* Repository → data access

---

## Scalability

The layered architecture allows the system to grow easily.

For example:

* Adding caching
* Adding authentication
* Connecting to different databases

---

# 7. Error Handling

Common error responses include:

400 – Bad Request
404 – Resource Not Found
500 – Internal Server Error

Example error response:

```json
{
"error": "Book not found"
}
```

---

# 8. Continuous Integration Support

The project includes a CI workflow that runs automatically on pull requests.

The workflow performs:

* Code linting
* Running unit tests
* Validating build

This ensures code quality and prevents broken code from being merged.

---

# 9. Future Improvements

Possible enhancements:

* Authentication and authorization
* Pagination for large datasets
* API documentation using Swagger
* Docker containerization
* Caching for improved performance

---

# 10. Conclusion

The Book Management API uses a clean layered architecture that improves modularity, maintainability, and scalability.
The separation between controllers, services, and repositories ensures clear responsibilities and supports future system growth.
