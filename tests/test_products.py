import unittest
import json

from App import app


class ProductTestCase(unittest.TestCase):
    """Unit tests for Product API."""

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_get_all_products(self):
        """Test GET /products."""

        response = self.client.get("/products")

        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)

        self.assertIsInstance(data, list)

    def test_get_single_product(self):
        """Test GET /products/<id>."""

        response = self.client.get("/products/1")

        self.assertIn(response.status_code, [200, 404])

    def test_create_product(self):
        """Test POST /products."""

        payload = {
            "supplier_id": 1,
            "product_name": "Unit Test Product",
            "category": "Testing",
            "quantity": 5,
            "purchase_price": 100,
            "selling_price": 150,
            "reorder_level": 2,
        }

        response = self.client.post("/products", json=payload)

        self.assertEqual(response.status_code, 201)

    def test_update_product(self):
        """Test PUT /products/<id>."""

        payload = {
            "supplier_id": 1,
            "product_name": "Updated Product",
            "category": "Testing",
            "quantity": 10,
            "purchase_price": 100,
            "selling_price": 200,
            "reorder_level": 3,
        }

        response = self.client.put("/products/1", json=payload)

        self.assertIn(response.status_code, [200, 404])

    def test_delete_product(self):
        """Test DELETE /products/<id>."""

        response = self.client.delete("/products/99999")

        self.assertIn(response.status_code, [200, 404])


if __name__ == "__main__":
    unittest.main()
