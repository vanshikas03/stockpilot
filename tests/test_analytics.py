import unittest
import json

from App import app


class AnalyticsTestCase(unittest.TestCase):
    """Unit tests for Analytics API."""

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_get_analytics(self):
        """Test GET /analytics."""

        response = self.client.get("/analytics")

        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)

        self.assertIn("total_products", data)
        self.assertIn("total_inventory_value", data)
        self.assertIn("low_stock_products", data)
        self.assertIn("products_by_category", data)
        self.assertIn("most_valuable_products", data)
        self.assertIn("restock_recommendations", data)


if __name__ == "__main__":
    unittest.main()
