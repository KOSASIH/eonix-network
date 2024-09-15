import unittest
from eonix_ml import EonixML

class TestEonixML(unittest.TestCase):
    def test_load_data(self):
        eonix_ml = EonixML()
        eonix_ml.load_data("data.csv")
        self.assertTrue(eonix_ml.model is not None)

    def test_predict(self):
        eonix_ml = EonixML()
        eonix_ml.load_data("data.csv")
        data = [1, 2, 3, 4, 5, 6]
        predictions = eonix_ml.predict(data)
        self.assertTrue(len(predictions) == 6)

    def test_save_model(self):
        eonix_ml = EonixML()
        eonix_ml.load_data("data.csv")
        eonix_ml.save_model("eonix_ml_model.bin")
        self.assertTrue("eonix_ml_model.bin" in os.listdir())

    def test_load_model(self):
        eonix_ml = EonixML()
        eonix_ml.load_model("eonix_ml_model.bin")
        self.assertTrue(eonix_ml.model is not None)

if __name__ == "__main__":
    unittest.main()
