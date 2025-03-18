from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

from sklearn.preprocessing import LabelEncoder


# Fetch dataset (Heart Disease dataset)
heart_disease = fetch_ucirepo(id=45)


# Access dataframe if available
if hasattr(heart_disease, 'dataframe') and heart_disease.dataframe is not None:
    heart_disease_df = heart_disease.dataframe
else:
    print("Dataframe not available, loading raw data.")
    # Manually handling the raw data (assuming 'features' and 'targets' are available)
    features = heart_disease.data.features
    target = heart_disease.data.targets
    
    # Create DataFrame
    heart_disease_df = pd.DataFrame(features, columns=heart_disease.data.feature_names)
    heart_disease_df['target'] = target

# # Check for missing values
# print(heart_disease_df.isnull().sum())

# Option 1: Fill missing values with the median (for numerical columns)
heart_disease_df['ca'].fillna(heart_disease_df['ca'].median(), inplace=True)
heart_disease_df['thal'].fillna(heart_disease_df['thal'].mode()[0], inplace=True)

# # Option 2: Drop rows with missing values (if appropriate)
# heart_disease_df.dropna(inplace=True)


# Encode categorical columns (assuming 'sex', 'cp', 'restecg', etc. are categorical)
le = LabelEncoder()

# Apply label encoding to categorical columns
heart_disease_df['sex'] = le.fit_transform(heart_disease_df['sex'])
heart_disease_df['cp'] = le.fit_transform(heart_disease_df['cp'])
heart_disease_df['fbs'] = le.fit_transform(heart_disease_df['fbs'])
heart_disease_df['restecg'] = le.fit_transform(heart_disease_df['restecg'])
heart_disease_df['exang'] = le.fit_transform(heart_disease_df['exang'])
heart_disease_df['slope'] = le.fit_transform(heart_disease_df['slope'])
heart_disease_df['thal'] = le.fit_transform(heart_disease_df['thal'])



# Split the data into features (X) and target (y)
X = heart_disease_df.drop('target', axis=1)  # Features
y = heart_disease_df['target']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Classifier model
rf_model = RandomForestClassifier(random_state=42)

# Train the model on the training data
rf_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_model.predict(X_test)

# # Evaluate the model
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Random Forest Model Accuracy: {accuracy:.4f}")

# # Optional: Print feature importances to understand which features are most important
# print("Feature Importances:")
# for feature, importance in zip(X.columns, rf_model.feature_importances_):
#     print(f"{feature}: {importance:.4f}")


# # Sort features by their importance
feature_importance = pd.DataFrame({'Feature': X.columns, 'Importance': rf_model.feature_importances_})
feature_importance = feature_importance.sort_values(by='Importance', ascending=False)

# Print the sorted features and their importance scores
# print(feature_importance)


# Select top 5 most important features
top_n_features = feature_importance['Feature'].head(5)

# Filter the dataset to only include top N features
X_top5 = X[top_n_features]

# Train the model using the selected top 5 features
rf_model.fit(X_top5, y)

# Evaluate the model's performance
y_pred = rf_model.predict(X_test[top_n_features])
accuracy = accuracy_score(y_test, y_pred)
print(f"Random Forest Model Accuracy with Top 5 Features: {accuracy:.4f}")
