
import unittest
import sqlite3
import tempfile
import os
import app as app_module
from database import create_database


class HotelBookingAPITest(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, "hotel.db")

        original_connect = sqlite3.connect

        def test_connect(*args, **kwargs):
            if args and args[0] == "hotel.db":
                return original_connect(self.db_path, **kwargs)
            return original_connect(*args, **kwargs)

        self.original_connect = sqlite3.connect
        sqlite3.connect = test_connect

        create_database()
        self.client = app_module.app.test_client()

    def tearDown(self):
        sqlite3.connect = self.original_connect
        self.temp_dir.cleanup()

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)

    def test_hotels_endpoint(self):
        response = self.client.get("/hotels")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.get_json()), 2)


if __name__ == "__main__":
    unittest.main()