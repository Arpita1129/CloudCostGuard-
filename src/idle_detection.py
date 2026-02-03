def detect_idle_resources(df):
    resource_df = (
        df.groupby("resource_id")
        .agg(
            total_cost=("cost", "sum"),
            total_usage=("usage_amount", "sum"),
            active_days=("date", "nunique"),
            service_name=("service_name", "first"),
            region=("region", "first")
        )
        .reset_index()
    )

    resource_df["cost_per_day"] = resource_df["total_cost"] / resource_df["active_days"]
    resource_df["usage_per_day"] = resource_df["total_usage"] / resource_df["active_days"]

    cost_th = resource_df["cost_per_day"].quantile(0.75)
    usage_th = resource_df["usage_per_day"].quantile(0.25)

    idle = resource_df[
        (resource_df["cost_per_day"] >= cost_th) &
        (resource_df["usage_per_day"] <= usage_th)
    ]

    return idle.sort_values("cost_per_day", ascending=False)
