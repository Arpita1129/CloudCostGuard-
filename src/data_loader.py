import pandas as pd

def load_billing_data(path: str):
    return pd.read_csv(path, parse_dates=["date"])
