import joblib
import pandas as pd
import numpy as np
from datetime import datetime

class K8sFailurePredictor:
    def __init__(self, model_path='k8s_failure_predictor.joblib', scaler_path='k8s_scaler.joblib'):
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)
        
    def prepare_features(self, metrics):
        """Prepare features for prediction"""
        # Add time-based features
        current_time = datetime.now()
        metrics['hour'] = current_time.hour
        metrics['day_of_week'] = current_time.weekday()
        
        # Create DataFrame with expected column order
        feature_columns = [
            'cpu_usage', 'memory_usage', 'network_io', 'disk_usage',
            'pod_restarts', 'response_time', 'hour', 'day_of_week'
        ]
        
        df = pd.DataFrame([metrics])[feature_columns]
        return df
    
    def predict(self, metrics):
        """Make prediction based on current metrics"""
        # Prepare features
        X = self.prepare_features(metrics)
        
        # Scale features
        X_scaled = self.scaler.transform(X)
        
        # Make prediction
        prediction = self.model.predict(X_scaled)[0]
        probability = self.model.predict_proba(X_scaled)[0][1]
        
        return {
            'prediction': bool(prediction),
            'failure_probability': float(probability),
            'timestamp': datetime.now().isoformat()
        }

def main():
    # Example usage
    predictor = K8sFailurePredictor()
    
    # Example metrics
    current_metrics = {
        'cpu_usage': 90.5,
        'memory_usage': 85.2,
        'network_io': 750.0,
        'disk_usage': 88.5,
        'pod_restarts': 4,
        'response_time': 2.5
    }
    
    # Make prediction
    result = predictor.predict(current_metrics)
    
    # Print results
    print("\nPrediction Results:")
    print(f"Failure Predicted: {result['prediction']}")
    print(f"Failure Probability: {result['failure_probability']:.2%}")
    print(f"Timestamp: {result['timestamp']}")

if __name__ == "__main__":
    main() 