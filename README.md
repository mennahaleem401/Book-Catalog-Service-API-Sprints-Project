# 📚 Book Catalog Service API

A simple RESTful API for managing books.
This project demonstrates a **Walking Skeleton implementation** including API endpoints, project structure, automated tests, and CI integration.

---

# 🚀 Features

* Add new books
* Retrieve all books
* Simple layered architecture
* Automated unit tests
* Continuous Integration workflow

---

# 🏗 Project Structure

```
book-catalog-service
│
├── app
│   ├── main.py
│   ├── models.py
│   ├── services.py
│   └── repository.py
│
├── tests
│   └── test_books.py
│
├── docs
│   └── DESIGN_DOCUMENT.md
│
├── .github/workflows
│   └── ci.yml
│
├── requirements.txt
└── README.md
```

---

# ▶️ Running the API

Install dependencies:

```
pip install -r requirements.txt
```

Run the server:

```
uvicorn app.main:app --reload
```

The API will be available at:

```
http://localhost:8000
```

---

# 📡 API Endpoints

### Get All Books

```
GET /books
```

### Add Book

```
POST /books
```

Example request:

```
{
  "title": "Clean Code",
  "author": "Robert Martin",
  "isbn": "123456"
}
```

---

# 🧪 Running Tests

```
pytest
```

---

# 🔄 Continuous Integration

A GitHub Actions workflow runs automatically on each push or pull request to:

* Install dependencies
* Run unit tests
* Ensure code quality
