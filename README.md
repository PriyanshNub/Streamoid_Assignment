

````markdown
# FastAPI Product API

A simple FastAPI application for managing products. Allows uploading products via CSV, listing products, and searching with filters.

---

## Features

- Upload products via CSV (`/upload`)
- List products with pagination (`/products`)
- Search products by brand, color, and price range (`/products/search`)
- Swagger UI and ReDoc documentation available

---

## Requirements

- Docker & Docker Compose
- PostgreSQL (Docker container included)

---

## Running the Application

1. Build and start the app using Docker Compose:

```bash
docker-compose build --no-cache
docker-compose up
````

2. Open the API in your browser:

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Endpoints

### POST `/upload`

Upload products via CSV file.

* **Request body:** `multipart/form-data`

  * `file` (CSV file)

* **Response:** JSON with stored and failed rows

---

### GET `/products`

List all products with pagination.

* **Query parameters:**

  * `page` (integer, default=1)
  * `limit` (integer, default=10)

* **Response:** JSON list of products with `total`, `page`, and `limit`.

---

### GET `/products/search`

Search products by filters.

* **Query parameters:**

  * `brand` (optional)
  * `color` (optional)
  * `minPrice` (optional)
  * `maxPrice` (optional)

* **Response:** JSON list of matching products

---

### GET `/`

Root endpoint for health check:

* **Response:** `{ "msg": "FastAPI Product API - alive" }`

---


