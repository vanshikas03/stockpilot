import unittest

from App import app


class StockPilotTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    # -------------------------
    # HOME
    # -------------------------
    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # -------------------------
    # GET PRODUCTS
    # -------------------------
    def test_get_products(self):
        response = self.client.get("/products")
        self.assertEqual(response.status_code, 200)

    # -------------------------
    # GET SUPPLIERS
    # -------------------------
    def test_get_suppliers(self):
        response = self.client.get("/suppliers")
        self.assertEqual(response.status_code, 200)

    # -------------------------
    # ANALYTICS
    # -------------------------
    def test_analytics(self):
        response = self.client.get("/analytics")
        self.assertEqual(response.status_code, 200)

    # -------------------------
    # INVENTORY LOGS
    # -------------------------
    def test_inventory_logs(self):
        response = self.client.get("/inventory-logs")
        self.assertEqual(response.status_code, 200)

    # -------------------------
    # CREATE PRODUCT
    # -------------------------
    def test_create_product(self):

        response = self.client.post(
            "/products",
            json={
                "supplier_id": 1,
                "product_name": "Test Product",
                "category": "Testing",
                "quantity": 5,
                "purchase_price": 100,
                "selling_price": 150,
                "reorder_level": 2
            }
        )

        self.assertEqual(response.status_code, 201)

        data = response.get_json()

        self.assertIn("product_id", data)


if __name__ == "__main__":
    unittest.main()