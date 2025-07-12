import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import make_classification

def create_heart_disease_dataset():
    np.random.seed(42)
    X, y = make_classification(n_samples=1000, n_features=13, n_informative=10, 
                             n_redundant=3, n_clusters_per_class=1, random_state=42)
    
    feature_names = ['age', 'sex', 'chest_pain_type', 'resting_bp', 'cholesterol',
                    'fasting_blood_sugar', 'resting_ecg', 'max_heart_rate', 
                    'exercise_angina', 'oldpeak', 'slope', 'ca', 'thal']
    
    df = pd.DataFrame(X, columns=feature_names)
    df['target'] = y
    return df

def main():
    print("Heart Disease Detection Model - Issue #211")
    print("=" * 50)
    
    # Create dataset
    df = create_heart_disease_dataset()
    print(f"Dataset shape: {df.shape}")
    
    # Prepare data
    X = df.drop('target', axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features for KNN
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train Random Forest
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    rf_pred = rf_model.predict(X_test)
    rf_accuracy = accuracy_score(y_test, rf_pred)
    
    # Train KNN
    knn_model = KNeighborsClassifier(n_neighbors=5)
    knn_model.fit(X_train_scaled, y_train)
    knn_pred = knn_model.predict(X_test_scaled)
    knn_accuracy = accuracy_score(y_test, knn_pred)
    
    # Cross-validation
    rf_cv_scores = cross_val_score(rf_model, X_train, y_train, cv=5)
    knn_cv_scores = cross_val_score(knn_model, X_train_scaled, y_train, cv=5)
    
    # Results
    print(f"\nRandom Forest Accuracy: {rf_accuracy:.4f}")
    print(f"KNN Accuracy: {knn_accuracy:.4f}")
    print(f"\nCross-validation:")
    print(f"Random Forest CV Mean: {rf_cv_scores.mean():.4f}")
    print(f"KNN CV Mean: {knn_cv_scores.mean():.4f}")
    
    # Best model
    if rf_accuracy > knn_accuracy:
        print(f"\nBest Model: Random Forest (Accuracy: {rf_accuracy:.4f})")
    elif knn_accuracy > rf_accuracy:
        print(f"\nBest Model: KNN (Accuracy: {knn_accuracy:.4f})")
    else:
        print(f"\nBoth models perform equally (Accuracy: {rf_accuracy:.4f})")
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'feature': X.columns,
        'importance': rf_model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print(f"\nTop 5 Important Features (Random Forest):")
    print(feature_importance.head())
    
    print(f"\nIssue #211 completed successfully!")

if __name__ == "__main__":
    main()
