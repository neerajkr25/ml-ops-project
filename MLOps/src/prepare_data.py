import pandas as pd
from sklearn.datasets import load_iris
import os

def prepare():
    iris = load_iris(as_frame=True)
    df = iris.frame
    df.rename(columns={"target": "species"}, inplace=True)

    # Convert numeric target to actual species names
    df["species"] = df["species"].map(dict(enumerate(iris.target_names)))

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/iris.csv", index=False)

    print("Dataset saved to data/iris.csv")

if __name__ == "__main__":
    prepare()
