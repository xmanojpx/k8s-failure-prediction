import pandas as pd
import numpy as np

def load_data(file_path):
    """Load raw metrics data from a CSV file."""
    data = pd.read_csv(file_path)
    return data

def handle_missing_values(data):
    """Handle missing values in the dataset."""
    # Example: Fill missing values with the mean of the column
    return data.fillna(data.mean())

def normalize_data(data):
    """Normalize the dataset to a range of [0, 1]."""
    return (data - data.min()) / (data.max() - data.min())

def extract_features(data):
    """Extract relevant features from the raw metrics data."""
    # Example: Create a new feature based on existing metrics
    data['cpu_memory_ratio'] = data['cpu_usage'] / (data['memory_usage'] + 1e-6)  # Avoid division by zero
    return data

def preprocess_data(file_path):
    """Main function to preprocess the raw metrics data."""
    data = load_data(file_path)
    data = handle_missing_values(data)
    data = normalize_data(data)
    data = extract_features(data)
    return data