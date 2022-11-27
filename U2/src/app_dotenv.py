from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

host = os.getenv('MYSQL_HOST')
port = os.getenv('MYSQL_PORT')
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
database = os.getenv('MYSQL_DB')

print (f"Host: {host}")
print (f"Port: {port}")
print (f"User: {user}")
print (f"Password: {password}")
print (f"Database: {database}")