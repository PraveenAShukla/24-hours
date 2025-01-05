import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load Dataset
data = pd.read_csv('C:/My Projects/credit/data/credit_data.csv')


# Features and Target
X = data.drop('Default', axis=1)
y = data['Default']

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save Model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)


print("Model trained and saved successfully!")
