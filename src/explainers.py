def explain_spike(date):
    return (
        f"A cloud cost spike was detected on {date}. "
        f"This usually happens due to sudden scaling or misconfigured services."
    )

def explain_idle(row):
    return (
        f"Resource {row['resource_id']} ({row['service_name']}, {row['region']}) "
        f"is costing {row['cost_per_day']:.2f} per day with very low usage "
        f"({row['usage_per_day']:.2f}), indicating cost leakage."
    )
