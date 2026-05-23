import pandas as pd
df= pd.read_csv('customer_shopping_behavior.csv')
print(df.head())
print(df.info())
print(df.describe(include="all"))
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(
    lambda x: x.fillna(x.median())
)
print(df['Review Rating'].head())
print(df.isnull().sum())
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
df=df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)
#creating new age group 
labels =['young_adult','adult', 'middle_aged','senior']
df['age_group'] = pd.qcut(df['age'],q=4, labels=labels)
print(df[['age','age_group']].head(10))
#purchase frequency days
frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)

print(df[['purchase_frequency_days', 'frequency_of_purchases']].head(10))
print(df[['discount_applied','promo_code_used']].head(10))
print((df['discount_applied'] == df['promo_code_used']).all())
df=df.drop(columns=['promo_code_used'])
print(df.columns)


# connect mysql
from sqlalchemy import create_engine

# your cleaning code already done above

# now connect mysql

import pandas as pd
from sqlalchemy import create_engine

# mysql connection

username = "root"
password = "Abhi%4054321"
host = "localhost"
port = "3306"
database = "customer_analysis"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

print("Connected Successfully")

# upload dataframe to mysql

df.to_sql(
    name='shopping_data',
    con=engine,
    if_exists='replace',
    index=False
)

print("Data uploaded successfully")