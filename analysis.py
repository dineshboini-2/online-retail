import pandas as pd
import streamlit as st
from eda import *
import plotly as px

df = pd.read_csv(r"C:\Users\dines\OneDrive\Documents\online_retail\cleaned_sales.csv")
st.title("Online retail sales")


st.plotly_chart(get_paymentmethod(df))

st.write('''  
- Observation    -> Most customers are prefering cash on delivery.
- Reason         -> May be customers are not trusting or not getting offers.
- Impact         -> we may loss our customers.
- Recommendation -> we can give more offers if customers pay via credit card''')
st.write('--------------------------------------------------------------------------------------------------')

st.plotly_chart(get_category_sales(df))
st.write('''  
- Observation    -> alysis.pyWe have better sales in fashion and  sports & Stationary throughout the year,
                    we have incosistence sales in Home & living.
                    we are making higest sales in month of december and lowest in feb.
- Reason         -> Due to christmas in dec we have high sales.
- Recommendation -> We should focus on electronics and home & living  their sales are inconsistent.''')
st.write('--------------------------------------------------------------------------------------------------')

st.plotly_chart(get_monthlysales(df))

st.write('''  
- Observation    -> we are making extreamly less sales in feb.
                    we have low's and high's throught the year.
- Impact         -> we could not make constant sales.
- Recommendation -> mainly we have to focus feb and oct''')
st.write('--------------------------------------------------------------------------------------------------')

st.plotly_chart(get_topcitys(df))
st.write('''  
- Observation    -> We are getting more sales from patriciaville.
- Recommendation -> we should hire more delivery partners for fast delivery.
''')
st.write('--------------------------------------------------------------------------------------------------')

st.plotly_chart(get_bottomcitys(df))
st.write('''  
- Observation    -> In these cities we are making very small amount of sales,
- Reason         -> In these cities they are buying from another platfroms.
- Impact         -> we should advertise more in these cities.
''')
st.write('--------------------------------------------------------------------------------------------------')

st.plotly_chart(get_category_percentage(df))

st.write('''  
- Observation    -> We are getting more revenue from Electronics and less from Fashion.
                    almost we are making normal sales in all categories.''')
st.write('--------------------------------------------------------------------------------------------------')
st.plotly_chart(price_distribution(df))


st.write('''  
- Observation    -> We are getting more revenue from bulk sales.
                    customers are not buying costly products in bulk.
                    we have more sales from single products.
- Impact         ->we have more customers but less sales.
- Recommendation -> we have to give discount coupens if they buy in bulk''')
st.write('--------------------------------------------------------------------------------------------------')

st.plotly_chart(age_group(df))
st.write('''  
- Observation    -> We have most customers in the age group of 60-64
                    an less customers from young group.
- Reason         -> There are less products that are attracting the young age people.
- Impact         -> These are the working people if we enable to attract them we may lose more.
- Recommendation -> we have to sell new products that attract these groups.''')
st.write('--------------------------------------------------------------------------------------------------')

st.plotly_chart(gender(df))

st.write('''  
- Observation    -> We have almost equal customers in male and female.
- Reason         -> So, we don't have to focus more on any particular gender.
- Recommendation -> we dont have to change any thing.
''')
st.write('--------------------------------------------------------------------------------------------------')

st.plotly_chart(review(df))
st.write('''  
- Observation    -> Lot of sales are happening from 1,2 rated products.
                    
- Impact         -> If this continue we may lose lot of customers.
- Recommendation -> we have to remove those products.''')
st.write('--------------------------------------------------------------------------------------------------')
st.plotly_chart(age_sales(df))
st.write('''  
- Observation    -> Even though we have lot of customers in the age group 25-40 we are not getting 
                    lot of revenue.
                    We have very less customers in the age group of 15-20 we are getting lot of sales.
- Reason         -> we are not making promotions that attract this age group so that we make more sales.
- Recommendation -> we have to mainly focus in this age group''')
st.write('--------------------------------------------------------------------------------------------------')
st.plotly_chart(heat(df))
st.write('''  
- Observation    -> We are getting most money from home&living, electronics but only in single month
                    and we making very less money from Home&living in remaing months.
- Reason         -> Becasue of new year people are buying more home&living products.
''')
