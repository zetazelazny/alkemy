from decouple import config

host = config('MYSQL_HOST')
port = config('MYSQL_PORT')
user = config('MYSQL_USER')
password = config('MYSQL_PASSWORD')
database = config('MYSQL_DB')

print (f"Host: {host}")
print (f"Port: {port}")
print (f"User: {user}")
print (f"Password: {password}")
print (f"Database: {database}")