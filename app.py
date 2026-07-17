from flask import Flask, request, jsonify, render_template

from Db import (
    create_database,

    # Product Functions
    get_all_products,
    get_product,
    add_product,
    update_product,
    delete_product,

    # Supplier Functions
    get_all_suppliers,
    get_supplier,
    add_supplier,
    update_supplier,
    delete_supplier,

    # Inventory Logs
    add_inventory_log,
    get_all_inventory_logs


    
)
from analytics import get_analytics

app = Flask(__name__)

# Create database and tables
create_database()


# ======================================================
# DASHBOARD (HOME PAGE)
# ======================================================
@app.route("/")
def home():

    products = get_all_products()

    total_products = len(products)

    total_quantity = sum(
        product["quantity"] for product in products
    )

    low_stock = sum(
        1
        for product in products
        if product["quantity"] <= product["reorder_level"]
    )

    return render_template(
        "dashboard.html",
        total_products=total_products,
        total_quantity=total_quantity,
        low_stock=low_stock
    )


# ======================================================
# GET ALL PRODUCTS
# ======================================================
@app.route("/products", methods=["GET"])
def fetch_products():

    products = get_all_products()

    return jsonify(products), 200


# ======================================================
# GET PRODUCT BY ID
# ======================================================
@app.route("/products/<int:product_id>", methods=["GET"])
def fetch_product(product_id):

    product = get_product(product_id)

    if product:
        return jsonify(product), 200

    return jsonify({
        "error": "Product not found"
    }), 404


# ======================================================
# ADD PRODUCT
# ======================================================
@app.route("/products", methods=["POST"])
def create_product():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body cannot be empty."
        }), 400

    required_fields = [
        "supplier_id",
        "product_name",
        "category",
        "quantity",
        "purchase_price",
        "selling_price",
        "reorder_level"
    ]

    for field in required_fields:

        if field not in data:

            return jsonify({
                "error": f"{field} is required."
            }), 400

    product_id = add_product(
        data["supplier_id"],
        data["product_name"],
        data["category"],
        data["quantity"],
        data["purchase_price"],
        data["selling_price"],
        data["reorder_level"]
    )
    
    add_inventory_log(
    product_id=product_id,
    action="CREATE",
    quantity_changed=data["quantity"],
    previous_quantity=0,
    new_quantity=data["quantity"],
    remarks="Product added"
    )

    return jsonify({
        "message": "Product added successfully!",
        "product_id": product_id
    }), 201


# ======================================================
# UPDATE PRODUCT
# ======================================================
@app.route("/products/<int:product_id>", methods=["PUT"])
def edit_product(product_id):

    product = get_product(product_id)
    previous_quantity = product["quantity"]

    if not product:
        return jsonify({
            "error": "Product not found"
        }), 404

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body cannot be empty."
        }), 400

    required_fields = [
        "supplier_id",
        "product_name",
        "category",
        "quantity",
        "purchase_price",
        "selling_price",
        "reorder_level"
    ]

    for field in required_fields:

        if field not in data:

            return jsonify({
                "error": f"{field} is required."
            }), 400
        
    previous_quantity = product["quantity"]

    update_product(
        product_id,
        data["supplier_id"],
        data["product_name"],
        data["category"],
        data["quantity"],
        data["purchase_price"],
        data["selling_price"],
        data["reorder_level"]
    )

    add_inventory_log(
        product_id=product_id,
        action="UPDATE",
        quantity_changed=data["quantity"] - previous_quantity,
        previous_quantity=previous_quantity,
        new_quantity=data["quantity"],
        remarks="Product updated"
    )


    return jsonify({
        "message": "Product updated successfully!"
    }), 200


# ======================================================
# DELETE PRODUCT
# ======================================================
@app.route("/products/<int:product_id>", methods=["DELETE"])
def remove_product(product_id):
    
    product = get_product(product_id)
    previous_quantity = product["quantity"]

    if not product:
        return jsonify({
            "error": "Product not found"
        }), 404
    

    delete_product(product_id)

    add_inventory_log(
        product_id=product_id,
        action="DELETE",
        quantity_changed=-previous_quantity,
        previous_quantity=previous_quantity,
        new_quantity=0,
        remarks="Product deleted"
    )

    return jsonify({
        "message": "Product deleted successfully!"
    }), 200


# ======================================================
# PRODUCTS PAGE (Coming Next)
# ======================================================
@app.route("/products-page")
def products_page():
    return "<h2>Products Page - Coming Soon</h2>"


# ======================================================
# SUPPLIERS PAGE (Coming Next)
# ======================================================
@app.route("/suppliers-page")
def suppliers_page():
    return "<h2>Suppliers Page - Coming Soon</h2>"

# ======================================================
# GET ALL SUPPLIERS
# ======================================================
@app.route("/suppliers", methods=["GET"])
def fetch_suppliers():

    suppliers = get_all_suppliers()

    return jsonify(suppliers), 200


# ======================================================
# GET SUPPLIER BY ID
# ======================================================
@app.route("/suppliers/<int:supplier_id>", methods=["GET"])
def fetch_supplier(supplier_id):

    supplier = get_supplier(supplier_id)

    if supplier:
        return jsonify(supplier), 200

    return jsonify({
        "error": "Supplier not found"
    }), 404


# ======================================================
# ADD SUPPLIER
# ======================================================
@app.route("/suppliers", methods=["POST"])
def create_supplier():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body cannot be empty."
        }), 400

    required_fields = [
        "supplier_name",
        "contact_person",
        "email",
        "phone",
        "address"
    ]

    for field in required_fields:

        if field not in data:

            return jsonify({
                "error": f"{field} is required."
            }), 400

    supplier_id = add_supplier(
        data["supplier_name"],
        data["contact_person"],
        data["email"],
        data["phone"],
        data["address"]
    )

    return jsonify({
        "message": "Supplier added successfully!",
        "supplier_id": supplier_id
    }), 201


# ======================================================
# UPDATE SUPPLIER
# ======================================================
@app.route("/suppliers/<int:supplier_id>", methods=["PUT"])
def edit_supplier(supplier_id):

    supplier = get_supplier(supplier_id)

    if not supplier:
        return jsonify({
            "error": "Supplier not found"
        }), 404

    data = request.get_json()

    update_supplier(
        supplier_id,
        data["supplier_name"],
        data["contact_person"],
        data["email"],
        data["phone"],
        data["address"]
    )

    return jsonify({
        "message": "Supplier updated successfully!"
    }), 200


# ======================================================
# DELETE SUPPLIER
# ======================================================
@app.route("/suppliers/<int:supplier_id>", methods=["DELETE"])
def remove_supplier(supplier_id):

    supplier = get_supplier(supplier_id)

    if not supplier:
        return jsonify({
            "error": "Supplier not found"
        }), 404

    delete_supplier(supplier_id)

    return jsonify({
        "message": "Supplier deleted successfully!"
    }), 200

# ======================================================
# GET ALL INVENTORY LOGS
# ======================================================
@app.route("/inventory-logs", methods=["GET"])
def fetch_inventory_logs():

    logs = get_all_inventory_logs()

    return jsonify(logs), 200

# ======================================================
# ANALYTICS PAGE (Coming Next)
# ======================================================
@app.route("/analytics-page")
def analytics_page():
    return "<h2>Analytics Page - Coming Soon</h2>"
# ======================================================
# ANALYTICS API
# ======================================================
@app.route("/analytics", methods=["GET"])
def analytics():

    data = get_analytics()

    return jsonify(data), 200

# ======================================================
# RUN APPLICATION
# ======================================================
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
