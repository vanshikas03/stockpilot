import unittest
import json

from App import app


class SupplierTestCase(unittest.TestCase):
    """Unit tests for Supplier API."""

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_get_all_suppliers(self):
        """Test GET /suppliers."""

        response = self.client.get("/suppliers")

        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)

        self.assertIsInstance(data, list)

    def test_get_single_supplier(self):
        """Test GET /suppliers/<id>."""

        response = self.client.get("/suppliers/1")

        self.assertIn(response.status_code, [200, 404])

    def test_create_supplier(self):
        """Test POST /suppliers."""

        payload = {
            "supplier_name": "Unit Test Supplier",
            "contact_person": "John Doe",
            "email": "john@test.com",
            "phone": "9876543210",
            "address": "Delhi",
        }

        response = self.client.post("/suppliers", json=payload)

        self.assertEqual(response.status_code, 201)

    def test_update_supplier(self):
        """Test PUT /suppliers/<id>."""

        payload = {
            "supplier_name": "Updated Supplier",
            "contact_person": "Jane Doe",
            "email": "jane@test.com",
            "phone": "9999999999",
            "address": "Mumbai",
        }

        response = self.client.put("/suppliers/1", json=payload)

        self.assertIn(response.status_code, [200, 404])

    def test_delete_supplier(self):
        """Test DELETE /suppliers/<id>."""

        response = self.client.delete("/suppliers/99999")

        self.assertIn(response.status_code, [200, 404])


if __name__ == "__main__":
    unittest.main()
