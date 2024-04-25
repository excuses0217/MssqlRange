from flask import Flask, request
import pyodbc

app = Flask(__name__)
connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=db;DATABASE=test;UID=sa;PWD=p@ssw0rd123'

@app.route('/')
def index():
    product_id = request.args.get('id', '')

    # Check if 'id' parameter is provided
    if not product_id:
        return "Welcome to MssqlRange.Please provide 'id' parameter."

    query = f"SELECT * FROM product WHERE id = {product_id}"
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    if row:
        return f'ID: {row.id}, Name: {row.name}, Price: {row.price}, Description: {row.description}'
    else:
        return "No product found with the given ID."


if __name__ == '__main__':
    app.run(host='0.0.0.0')
