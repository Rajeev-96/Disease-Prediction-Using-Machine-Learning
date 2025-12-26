import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv("dataset/disease_data.csv")

X = data.drop("disease", axis=1)
y = data["disease"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

def predict_disease(symptoms):
    return model.predict([symptoms])[0]
