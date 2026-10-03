import psycopg2
import pandas as pd

# Database connection configuration
conn = psycopg2.connect(
    host="localhost",
    database="churn_db",
    user="postgres",
    password="Bonyunyu12!",
    port="5432"
)

# Fetch data using SQL query
query = "SELECT * FROM customers WHERE churn_risk_score > 0.50;"
df = pd.read_sql_query(query, conn)

# Print database records in terminal
print("High Risk Churn Customers:")
print(df)

conn.close()