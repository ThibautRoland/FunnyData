import psycopg2

# Function to establish a connection to the PostgreSQL database
def create_connection():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="funnydatabase",
        user="thibaut",
        password="password"
    )
    return conn

# Function to retrieve all records from the database
def get_records(conn):
    sql = "SELECT * FROM conso_elec_gaz"
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print("residential_consumption:", row[0])
            print("number_residential_points:", row[1])
            print("quality_residential_index:", row[2])
            print("postal_code:", row[2])
            print("region_code:", row[2])
            print("-----------")
    except (Exception, psycopg2.Error) as error:
        print("Error retrieving records:", error)

# Main function
def main():
    # Create a connection to the database
    conn = create_connection()

    # Retrieve all records
    get_records(conn)

    # Close the connection
    conn.close()

# Execute the main function
if __name__ == '__main__':
    main()