#This model allocates each SKU to Tier A, B, or C based on the annual usage value and cumulative percentage.
import math


skus = [
    {"sku": "BRK-100", "demand": 2000, "cost": 45},
    {"sku": "GSK-220", "demand": 1500, "cost": 30},
    {"sku": "BLT-010", "demand": 10000, "cost": 2},
    {"sku": "BRG-330", "demand": 800, "cost": 60},
    {"sku": "SEAL-500", "demand": 3000, "cost": 5},
    {"sku": "MTR-700", "demand": 50, "cost": 800},
    {"sku": "WSH-050", "demand": 20000, "cost": 0.5},
    {"sku": "CBL-900", "demand": 400, "cost": 25}
]

# usage calculation
def usage_value(demand, cost):
    return demand * cost

# Calculation of  usage value for every SKU
for item in skus:
    item["value"] = usage_value(item["demand"], item["cost"])

# Sorting SKUs
skus_sorted = sorted(
    skus,
    key=lambda item: item["value"],
    reverse=True
)

# Calculation of total value
total_value = sum(item["value"] for item in skus_sorted)

# Calculation of  cumulative %
running_total = 0

for item in skus_sorted:
    running_total += item["value"]
    item["cum_pct"] = (running_total / total_value) * 100

# ABC tier
def assign_tier(cum_pct):
    if cum_pct <= 80:
        return "A"
    elif cum_pct <= 95:
        return "B"
    else:
        return "C"


for item in skus_sorted:
    item["tier"] = assign_tier(item["cum_pct"])


print("ABC INVENTORY CLASSIFICATION")
print("-----------------------------")

for item in skus_sorted:
    print(
        item["sku"],
        "| value:", item["value"],
        "| cum %:", round(item["cum_pct"], 1),
        "| tier:", item["tier"]
    )


tier_counts = {"A": 0, "B": 0, "C": 0}

for item in skus_sorted:
    tier_counts[item["tier"]] += 1

print("-----------------------------")
print("Tier counts:", tier_counts)