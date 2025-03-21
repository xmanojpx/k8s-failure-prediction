import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

def evaluate_model(test_data_path, model_path):
    # Load the test data
    test_data = pd.read_csv(test_data_path)
    X_test = test_data.drop('target', axis=1)  # Assuming 'target' is the label column
    y_test = test_data['target']

    # Load the trained model
    model = joblib.load(model_path)

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate evaluation metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')

    # Print the evaluation results
    print(f'Accuracy: {accuracy:.2f}')
    print(f'Precision: {precision:.2f}')
    print(f'Recall: {recall:.2f}')
    print(f'F1 Score: {f1:.2f}')

if __name__ == "__main__":
    evaluate_model('../data/processed/training_data.csv', 'path_to_trained_model.pkl')  # Update with actual paths as needed