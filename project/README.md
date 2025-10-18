Absolutely! Here’s a professional and clean **`README.md`** template for your FastAPI Product API project:

````markdown
# FastAPI Product API

**Version:** 0.1.0  

This is a FastAPI application to manage products. It supports uploading products via CSV, listing, and searching products with filters.

---

## **Features**

- Upload products from a CSV file (`/upload`)
- List all products with pagination (`/products`)
- Search products by brand, color, and price range (`/products/search`)
- Root endpoint to check API health (`/`)

---

## **Installation**

1. Clone the repository:

```bash
git clone https://github.com/your-username/fastapi-product-api.git
cd fastapi-product-api
````

2. Create a virtual environment and activate it:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up PostgreSQL (via Docker recommended):

```bash
docker-compose up -d
```

---

## **Running the API**

```bash
uvicorn main:app --reload
```

* API will run at [http://127.0.0.1:8000](http://127.0.0.1:8000)
* No Swagger docs are available since `docs_url=None` and `redoc_url=None`.

---

## **Endpoints**

| Method | Endpoint           | Description                                                 |
| ------ | ------------------ | ----------------------------------------------------------- |
| `GET`  | `/`                | API health check                                            |
| `POST` | `/upload`          | Upload products CSV file                                    |
| `GET`  | `/products`        | List products with pagination (`page`, `limit`)             |
| `GET`  | `/products/search` | Search products by `brand`, `color`, `minPrice`, `maxPrice` |

---

## **Sample CSV Format**

```csv
SKU,Name,Brand,Color,Size,MRP,Price,Quantity
101,Running Shoes,Nike,Black,9,6000,5499,20
102,T-Shirt,Puma,Blue,L,1999,1499,50
103,Smart Watch,Boat,Black,One Size,4999,3999,15
```

---

## **Docker**

You can use Docker to run both the app and database:

```bash
docker-compose up --build
```

---

## **Author**

Priyansh Sharaf

---


