import pandas as pd
import datetime as tm
import seaborn as sbn
import matplotlib.pyplot as plt
df= pd.read_csv(r"C:\Users\Lenovo\Downloads\4. covid_19_data.csv")
print(" COVID-DATA ANALYSIS ON THE DATA USED AS ON APRIL 29,2020")
print(df)
df1=df.count()
print(df1)
null_values= df.isnull().sum()
print(null_values)

print("---------------------------------------------------------")

sbn.heatmap(df.isnull())
plt.show()

print("---------------------------------------------------------")

print("Data shape")
print(df.shape)

print("Data Size", df.size)

print("Total confirmed Cases:",df['Confirmed'].sum())

print("---------------------------------------------------------")
print("Top 10 countries with Confirmed cases")
print(df.groupby('Region')['Confirmed'].sum().sort_values(ascending=False).head(10))

print("---------------------------------------------------------")
print("Top 10 list Regarding Deaths")
print(df.groupby('Region')['Deaths'].sum().sort_values(ascending=False).head(10))

print("---------------------------------------------------------")
print("Top 10 recovered countries: ")
print(df.groupby('Region')['Recovered'].sum().sort_values(ascending=False).head(10))

print("----------------------------------------------------------")
print("Top 10 Least affected nations or Confirmed cases: ")
print(df.groupby('Region')['Confirmed'].sum().sort_values(ascending=True).head(10))
print("Top 10 regarding less deaths: ")
print(df.groupby('Region')['Deaths'].sum().sort_values(ascending=True).head(10))

print("----------------------------------------------------------")
print("confirmed cases recorded in India: ")
print(df[df.Region=='India'])
print("Confirmed deaths in India: ")


