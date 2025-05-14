import json
import pandas as pd

def export_to_json(data, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def export_to_csv(data, filepath):
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)
