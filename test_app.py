
import unittest
import json
from app import app


class HotelBookingAPITest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)

    def test_hotels_endpoint(self):
        response = self.client.get("/hotels")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()