# Solution for `Module 3 Homework: Data Warehouse`

> This is the solution to the fourth homework for the 2025 cohort of **DE Zoomcamp**.  
> For this homework the Yellow Taxi Trip Records for January 2024 - June 2024 are used. Parquet Files from the New York City Taxi Data were found here:
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
> The files were manually uploaded to GCS Bucket.
 ## BIG QUERY SETUP:
 To create external table using the uploaded data I ran the following query:
```sql
   CREATE OR REPLACE TABLE green-bedrock-450715-u0.yellow_taxi_2024.native_yellow_taxi
AS(
  SELECT * FROM `green-bedrock-450715-u0.yellow_taxi_2024.yellow_taxi_external`
)
```

To create materialized table using the uploaded data I ran the following query:
```sql
   CREATE TABLE `green-bedrock-450715-u0.yellow_taxi_2024.yellow_taxi_materialized`
AS
SELECT * FROM `green-bedrock-450715-u0.yellow_taxi_2024.yellow_taxi_external`;
```
 In the code snippets above 'green-bedrock-450715-u0' is the name BigQuery console assigned automatically to the project.
## Question 1: What is count of records for the 2024 Yellow Taxi Data?
#### Options:
- 65,623
- 840,402
- 20,332,093
- 85,431,289
  
### Solution:
To count the records, I ran the following query:
```sql
SELECT count(1) FROM `green-bedrock-450715-u0.yellow_taxi_2024.yellow_taxi_materialized`;
 ```
### Answer: 
20,332,093

## Question 2: Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables. What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

#### Options:
- 18.82 MB for the External Table and 47.60 MB for the Materialized Table
- 0 MB for the External Table and 155.12 MB for the Materialized Table
- 2.14 GB for the External Table and 0MB for the Materialized Table
- 0 MB for the External Table and 0MB for the Materialized Table
### Solution:
By running the following two queries:
```sql
SELECT COUNT(DISTINCT PULocationID) AS distinct_pu_locations FROM `green-bedrock-450715-u0.yellow_taxi_2024.yellow_taxi_external`;
```
```sql
SELECT COUNT(DISTINCT PULocationID) AS distinct_pu_locations FROM `green-bedrock-450715-u0.yellow_taxi_2024.yellow_taxi_materialized`;
```
for external and materized table respectfully, it is possible to estimate the amount of memory BigQuery will process while running the query. The answer is 
- 0 MB for the External Table and 155.12 MB for the Materialized Table
## Task: Prepare PostgreSQL and Load Data
For this task, I used the python script to load two provided datasets into Postgres. The Python script can be found [here](./load_data_to_postgres.py).


## Question 3:Write a query to retrieve the PULocationID from the table (not the external table) in BigQuery. Now write a query to retrieve the PULocationID and DOLocationID on the same table. Why are the estimated number of Bytes different?

### Solution:
To retrieve the PULocationID:
```sql
SELECT PULocationID FROM `green-bedrock-450715-u0.yellow_taxi_2024.yellow_taxi_materialized`;
```

To retrieve the PULocationID and DOLocationID:
```sql
SELECT PULocationID, DOLocationID FROM `green-bedrock-450715-u0.yellow_taxi_2024.yellow_taxi_materialized`;
```

BigQuery does not duplicate columns in partitions unnecessarily. It only reads the requested columns.
BigQuery does not cache query results automatically unless you use BI Engine or Materialized Views.
There is no implicit join. BigQuery simply reads more columns but does not "join" them.


## Question 4: How many records have a fare_amount of 0? 

### Solution:
```sql
SELECT COUNT(fare_amount)  FROM `green-bedrock-450715-u0.yellow_taxi_2024.yellow_taxi_external`
WHERE fare_amount = 0 ;
```

## Question 5: What is the best strategy to make an optimized table in Big Query if your query will always filter based on tpep_dropoff_datetime and order the results by VendorID (Create a new table with this strategy) 

### Solution:
```sql
CREATE OR REPLACE TABLE `green-bedrock-450715-u0.yellow_taxi_2024.optimized_taxi_table`
PARTITION BY DATE(tpep_dropoff_datetime)  -- Partitioning on date for filtering efficiency
CLUSTER BY VendorID  -- Clustering on VendorID for efficient ordering
AS
SELECT * FROM `green-bedrock-450715-u0.yellow_taxi_2024.yellow_taxi_materialized`;
```
Partitioning by tpep_dropoff_datetime would allow BigQuery to scan only relevant partitions instead of the entire table.
Clustering by VendorID allows ordering on this column.

## Question 6: Write a query to retrieve the distinct VendorIDs between tpep_dropoff_datetime 2024-03-01 and 2024-03-15 (inclusive). Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 5 and note the estimated bytes processed. What are these values? 


### Solution:

### SQL Query:

## Question 7: Where is the data stored in the External Table you created?
