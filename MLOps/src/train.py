import pandas as pd
import mlflow
import mlflow.sklearn
import json
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

DATA_PATH = "data/iris.csv"
MODEL_PATH = "model.pkl"

def load_data():
    df = pd.read_csv(DATA_PATH)
    X = df.drop("species", axis=1)
    y = df["species"]
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train():
    X_train, X_test, y_train, y_test = load_data()

    mlflow.set_experiment("iris-classifier")

    with mlflow.start_run():
        model = RandomForestClassifier(n_estimators=100)
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)

        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(model, "model")

        joblib.dump(model, MODEL_PATH)

        with open("metrics.json", "w") as f:
            json.dump({"accuracy": acc}, f)

        print(f"Model trained. Accuracy: {acc}")

if __name__ == "__main__":
    train()
