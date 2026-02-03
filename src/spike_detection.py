import pandas as pd

def compute_daily_cost(df):
    return (
        df.groupby("date")["cost"]
        .sum()
        .reset_index()
        .sort_values("date")
    )

def detect_spikes(daily_df, threshold=2):
    daily_df = daily_df.copy()

    daily_df["rolling_mean"] = daily_df["cost"].rolling(7, min_periods=3).mean()
    daily_df["rolling_std"] = daily_df["cost"].rolling(7, min_periods=3).std()

    daily_df["z_score"] = (
        (daily_df["cost"] - daily_df["rolling_mean"]) /
        daily_df["rolling_std"]
    )

    return daily_df[daily_df["z_score"] > threshold]
