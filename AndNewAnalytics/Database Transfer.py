
# Pass in imports
import pandas as pd
from sqlalchemy import create_engine

# Load in the data
df = pd.read_csv("file path / UFC_Fight.csv')

df2 = pd.read_csv(r'file path / UFC_Fighter_Stats.csv')

# Instantiate sqlachemy.create_engine object
engine = create_engine('database path')

# Add updated tables to the database
df.to_sql(
    'Every_Fight', 
    engine,
    index=False,
    if_exists = 'replace'
)

df2.to_sql(
    'Fighter_Profiles', 
    engine,
    index=False,
    if_exists = 'replace'
)
