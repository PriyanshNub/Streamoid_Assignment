````markdown
# FastAPI Product API

A FastAPI application for managing products with features like CSV upload, listing, and searching. Built to run with Docker and PostgreSQL.

---

## Features

- Upload products from CSV (`/upload`)
- List products with pagination (`/products`)
- Search products by brand, color, and price range (`/products/search`)
- API documentation via Swagger UI and ReDoc

---

## Requirements

- [Docker](https://www.docker.com/get-started) & [Docker Compose](https://docs.docker.com/compose/install/)
- Git

---

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/PriyanshNub/Streamoid_Assignment.git
cd Streamoid_Assignment
````

2. **Build Docker images**

```bash
docker-compose build --no-cache
```

3. **Start the application**

```bash
docker-compose up
```

The command will start two containers:

* **Web API**: FastAPI application
* **Database**: PostgreSQL

---

## Accessing the API

* **Swagger UI (interactive docs):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc (alternative docs):** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
* **Health check:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## API Endpoints

### 1. POST `/upload`

Upload a CSV file containing products.

* **Request body:** `multipart/form-data`

  * `file` → CSV file (e.g., `sample.csv`)

* **Response:** JSON object with:

  * `stored`: number of successfully stored rows
  * `failed`: rows that failed insertion

---

### 2. GET `/products`

List all products with pagination.

* **Query parameters:**

  * `page` (integer, default=1)
  * `limit` (integer, default=10)

* **Response:**

```json
{
  "total": 3,
  "page": 1,
  "limit": 10,
  "products": [
    {
      "sku": "101",
      "name": "Running Shoes",
      "brand": "Nike",
      "color": "Black",
      "size": "9",
      "mrp": 6000,
      "price": 5499,
      "quantity": 20
    }
  ]
}
```

---

### 3. GET `/products/search`

Search products by filters.

* **Query parameters (optional):**

  * `brand` → string
  * `color` → string
  * `minPrice` → number
  * `maxPrice` → number

* **Response:** JSON array of matching products.

---

## Example CSV Format

| SKU | Name          | Brand | Color | Size     | MRP  | Price | Quantity |
| --- | ------------- | ----- | ----- | -------- | ---- | ----- | -------- |
| 101 | Running Shoes | Nike  | Black | 9        | 6000 | 5499  | 20       |
| 102 | T-Shirt       | Puma  | Blue  | L        | 1999 | 1499  | 50       |
| 103 | Smart Watch   | Boat  | Black | One Size | 4999 | 3999  | 15       |

---

## Notes

* Make sure Docker is running before building or starting containers.
* Swagger UI (`/docs`) provides an interactive way to test all endpoints.
* CSV must match the column structure above to avoid insertion errors.
* Database and application logs are visible in the terminal when using `docker-compose up`.

---

