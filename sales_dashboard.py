import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("sales_data.csv")


print(df.head())

sales_by_category = df.groupby("Category")["Sales"].sum()


sales_by_category.plot(kind="bar")

plt.title("Sales Revenue Analysis")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()
