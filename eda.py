import pandas as pd
import plotly.express as px

df = pd.read_csv(r"C:\Users\dines\OneDrive\Documents\online_retail\cleaned_sales.csv")
#print(df.info())
df = df.fillna('n/a')

def get_category_sales(df):
    fig = px.bar(df,x='month',y='sales',color='category_name',title='monthly sales of category')
    return fig

def get_paymentmethod(df):   
    fig = px.bar(df,x='category_name',y='product_name',color='payment_method',title='paytmenttype vs category')
    return fig
#fig.show()
def get_monthlysales(df):
    monthly = df.groupby('month')['sales'].sum().reset_index()
    fig = px.line(monthly, x = 'month', y='sales', title='Monthly Sales Trend')
    return fig
def get_topcitys(df):
    top_citys = df.groupby('city')['sales'].sum().sort_values(ascending=False).head(10)
    fig = px.bar(top_citys,x=top_citys.index,y=top_citys.values,title='Top 10 cities')
    return fig

def get_bottomcitys(df):
    top_citys = df.groupby('city')['sales'].sum().sort_values(ascending=True).head(10)
    fig = px.bar(top_citys,x=top_citys.index,y=top_citys.values,title='bottom 10 cities')
    return fig

def get_category_percentage(df):
    fig = px.pie(df,values='sales',names='category_name',title='percentage each category imapacting')
    return fig
def price_distribution(df):
    fig = px.scatter(df,x='price',y='quantity',size='sales',title='price vs quantity')
    return fig

def age_group(df):
    fig = px.histogram(df,x='age',nbins=20,title='Age group')
    return fig

def gender(df):
    fig = px.bar(df,x='gender',y='sales',title='gender vs sales')
    return fig

  
def review(df):
    fig = px.scatter(df,x='sales',y='review_score',size='price',title='review vs sales')
    return fig
def age_sales(df):
    fig = px.bar(df,x='age',y='sales',title='age vs sales')
    return fig

def heat(df):
    heatmap_data = df.groupby(['category_name', 'month'])['sales'].sum().reset_index()

    pivot_table = heatmap_data.pivot(
        index='category_name',
        columns='month',
        values='sales'
    )

    fig = px.imshow(
        pivot_table,
        title="Sales Heatmap (Category vs Month)",
        labels=dict(x="Month", y="Category", color="Sales")
    )
    return fig





