import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection details for Docker
db_host = "localhost"  # Host for connections from your local machine
db_port = "5433"       # Host port mapped to the container
db_name = "ny_taxi"    # Database name
db_user = "postgres"   # Username
db_password = "postgres"  # Password

# Creating the PostgreSQL connection engine
engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

# Function to load CSV data into PostgreSQL
def load_csv_to_postgres(csv_file, table_name):
    try:
        # Read the CSV file
        df = pd.read_csv(
            csv_file,
            low_memory=False,           # Avoid mixed type warnings
            encoding="ISO-8859-1"       # Handle encoding issues
        )
        # Writing the data into PostgreSQL
        df.to_sql(table_name, engine, index=False, if_exists="replace")
        print(f"Data successfully loaded into '{table_name}'.")
    except Exception as e:
        print(f"Error loading data: {e}")

# Loading datasets into PostgreSQL
load_csv_to_postgres("green_tripdata_2019-10.csv", "green_tripdata_2019_10")
load_csv_to_postgres("taxi_zone_lookup.csv", "taxi_zone_lookup")