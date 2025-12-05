import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv(r"C:\Users\dines\OneDrive\Documents\online_retail\synthetic_online_retail_data.csv")
#print(df.head(10))
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())
#print(df.duplicated().sum())

#removing duplicated rows if any
df = df.drop_duplicates()
#print(df)

df['order_date'] = pd.to_datetime(
    df['order_date'],
    dayfirst=True,
    format='mixed',
    errors='coerce'
)


#df = (df['product_name'] != df['product_name'].str.strip()).sum()
#print(df)

df['product_name'] = df['product_name'].str.strip().str.title()
df['category_name'] = df['category_name'].str.strip().str.title()
df['payment_method'] = df['payment_method'].str.strip().str.title()
df['city'] = df['city'].str.strip().str.title()
df['gender'] = df['gender'].str.strip().str.title()

df = df.fillna('n/a')
print(df)
#df['gender'].unique()
#df['review_score'].unique()

#df=df['payment_method'].unique()
#df=df['category_name'].unique()

#print(df)
#print(df.isnull().sum())

df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.month
#print(df['year'])

df['sales'] = df['price']*df['quantity']



Q1 = df['sales'].quantile(0.25)
Q3 = df['sales'].quantile(0.75)
IQR = Q3-Q1
lower = Q1 -1.5*IQR
upper = Q3 + 1.5*IQR
df = df[(df['sales'] >= lower) & (df['sales'] <= upper)]

print(df.isnull().sum())
df=df.to_csv("cleaned_sales.csv",index=False)
print(df.isnull().sum())