import json
import sys

THRESHOLD = 0.85

with open("metrics.json") as f:
    metrics = json.load(f)

accuracy = metrics["accuracy"]

print(f"Model accuracy: {accuracy}")

if accuracy < THRESHOLD:
    print("Model performance below threshold. Failing pipeline.")
    sys.exit(1)

print("Model passed performance gate.")
