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

# Create database when application starts
create_database()


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to StockPilot Inventory API!"
    })


# -----------------------------
# GET ALL PRODUCTS
# -----------------------------
@app.route("/products", methods=["GET"])
def fetch_products():

    products = get_all_products()

    return jsonify(products), 200

# -----------------------------
# ADD PRODUCT
# -----------------------------
@app.route("/products", methods=["POST"])
def create_product():

    data = request.get_json()

    # Validation
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
                "error": f"{field} is required"
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

if __name__ == "__main__":
    app.run(debug=True)