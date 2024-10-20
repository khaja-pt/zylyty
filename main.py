import os
from cfonts import render

# Note: Do not rename this file, it must be the entry point of your application.

# Note 2: You must read from the following environment variables:
# ADMIN_API_KEY -> "The secret API key used to call the API endpoints (the Bearer token)"
# DB_HOST -> "The hostname of the database"
# DB_PORT -> "The port of the database"
# DB_USERNAME -> "The username of the database"
# DB_PASSWORD -> "The password of the database"
# DB_NAME -> "The name of the database"
# API_BASE_URL -> "The base URL of the API your project will connect to"

# Example:
ADMIN_API_KEY = os.getenv('ADMIN_API_KEY')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
API_BASE_URL = os.getenv('API_BASE_URL')

print(render('Hello ZYLYTY!', colors=['cyan', 'magenta'], align='center', font='3d'))
print(f"Admin API Key: {ADMIN_API_KEY}")
print(f"Database Host: {DB_HOST}")
print(f"Database Port: {DB_PORT}")
print(f"Database Username: {DB_USERNAME}")
print(f"Database Password: {DB_PASSWORD}")
print(f"Database Name: {DB_NAME}")
print(f"API Base URL: {API_BASE_URL}")

# Example main, modify at will
def main():
    # You can import the data here from API_BASE_URL, using the ADMIN_API_KEY!
    # (...)
    # Don't forget to print the following string after you import all the necessary data:
    print("ZYLYTY Data Import Completed [0, 0, 0]")

if __name__ == "__main__":
    main()
