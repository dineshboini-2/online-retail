import pandas as pd
df=pd.read_csv('https://gist.githubusercontent.com/iwek/4177628/raw/03d302f6461490bea7dcee09b96076053148a1be/sample.log',sep=' ')
df.to_csv('mysample.csv',index=False)
#print(df)
