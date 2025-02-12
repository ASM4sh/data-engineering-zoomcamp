# Solution for `Module 3 Homework: Data Warehouse`

> This is the solution to the fourth homework for the 2025 cohort of **DE Zoomcamp**.  
> For this homework the Yellow Taxi Trip Records for January 2024 - June 2024 are used. Parquet Files from the New York City Taxi Data were found here:
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
> The files were manually uploaded to GCS Bucket.
> ## BIG QUERY SETUP:
> To create external table using the uploaded data I ran the following query:
>```sql
   CREATE OR REPLACE TABLE green-bedrock-450715-u0.yellow_taxi_2024.native_yellow_taxi
AS(
  SELECT * FROM `green-bedrock-450715-u0.yellow_taxi_2024.yellow_taxi_external`
)
   ```

> To create materialized table using the uploaded data I ran the following query:
>```sql
   CREATE TABLE `green-bedrock-450715-u0.yellow_taxi_2024.yellow_taxi_materialized`
AS
SELECT * FROM `green-bedrock-450715-u0.yellow_taxi_2024.yellow_taxi_external`;
   ```
> In the code snippets above 'green-bedrock-450715-u0' is the name BigQuery console assigned automatically to the project.
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


## Question 3: 

### Task:

### Solution:


## Question 4: How many records have a fare_amount of 0? 

### Solution:
```sql
SELECT COUNT(DISTINCT PULocationID) AS distinct_pu_locations FROM `green-bedrock-450715-u0.yellow_taxi_2024.yellow_taxi_external`;
```

## Question 5: 



### Solution:


## Question 6: 


### Solution:

### SQL Query:

