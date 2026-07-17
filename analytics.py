import sqlite3

DATABASE_NAME = "inventory.db"


def get_analytics():

    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    # Total Products
    cursor.execute("SELECT COUNT(*) AS total_products FROM products")
    total_products = cursor.fetchone()["total_products"]

    # Total Quantity
    cursor.execute("SELECT SUM(quantity) AS total_quantity FROM products")
    total_quantity = cursor.fetchone()["total_quantity"] or 0

    # Inventory Value
    cursor.execute("""
        SELECT SUM(quantity * purchase_price) AS inventory_value
        FROM products
    """)
    inventory_value = cursor.fetchone()["inventory_value"] or 0

    # Low Stock Products
    cursor.execute("""
        SELECT COUNT(*) AS low_stock_products
        FROM products
        WHERE quantity <= reorder_level
    """)
    low_stock_products = cursor.fetchone()["low_stock_products"]

    connection.close()

    return {
        "total_products": total_products,
        "total_quantity": total_quantity,
        "inventory_value": inventory_value,
        "low_stock_products": low_stock_products
    }