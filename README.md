📊 Retail ETL Pipeline with Apache Airflow & PostgreSQL
🧠 Project Overview

This project is an end-to-end ETL pipeline built using Apache Airflow, Pandas, and PostgreSQL.
It automates data extraction from both a CSV file and a REST API, applies transformation and validation logic, and loads clean data into a PostgreSQL data warehouse using an incremental loading strategy.

🏗️ Architecture
CSV File        REST API
   │               │
   └── Extract Stage (Airflow Tasks)
                │
        Transform Stage (Pandas)
                │
        Validation Layer
                │
     Incremental Load (PostgreSQL)
                │
        Data Warehouse (Fact & Dim Tables)
⚙️ Technologies Used
Apache Airflow
Python
Pandas
PostgreSQL
Requests (API integration)
Docker (Astronomer Runtime)
Pytest (DAG testing)
🚀 DAG Workflow

The pipeline consists of two parallel workflows:

1. Sales Pipeline
Extract data from CSV
Clean and transform data
Validate schema and null values
Incrementally load into fact_sales
2. Products Pipeline
Extract data from external API
Normalize nested JSON structures
Validate product schema
Incrementally load into dim_products
🔄 ETL Steps
📥 Extract
Load CSV file from local directory
Fetch product data from API (dummyjson.com)
🔧 Transform
Standardize column names
Remove duplicates
Handle missing values
Convert data types
✅ Validate
Ensure required columns exist
Check for null values
Data integrity checks
📤 Load
Incremental loading (avoids duplicates)
PostgreSQL integration using Airflow Hooks
🧪 Testing

Includes automated DAG tests:

DAG import validation
Tag enforcement
Retry policy validation
📁 Project Structure
dags/
  retail_etl_dag.py

include/
  extract.py
  transform.py
  validate.py
  load_postgre.py
  data/

tests/
  test_dag_example.py
⚡ How to Run Locally
astro dev start

Then open:

http://localhost:8080
📌 Key Features
Incremental data loading
API retry mechanism
Modular ETL design
Parallel DAG execution
Production-like Airflow setup
Data validation layer
📈 Future Improvements
Add Spark for large-scale processing
Implement data quality dashboards
Add monitoring & alerting
Deploy on cloud (AWS / GCP)
Add CI/CD pipeline
👩‍💻 Author

Built by Ghada Rabea as part of a Data Engineering / Airflow learning project.
