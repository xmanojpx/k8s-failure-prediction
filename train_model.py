import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

class K8sFailurePredictor:
    def __init__(self):
        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42
        )
        self.scaler = StandardScaler()
        
    def prepare_features(self, df):
        """Prepare features for training"""
        # Convert timestamp to useful features
        df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
        df['day_of_week'] = pd.to_datetime(df['timestamp']).dt.dayofweek
        
        # Select features for training
        feature_columns = [
            'cpu_usage', 'memory_usage', 'network_io', 'disk_usage',
            'pod_restarts', 'response_time', 'hour', 'day_of_week'
        ]
        
        return df[feature_columns]
    
    def train(self, data_file):
        """Train the model using the provided dataset"""
        # Load data
        df = pd.read_csv(data_file)
        
        # Prepare features and target
        X = self.prepare_features(df)
        y = df['is_failure']
        
        # Split dataset
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Train model
        print("Training model...")
        self.model.fit(X_train_scaled, y_train)
        
        # Evaluate model
        y_pred = self.model.predict(X_test_scaled)
        
        # Print metrics
        print("\nModel Performance:")
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))
        
        # Plot confusion matrix
        self.plot_confusion_matrix(y_test, y_pred)
        
        # Plot feature importance
        self.plot_feature_importance(X.columns)
        
        # Save model and scaler
        self.save_model()
        
    def plot_confusion_matrix(self, y_true, y_pred):
        """Plot confusion matrix"""
        cm = confusion_matrix(y_true, y_pred)
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.title('Confusion Matrix')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.savefig('confusion_matrix.png')
        plt.close()
        
    def plot_feature_importance(self, feature_names):
        """Plot feature importance"""
        importances = self.model.feature_importances_
        indices = np.argsort(importances)[::-1]
        
        plt.figure(figsize=(10, 6))
        plt.title('Feature Importance')
        plt.bar(range(len(importances)), importances[indices])
        plt.xticks(range(len(importances)), [feature_names[i] for i in indices], rotation=45)
        plt.tight_layout()
        plt.savefig('feature_importance.png')
        plt.close()
        
    def save_model(self):
        """Save the trained model and scaler"""
        joblib.dump(self.model, 'k8s_failure_predictor.joblib')
        joblib.dump(self.scaler, 'k8s_scaler.joblib')
        print("\nModel and scaler saved to disk")

def main():
    predictor = K8sFailurePredictor()
    predictor.train('k8s_metrics.csv')

if __name__ == "__main__":
    main() 