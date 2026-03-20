# ================================
# 📌 1. IMPORT LIBRARIES
# ================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# ================================
# 📌 2. LOAD DATA
# ================================
df = pd.read_csv("discount_impact_dataset.csv")

print("First 5 rows:")
print(df.head())

# ================================
# 📌 3. DATA CLEANING
# ================================
print("\nMissing Values:\n", df.isnull().sum())

df.drop_duplicates(inplace=True)

# ================================
# 📌 4. FEATURE ENGINEERING
# ================================
def discount_level(x):
    if x == 0:
        return "No Discount"
    elif x <= 10:
        return "Low"
    elif x <= 25:
        return "Medium"
    else:
        return "High"

df["Discount_Level"] = df["Discount_Percent"].apply(discount_level)

# ================================
# 📌 5. EDA (VISUALIZATION)
# ================================

# Revenue by Discount Level
plt.figure()
df.groupby("Discount_Level")["Revenue"].sum().plot(kind='bar')
plt.title("Revenue by Discount Level")
plt.xlabel("Discount Level")
plt.ylabel("Total Revenue")
plt.show()

# Quantity Sold vs Discount
plt.figure()
df.groupby("Discount_Percent")["Quantity_Sold"].mean().plot()
plt.title("Quantity Sold vs Discount %")
plt.xlabel("Discount %")
plt.ylabel("Avg Quantity Sold")
plt.show()

# Revenue by Category
plt.figure()
df.groupby("Product_Category")["Revenue"].sum().plot(kind='bar')
plt.title("Revenue by Product Category")
plt.show()

# Region-wise Revenue
plt.figure()
df.groupby("Region")["Revenue"].sum().plot(kind='bar')
plt.title("Revenue by Region")
plt.show()

# Scatter Plot: Discount vs Revenue
plt.figure()
plt.scatter(df["Discount_Percent"], df["Revenue"])
plt.title("Discount vs Revenue")
plt.xlabel("Discount %")
plt.ylabel("Revenue")
plt.show()

# ================================
# 📌 6. MACHINE LEARNING
# ================================

# Features and Target
X = df[["Original_Price", "Discount_Percent", "Quantity_Sold"]]
y = df["Revenue"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# ================================
# 📌 7. MODEL EVALUATION
# ================================
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print("MAE:", mae)
print("R2 Score:", r2)

# ================================
# 📌 8. ACTUAL vs PREDICTED GRAPH
# ================================
plt.figure()
plt.scatter(y_test, y_pred)
plt.title("Actual vs Predicted Revenue")
plt.xlabel("Actual Revenue")
plt.ylabel("Predicted Revenue")
plt.show()

# ================================
# 📌 9. FEATURE IMPORTANCE (COEFFICIENTS)
# ================================
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.coef_
})

print("\nFeature Importance:")
print(importance)

# ================================
# 📌 10. SAVE PROCESSED DATA
# ================================
df.to_csv("processed_discount_data.csv", index=False)

print("\n✅ Project Completed Successfully!")