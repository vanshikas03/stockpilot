# StockPilot – Smart Inventory Management & Business Analytics System

StockPilot is a modern inventory management system designed to help businesses organize, monitor, and analyze their inventory with ease. Instead of relying on spreadsheets or manual stock tracking, StockPilot provides a centralized platform to manage products, suppliers, inventory movements, and business insights in one place.

Built using **React**, **Flask**, **SQLite**, and **Pandas**, the application combines a responsive web interface with powerful backend analytics to simplify inventory operations and support better business decisions.

Whether it's tracking stock levels, managing suppliers, identifying low-stock products, or analyzing inventory value, StockPilot transforms raw inventory data into meaningful insights.

---

# Why StockPilot?

Managing inventory efficiently is one of the biggest challenges for businesses. Poor inventory management often leads to:

- Overstocking products
- Running out of important inventory
- Difficulty tracking suppliers
- Manual record keeping
- Limited visibility into inventory performance

StockPilot addresses these challenges by providing an intuitive inventory management platform with built-in analytics, allowing businesses to monitor stock levels and make informed purchasing decisions.

---

# Key Features

## Product Management

Manage inventory with complete CRUD functionality.

- Add new products
- View inventory
- Update product information
- Delete products
- Track product quantity
- Configure reorder levels
- Store purchase and selling prices

---

## Supplier Management

Maintain supplier information in one place.

- Add suppliers
- View supplier details
- Update supplier information
- Delete supplier records

---

## Inventory Analytics

StockPilot uses **Pandas** to generate meaningful inventory insights rather than relying solely on database queries.

Analytics include:

- Total Products
- Total Inventory Value
- Products by Category
- Low Stock Products
- Most Valuable Products
- Restock Recommendations

These insights help businesses understand their inventory performance and make smarter stocking decisions.

---

## Inventory Logs

Every inventory operation is automatically recorded.

Whenever a product is:

- Created
- Updated
- Deleted

StockPilot stores:

- Product ID
- Action Performed
- Previous Quantity
- New Quantity
- Quantity Changed
- Timestamp
- Remarks

This creates a complete audit trail of inventory activities.

---

# Technology Stack

## Frontend

- React.js
- Tailwind CSS
- Axios
- React Router

## Backend

- Flask
- Python

## Database

- SQLite

## Data Analytics

- Pandas

## Version Control

- Git
- GitHub

---

# Project Architecture

```text
                React Frontend
                       │
                       │ REST APIs
                       ▼
                Flask Backend
          ┌────────────┼────────────┐
          │            │            │
      Validation   SQLite DB    Pandas
          │            │            │
          └────────────┼────────────┘
                       │
               Business Insights
```

---

# Project Structure

```text
StockPilot/

├── backend/
│   ├── App.py
│   ├── database.py
│   ├── analytics.py
│   ├── requirements.txt
│   ├── inventory.db
│   └── .env
│
├── frontend/
│   ├── src/
│   │
│   ├── pages/
│   │     Dashboard.js
│   │     Products.js
│   │     Suppliers.js
│   │     Analytics.js
│   │     InventoryLogs.js
│   │
│   ├── services/
│   │     Api.js
│   │
│   └── App.js
│
└── README.md
```

---

# Database Design

The application consists of three core modules.

## Products

Stores inventory information including:

- Product Name
- Category
- Supplier
- Quantity
- Purchase Price
- Selling Price
- Reorder Level
- Created Date

---

## Suppliers

Stores supplier information including:

- Supplier Name
- Contact Details
- Email Address

---

## Inventory Logs

Maintains a complete history of inventory operations.

Relationship Diagram

```text
Supplier
    │
    └────────► Products
                     │
                     └────────► Inventory Logs
```

---

# REST API Endpoints

## Products

| Method | Endpoint |
|---------|----------|
| GET | /products |
| GET | /products/{id} |
| POST | /products |
| PUT | /products/{id} |
| DELETE | /products/{id} |

## Suppliers

| Method | Endpoint |
|---------|----------|
| GET | /suppliers |
| GET | /suppliers/{id} |
| POST | /suppliers |
| PUT | /suppliers/{id} |
| DELETE | /suppliers/{id} |

## Analytics

| Method | Endpoint |
|---------|----------|
| GET | /analytics |

## Inventory Logs

| Method | Endpoint |
|---------|----------|
| GET | /inventory-logs |

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/yourusername/StockPilot.git

cd StockPilot
```

## Backend Setup

```bash
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python App.py
```

Backend runs at:

```
http://127.0.0.1:8000
```

## Frontend Setup

```bash
cd frontend

npm install

npm start
```

Frontend runs at:

```
http://localhost:3000
```

---

# Screenshots

- Dashboard
- Products
- Suppliers
- Analytics
- Inventory Logs

(Add screenshots here after capturing your application.)

---

# Future Enhancements

StockPilot has been designed with scalability in mind. Future improvements may include:

- User Authentication
- Role-Based Access Control
- Barcode Scanner Integration
- Product Image Upload
- Search & Filtering
- Export Reports to Excel and PDF
- Interactive Charts
- Email Notifications for Low Stock
- MySQL Support
- Cloud Deployment

---

# Project Highlights

- Full Stack Web Application
- RESTful API Architecture
- Responsive React Interface
- Inventory Analytics with Pandas
- Automatic Inventory Logging
- Clean Modular Architecture
- Business-Oriented Dashboard
- Scalable Design

---

# Author

**Vanshika**

Capstone Project

Full Stack Python Development

---

# License

This project was developed for educational purposes as part of a Full Stack Python Development Capstone Project.