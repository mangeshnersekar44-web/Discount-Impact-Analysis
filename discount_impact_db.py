
import pandas as pd
from sqlalchemy import create_engine

# Read CSV directly
df = pd.read_csv("discount_impact_dataset.csv")

# Create connection
engine = create_engine(
    "mysql+mysqlconnector://root:M084637N@localhost/discount_project"
)

# Upload dataframe to MySQL
df.to_sql(
    name="discount_analysis",
    con=engine,
    if_exists="replace",
    index=False
)

print("✅ Data uploaded successfully!")

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+mysqlconnector://root:M084637N@localhost/discount_project"
)

df = pd.read_sql("SELECT * FROM discount_analysis", engine)

print(df.head())
print(df.columns)
print(df.info())
print(df.shape)



