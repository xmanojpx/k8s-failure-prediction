import unittest
from src.data_collection.collect_metrics import collect_metrics

class TestDataCollection(unittest.TestCase):

    def test_collect_metrics(self):
        # Test the metrics collection function
        metrics = collect_metrics()
        self.assertIsInstance(metrics, dict)
        self.assertIn('cpu_usage', metrics)
        self.assertIn('memory_usage', metrics)
        self.assertIn('pod_status', metrics)
        self.assertIn('network_io', metrics)

    def test_metrics_values(self):
        # Test the values of the collected metrics
        metrics = collect_metrics()
        self.assertGreaterEqual(metrics['cpu_usage'], 0)
        self.assertGreaterEqual(metrics['memory_usage'], 0)
        self.assertIsInstance(metrics['pod_status'], str)
        self.assertGreaterEqual(metrics['network_io'], 0)

if __name__ == '__main__':
    unittest.main()