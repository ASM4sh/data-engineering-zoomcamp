# Solution for `Module 1 Homework: Docker & SQL`

> This is the solution to the first homework for the 2025 cohort of **DE Zoomcamp**.  
> When submitting your homework, ensure to include a link to your GitHub repository or another public code-hosting platform.  
> This repository should contain the code used to solve the homework.  
> For homework that includes SQL or shell commands (instead of code files such as Python scripts), include the commands directly in the README file of your repository.

## Question 1: Understanding Docker First Run

### Task:
> Run Docker with the `python:3.12.8` image in interactive mode, using the entrypoint `bash`.  
> Identify the version of `pip` in the image.

#### Options:
- 24.3.1
- 24.2.1
- 23.3.1
- 23.2.1

### Solution:
By the time I started the course, I already had a basic understanding of Docker and had the Docker Desktop app installed. The first question of the homework was solved through the following steps:

1. **Running the Docker container**:  
   In **Windows Command Line**, I started the Docker container using the specified Python image by running the following command:
   
   ```bash
   docker run -it --entrypoint bash python:3.12.8
   ```

2. **Verifying the container:**:  
  After executing the command, I ensured to see the following prompt, indicating that I was inside the container:
   
   ```bash
   root@<my-container-id>:/#
   ```
3. **Checking pip version:**:  
  To check the **pip** version I ran the command:
   ```bash
   pip --version
   ```
   which displayed the exact version of **pip** in the image

## Question 2: Understanding Docker networking and docker-compose

### Task:
> Given the docker-compose.yaml, identify the hostname and port that pgadmin should use to connect to the postgres database.
#### Options:
- postgres:5433
- localhost:5432
- db:5433
- postgres:5432
- db:5432

In the provided .yaml file, two services are defined:
     - The `db` service uses the **`postgres:17-alpine`** image (PostgreSQL).
     - The `pgadmin` service uses the **`dpage/pgadmin4`** image (pgAdmin).
In Docker Compose, containers within the same network can refer to each other by their **service names**. The PostgreSQL container has the service name `db`, and this can be used as the **hostname** inside the Docker network.
However, as far as I am aware, container name can also be a valid option to access service container in an intercontainer network. In this case, the container name for the PostgreSQL container is **postgres**.
Regarding the port,  the `db` service is mapping port **5433** on the host to **5432** inside the container. In this case, pgAdmin should connect to the **internal port 5432** of the PostgreSQL container due to the port mapping internally within the network.

## Task: Prepare PostgreSQL and Load Data
For this task, I used the python script to load two provided datasets into Postgres. The Python script can be found [here](./load_data_to_postgres.py).


## Question 3: Trip Segmentation Count

### Task:
> During the period of **October 1st, 2019** (inclusive) and **November 1st, 2019** (exclusive), how many trips, respectively, happened in each of the following distance ranges:
> - Up to 1 mile
> - In between 1 (exclusive) and 3 miles (inclusive)
> - In between 3 (exclusive) and 7 miles (inclusive)
> - In between 7 (exclusive) and 10 miles (inclusive)
> - Over 10 miles

### Solution:
To answer this question, I used the following SQL Query:

```sql
SELECT
    CASE
        WHEN trip_distance <= 1 THEN 'Up to 1 mile'
        WHEN trip_distance > 1 AND trip_distance <= 3 THEN '1 to 3 miles'
        WHEN trip_distance > 3 AND trip_distance <= 7 THEN '3 to 7 miles'
        WHEN trip_distance > 7 AND trip_distance <= 10 THEN '7 to 10 miles'
        ELSE 'Over 10 miles'
    END AS distance_range,
    COUNT(*) AS trip_count
FROM green_tripdata_2019_10
WHERE
    lpep_pickup_datetime >= '2019-10-01'
    AND lpep_pickup_datetime < '2019-11-01'
    AND trip_distance IS NOT NULL  -- Ensure valid trip distances
GROUP BY distance_range
ORDER BY trip_count DESC;
```
where the **CASE** statement is used to categorize trips into the required distance ranges and the **WHERE** clause filters trips by dates. 
The result to the query can be found [here](images/Question3_Query.PNG)

When the query was executed, the results did not match any of the options stated in the problem. To ensure the accuracy of our results, we also performed the same calculations using pandas in a Jupyter Notebook.
The results were the same as the ones recieved with the query, so I chose the closes option of the provided. 

The Jupyter Notebook can be found [here](https://colab.research.google.com/drive/1IishWo1pE6CN-HyBtFl8anNxDD6iKKE8?usp=sharing))

