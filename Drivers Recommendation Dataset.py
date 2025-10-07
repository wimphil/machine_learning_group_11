#first run pip install ucimlrepo
import pandas as pd
from ucimlrepo import fetch_ucirepo
import matplotlib.pyplot as plt
# fetch dataset
in_vehicle_coupon_recommendation = fetch_ucirepo(id=603)

# data (as pandas dataframes)
X = in_vehicle_coupon_recommendation.data.features
y = in_vehicle_coupon_recommendation.data.targets

# metadata
#print(in_vehicle_coupon_recommendation.metadata)
pd.set_option('display.max_columns', None)  # Show all columns
#print(X.head())
# variable information
#print(in_vehicle_coupon_recommendation.variables)
#print(len(X))
#print(X.info())
#print(X.describe())

#####################################Barchart of missing values#######
# 1. Calculate percentage of missing values for each column
missing_percent = X.isnull().mean() * 100
missing_percent = missing_percent[missing_percent > 0].sort_values(ascending=False)

# 2. Create the bar chart
plt.figure(figsize=(10, 6))
ax = missing_percent.plot(kind='bar', color='steelblue')

# 3. Add labels and title
plt.title('Percentage of Missing Values per Feature', fontsize=14)
plt.xlabel('Features', fontsize=12)
plt.ylabel('Missing Values (%)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# use of container
for container in ax.containers:
    ax.bar_label(container, fmt='%.1f%%', label_type='edge', color='blue')

plt.tight_layout()
plt.show()
######################################
X.hist(figsize=(10, 8))
plt.tight_layout()
plt.show()
