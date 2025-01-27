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
> Given thedocker-compose.yaml, identify the hostname and port that pgadmin should use to connect to the postgres database.
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

