import unittest
from src.model.train_model import train_model
from src.model.evaluate_model import evaluate_model
from src.model.predict_issues import predict_issues

class TestModel(unittest.TestCase):

    def setUp(self):
        # Setup code to initialize any required variables or states
        self.training_data = 'data/processed/training_data.csv'
        self.test_data = 'data/processed/test_data.csv'  # Assuming test data is available
        self.model = train_model(self.training_data)

    def test_model_training(self):
        # Test if the model is trained correctly
        self.assertIsNotNone(self.model, "Model should not be None after training")

    def test_model_evaluation(self):
        # Test model evaluation
        metrics = evaluate_model(self.model, self.test_data)
        self.assertIn('accuracy', metrics, "Metrics should contain accuracy")
        self.assertGreaterEqual(metrics['accuracy'], 0.7, "Model accuracy should be at least 70%")

    def test_model_prediction(self):
        # Test model predictions
        sample_data = {'cpu_usage': 0.5, 'memory_usage': 0.7}  # Example input
        prediction = predict_issues(self.model, sample_data)
        self.assertIn(prediction, ['failure', 'no_failure'], "Prediction should be either 'failure' or 'no_failure'")

if __name__ == '__main__':
    unittest.main()