import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)


def evaluate_model(y_true, y_pred):
    """
    Evaluate the model's predictions against the true labels.

    Args:
    - y_true: np.array, true labels.
    - y_pred: np.array, predicted labels.

    Returns:
    - metrics: dict, containing accuracy, precision, recall, F1 score, and confusion matrix.
    """
    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred),
        "recall": recall_score(y_true, y_pred),
        "f1_score": f1_score(y_true, y_pred),
        "confusion_matrix": confusion_matrix(y_true, y_pred),
    }
    return metrics


def print_evaluation(metrics):
    """
    Print evaluation metrics in a readable format.

    Args:
    - metrics: dict, evaluation metrics.
    """
    print("Evaluation Metrics:")
    print(f"Accuracy: {metrics['accuracy']:.4f}")
    print(f"Precision: {metrics['precision']:.4f}")
    print(f"Recall: {metrics['recall']:.4f}")
    print(f"F1 Score: {metrics['f1_score']:.4f}")
    print("Confusion Matrix:")
    print(metrics["confusion_matrix"])


# Example usage
if __name__ == "__main__":
    # Assuming you have your dataset loaded
    X = np.random.rand(100, 2)  # 100 samples, 2 features
    y_true = np.random.choice([0, 1], size=100)  # Random binary true labels

    # Example predictions from your AlwaysZero model (always predicts 0)
    y_pred = np.zeros(y_true.shape[0])  # Always predict 0

    # Evaluate the model
    metrics = evaluate_model(y_true, y_pred)
    print_evaluation(metrics)
