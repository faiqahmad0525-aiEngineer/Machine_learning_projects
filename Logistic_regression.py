import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , classification_report, confusion_matrix

# Create Sample dataset
df = pd.read_csv(r"C:\Users\ADMIN\Downloads\archive (8)\heart.csv")
print(df.columns)

# split data into feature adn lable
X = df.drop("target", axis=1)
y = df["target"]

#train adn test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)

# model training
model = LogisticRegression()
model.fit(X_train, y_train)

#prediction
y_pred = model.predict(X_test)
print("Predicted values:", y_pred)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)
print("classificatio report:", classification_report(y_test, y_pred))
print("confusion matrix:", confusion_matrix(y_test, y_pred))
