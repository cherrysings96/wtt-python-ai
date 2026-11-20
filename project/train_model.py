import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# 1. Load the Kaggle dataset
df = pd.read_csv('online_shoppers_intention.csv')

# 2. Preprocess categorical columns into numeric
df['VisitorType_Numeric'] = df['VisitorType'].apply(lambda x: 1 if x == 'Returning_Visitor' else 0)
df['Weekend_Numeric'] = df['Weekend'].astype(int)
df['Revenue_Target'] = df['Revenue'].astype(int)

# 3. Select core browsing and shopping behaviour features
features = [
    'Administrative',
    'Informational',
    'ProductRelated',
    'ProductRelated_Duration',
    'BounceRates',
    'ExitRates',
    'PageValues',
    'VisitorType_Numeric',
    'Weekend_Numeric'
]

X = df[features]
y = df['Revenue_Target']

# 4. Train-Test Split (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 5. Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 6. Train Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
model.fit(X_train_scaled, y_train)

# 7. Evaluate the model
y_pred = model.predict(X_test_scaled)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 8. Save the trained model and scaler
joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("Saved model.pkl and scaler.pkl successfully!")