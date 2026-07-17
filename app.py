from flask import Flask, request, jsonify

from db import (
    create_database,
    get_all_products,
    get_product,
    add_product,
    update_product,
    delete_product
)

app = Flask(__name__)

# Create database and tables
create_database()


# ==========================================
# HOME ROUTE
# ==========================================
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to StockPilot Inventory API!"
    })


# ==========================================
# GET ALL PRODUCTS
# ==========================================
@app.route("/products", methods=["GET"])
def fetch_products():

    products = get_all_products()

    return jsonify(products), 200


# ==========================================
# GET PRODUCT BY ID
# ==========================================
@app.route("/products/<int:product_id>", methods=["GET"])
def fetch_product(product_id):

    product = get_product(product_id)

    if product:
        return jsonify(product), 200

    return jsonify({
        "error": "Product not found"
    }), 404


# ==========================================
# ADD PRODUCT
# ==========================================
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

    return jsonify({
        "message": "Product added successfully!",
        "product_id": product_id
    }), 201


# ==========================================
# UPDATE PRODUCT
# ==========================================
@app.route("/products/<int:product_id>", methods=["PUT"])
def edit_product(product_id):

    product = get_product(product_id)

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

    return jsonify({
        "message": "Product updated successfully!"
    }), 200


# ==========================================
# DELETE PRODUCT
# ==========================================
@app.route("/products/<int:product_id>", methods=["DELETE"])
def remove_product(product_id):

    product = get_product(product_id)

    if not product:
        return jsonify({
            "error": "Product not found"
        }), 404

    delete_product(product_id)

    return jsonify({
        "message": "Product deleted successfully!"
    }), 200


# ==========================================
# RUN APPLICATION
# ==========================================
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)