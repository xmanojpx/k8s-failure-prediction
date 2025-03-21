# Kubernetes Failure Prediction System

This project implements a machine learning-based system for predicting potential failures in Kubernetes clusters. The system analyzes various metrics and uses machine learning to predict potential issues before they occur.

## Features

- Data collection from Kubernetes clusters (simulated in this phase)
- Machine learning model for failure prediction
- Real-time prediction capabilities
- Visualization of model performance and feature importance
- Support for multiple types of failures:
  - Node/pod failures
  - Resource exhaustion
  - Network issues
  - Service disruptions

## Requirements

Install the required packages using:

```bash
pip install -r requirements.txt
```

## Project Structure

- `data_collector.py`: Simulates and collects Kubernetes cluster metrics
- `train_model.py`: Trains the machine learning model on collected data
- `predict.py`: Makes real-time predictions using the trained model
- `requirements.txt`: List of Python dependencies
- Generated files:
  - `k8s_metrics.csv`: Dataset of collected metrics
  - `k8s_failure_predictor.joblib`: Trained model
  - `k8s_scaler.joblib`: Feature scaler
  - `confusion_matrix.png`: Model performance visualization
  - `feature_importance.png`: Feature importance visualization

## Usage

1. Generate training data:
```bash
python data_collector.py
```

2. Train the model:
```bash
python train_model.py
```

3. Make predictions:
```bash
python predict.py
```

## Model Details

The system uses a Random Forest Classifier with the following features:
- CPU usage
- Memory usage
- Network I/O
- Disk usage
- Pod restart count
- Service response time
- Time-based features (hour, day of week)

## Performance Metrics

The model's performance can be evaluated using:
- Classification report (precision, recall, F1-score)
- Confusion matrix visualization
- Feature importance analysis

## Future Improvements

1. Integration with real Kubernetes clusters
2. Support for additional metrics and failure types
3. Real-time monitoring and alerting system
4. Model retraining pipeline
5. Integration with popular monitoring tools

## License

MIT License