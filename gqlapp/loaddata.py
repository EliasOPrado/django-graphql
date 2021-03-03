import sqlite3
import pandas as pd

# connect with local db
conn = sqlite3.connect('/Users/macbook/software_projects/graphQl_and_django/gqlproject/db.sqlite3')

# connect with .csv file
df = pd.read_csv('/Users/macbook/software_projects/graphQl_and_django/gqlproject/sam.csv')

df['id'] = df.index

# instanciate csv columns to reflect the data base/ model
df = df[['id', 'Segment', 'Country', 'Product', 'Units', 'Sales', 'Datesold']]

# mirror to db / injection to db
df.to_sql('gqlapp_productmodel', conn, if_exists='replace', index=False)

