# Import library
import requests
import pandas as pd
import mysql.connector

# Function to extract data from API 
def extract():
    url = 'https://www.fruityvice.com/api/fruit/all' # API link
    data = requests.get(url).json() # request API link in json format
    return(data)
data = extract()

# Function to transform json to dataframe format
def transform(data:dict):
    df = pd.json_normalize(data) # Change json format to dataframe
    pd.set_option('display.max_columns', None) # Display all of dataframe's column 
    return df
df = transform(data)

# Persiapkan data untuk .executemany()
data_to_insert = [tuple(row) for row in df.values] # Change format to be able for .executemany()
     
# Load the data to mysql database
mydb = mysql.connector.connect(
    host = 'mysql-1a320b02-marsasyauqi1-c710.a.aivencloud.com',
    user = 'avnadmin',
    password = 'AVNS_nPY2wbJt1qJj6nbAY-K',
    database = 'defaultdb',
    port = '11593'
)

# Name of columns at mysql database
sql = "INSERT INTO fruit (name, id, family, orders, genus, calories, fats, sugar, carbohydrates, protein) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

# Execute the .executemany()
try:
    cursor = mydb.cursor() # Allows Python code to execute SQL command in a database session
    cursor.executemany(sql, data_to_insert) # Prepares a database operation (query or command) and executes it against all parameter sequences or mappings found in the sequence
    mydb.commit() # Sends a COMMIT statement to the MySQL server, committing the current transaction
    print("Data berhasil dimasukkan ke MySQL!")
except mysql.connector.Error as e:
    print(f"Error: {e}")
finally:
    if mydb.is_connected():
        cursor.close()
        mydb.close()
        print("Koneksi ke MySQL ditutup.")
