import json
import pandas as pd

def export_to_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def export_to_csv(data, path):
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)
