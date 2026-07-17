import sqlite3

# Database file name
DATABASE_NAME = "inventory.db"


def create_database():
    # Connect to SQLite database (creates it if it doesn't exist)
    connection = sqlite3.connect(DATABASE_NAME)

    # Create a cursor to execute SQL commands
    cursor = connection.cursor()

    # -------------------------------
    # Create Suppliers Table
    # -------------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS suppliers (
        supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
        supplier_name TEXT NOT NULL,
        contact_person TEXT,
        email TEXT,
        phone TEXT,
        address TEXT,
        created_at TEXT
    )
    """)

    # -------------------------------
    # Create Products Table
    # -------------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        supplier_id INTEGER,
        product_name TEXT NOT NULL,
        category TEXT,
        quantity INTEGER NOT NULL,
        purchase_price REAL,
        selling_price REAL,
        reorder_level INTEGER,
        created_at TEXT,
        updated_at TEXT,
        FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
    )
    """)

    # -------------------------------
    # Create Inventory Logs Table
    # -------------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory_logs (
        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        action TEXT,
        quantity_changed INTEGER,
        previous_quantity INTEGER,
        new_quantity INTEGER,
        remarks TEXT,
        timestamp TEXT,
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    )
    """)

    # Save changes
    connection.commit()

    # Close database connection
    connection.close()

    print("Database and tables created successfully!")


# Run this file directly
if __name__ == "__main__":
    create_database()

def get_connection():
    """
    Returns a connection to the SQLite database.
    """
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection

def get_all_products():
    """
    Returns all products.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    connection.close()

    return [dict(product) for product in products]

def get_product(product_id):
    """
    Returns one product by ID.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM products WHERE product_id = ?",
        (product_id,)
    )

    product = cursor.fetchone()

    connection.close()

    if product:
        return dict(product)

    return None

def add_product(
    supplier_id,
    product_name,
    category,
    quantity,
    purchase_price,
    selling_price,
    reorder_level
):
    """
    Adds a new product.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO products
        (
            supplier_id,
            product_name,
            category,
            quantity,
            purchase_price,
            selling_price,
            reorder_level,
            created_at,
            updated_at
        )

        VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'), datetime('now'))
    """,
    (
        supplier_id,
        product_name,
        category,
        quantity,
        purchase_price,
        selling_price,
        reorder_level
    ))

    connection.commit()

    product_id = cursor.lastrowid

    connection.close()

    return product_id

def update_product(
    product_id,
    supplier_id,
    product_name,
    category,
    quantity,
    purchase_price,
    selling_price,
    reorder_level
):
    """
    Updates an existing product.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE products

        SET
            supplier_id = ?,
            product_name = ?,
            category = ?,
            quantity = ?,
            purchase_price = ?,
            selling_price = ?,
            reorder_level = ?,
            updated_at = datetime('now')

        WHERE product_id = ?
    """,
    (
        supplier_id,
        product_name,
        category,
        quantity,
        purchase_price,
        selling_price,
        reorder_level,
        product_id
    ))

    connection.commit()

    updated = cursor.rowcount

    connection.close()

    return updated

def delete_product(product_id):
    """
    Deletes a product.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM products WHERE product_id = ?",
        (product_id,)
    )

    connection.commit()

    deleted = cursor.rowcount

    connection.close()

    return deleted
# =====================================================
# SUPPLIER FUNCTIONS
# =====================================================

def get_all_suppliers():
    """
    Returns all suppliers.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM suppliers")

    suppliers = cursor.fetchall()

    connection.close()

    return [dict(supplier) for supplier in suppliers]


def get_supplier(supplier_id):
    """
    Returns one supplier by ID.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM suppliers WHERE supplier_id = ?",
        (supplier_id,)
    )

    supplier = cursor.fetchone()

    connection.close()

    if supplier:
        return dict(supplier)

    return None


def add_supplier(
    supplier_name,
    contact_person,
    email,
    phone,
    address
):
    """
    Adds a new supplier.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO suppliers
        (
            supplier_name,
            contact_person,
            email,
            phone,
            address,
            created_at
        )

        VALUES
        (
            ?, ?, ?, ?, ?, datetime('now')
        )
    """,
    (
        supplier_name,
        contact_person,
        email,
        phone,
        address
    ))

    connection.commit()

    supplier_id = cursor.lastrowid

    connection.close()

    return supplier_id


def update_supplier(
    supplier_id,
    supplier_name,
    contact_person,
    email,
    phone,
    address
):
    """
    Updates an existing supplier.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE suppliers

        SET
            supplier_name = ?,
            contact_person = ?,
            email = ?,
            phone = ?,
            address = ?

        WHERE supplier_id = ?
    """,
    (
        supplier_name,
        contact_person,
        email,
        phone,
        address,
        supplier_id
    ))

    connection.commit()

    updated = cursor.rowcount

    connection.close()

    return updated


def delete_supplier(supplier_id):
    """
    Deletes a supplier.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM suppliers WHERE supplier_id = ?",
        (supplier_id,)
    )

    connection.commit()

    deleted = cursor.rowcount

    connection.close()

    return deleted
# =====================================================
# INVENTORY LOG FUNCTIONS
# =====================================================

def add_inventory_log(
    product_id,
    action,
    quantity_changed,
    previous_quantity,
    new_quantity,
    remarks
):
    """
    Adds a new inventory log.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO inventory_logs
        (
            product_id,
            action,
            quantity_changed,
            previous_quantity,
            new_quantity,
            remarks,
            timestamp
        )

        VALUES
        (
            ?, ?, ?, ?, ?, ?, datetime('now')
        )
    """,
    (
        product_id,
        action,
        quantity_changed,
        previous_quantity,
        new_quantity,
        remarks
    ))

    connection.commit()

    connection.close()

# =====================================================
# VIEW INVENTORY LOGS
# =====================================================

def get_all_inventory_logs():
    """
    Returns all inventory logs.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM inventory_logs
        ORDER BY timestamp DESC
    """)

    logs = cursor.fetchall()

    connection.close()

    return [dict(log) for log in logs]
