import sqlite3
import pandas as pd

DATABASE_NAME = "inventory.db"


def get_analytics():

    connection = sqlite3.connect(DATABASE_NAME)

    # Read products table into a Pandas DataFrame
    df = pd.read_sql_query("SELECT * FROM products", connection)

    connection.close()

    # If database has no products
    if df.empty:
        return {
            "total_products": 0,
            "total_inventory_value": 0,
            "low_stock_products": [],
            "products_by_category": {},
            "most_valuable_products": [],
            "restock_recommendations": []
        }

    # -----------------------------------
    # Total Products
    # -----------------------------------
    total_products = len(df)

    # -----------------------------------
    # Total Inventory Value
    # quantity × purchase_price
    # -----------------------------------
    df["inventory_value"] = df["quantity"] * df["purchase_price"]

    total_inventory_value = float(df["inventory_value"].sum())

    # -----------------------------------
    # Low Stock Products
    # -----------------------------------
    low_stock = df[
        df["quantity"] <= df["reorder_level"]
    ][
        ["product_name", "quantity", "reorder_level"]
    ]

    low_stock_products = low_stock.to_dict(orient="records")

    # -----------------------------------
    # Products By Category
    # -----------------------------------
    products_by_category = (
        df.groupby("category")
          .size()
          .to_dict()
    )

    # -----------------------------------
    # Most Valuable Products
    # -----------------------------------
    valuable = (
        df.sort_values(
            by="inventory_value",
            ascending=False
        )
        .head(5)
    )

    most_valuable_products = valuable[
        ["product_name", "inventory_value"]
    ].to_dict(orient="records")

    # -----------------------------------
    # Restock Recommendations
    # -----------------------------------
    restock = df[
        df["quantity"] <= df["reorder_level"]
    ][
        ["product_name", "quantity", "reorder_level"]
    ]

    restock_recommendations = restock.to_dict(orient="records")

    return {

        "total_products": total_products,

        "total_inventory_value": total_inventory_value,

        "low_stock_products": low_stock_products,

        "products_by_category": products_by_category,

        "most_valuable_products": most_valuable_products,

        "restock_recommendations": restock_recommendations
    }