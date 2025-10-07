#first run pip install ucimlrepo
import pandas as pd
from ucimlrepo import fetch_ucirepo

# fetch dataset
in_vehicle_coupon_recommendation = fetch_ucirepo(id=603)

# data (as pandas dataframes)
X = in_vehicle_coupon_recommendation.data.features
y = in_vehicle_coupon_recommendation.data.targets

# metadata
#print(in_vehicle_coupon_recommendation.metadata)
pd.set_option('display.max_columns', None)  # Show all columns
print(X.head())
# variable information
#print(in_vehicle_coupon_recommendation.variables)