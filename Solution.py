

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

def load_data():
    iris = load_iris()
    X = iris.data
    y = iris.target

    df = pd.DataFrame(X, columns=iris.feature_names)
    df["species"] = y

    print("First 5 rows of data:")
    print(df.head())
    print("\nFeature names:", iris.feature_names)
    print("Target names:", iris.target_names)
    print("\nShape of data:", df.shape)

    return df, iris

def train_test_split_data(df):
    X = df.drop("species", axis=1)
    y = df["species"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("\nTrain shape:", X_train.shape, "Test shape:", X_test.shape)
    return X_train, X_test, y_train, y_test

def train_logistic_regression(X_train, y_train):
    log_reg = LogisticRegression(max_iter=200)
    log_reg.fit(X_train, y_train)
    print("\nLogistic Regression training complete.")
    return log_reg

def evaluate_model(model, X_test, y_test, model_name="Model"):
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print(f"\n=== {model_name} Evaluation ===")
    print("Accuracy:", acc)
    print("\nClassification report:")
    print(classification_report(y_test, y_pred))

    print("Sample predictions vs true:")
    for i in range(min(5, len(y_test))):
        print(f"Predicted: {y_pred[i]}, True: {y_test.iloc[i]}")
    return acc

def train_knn(X_train, y_train, n_neighbors=5):
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train, y_train)
    print(f"\nKNN (k={n_neighbors}) training complete.")
    return knn

def main():
    df, iris = load_data()
    X_train, X_test, y_train, y_test = train_test_split_data(df)

    #Logistic Regression
    log_reg_model = train_logistic_regression(X_train, y_train)
    log_reg_acc = evaluate_model(log_reg_model, X_test, y_test, "Logistic Regression")

    #KNN
    knn_model = train_knn(X_train, y_train, n_neighbors=5)
    knn_acc = evaluate_model(knn_model, X_test, y_test, "KNN (k=5)")

    print("\nSummary:")
    print(f"Logistic Regression accuracy: {log_reg_acc:.4f}")
    print(f"KNN (k=5) accuracy: {knn_acc:.4f}")

    if knn_acc > log_reg_acc:
        print("KNN performed better on this test split.")
    elif knn_acc < log_reg_acc:
        print("Logistic Regression performed better on this test split.")
    else:
        print("Both models performed equally on this test split.")

if __name__ == "__main__":
    main()
