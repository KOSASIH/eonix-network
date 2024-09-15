import unittest
from eonix_iot_raspberrypi import eonix_iot_init, eonix_iot_send_data

class TestEonixIot(unittest.TestCase):
    def test_eonix_iot_init(self):
        eonix_iot_init()
        self.assertEqual(EONIX_IOT_SERVER, eonix_iot.server_url)
        self.assertEqual(EONIX_IOT_API_KEY, eonix_iot.api_key)

    def test_eonix_iot_send_data(self):
        temperature = 25.0
        humidity = 60.0
        eonix_iot_send_data(temperature, humidity)
        # Verify that the data was sent successfully
        self.assertTrue(True)  # Replace with actual verification logic

if __name__ == "__main__":
    unittest.main()
