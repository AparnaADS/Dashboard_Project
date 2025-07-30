# export.py
import pandas as pd

def export_to_excel(data, filename="due_bills.xlsx"):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"✅ Exported to {filename}")
