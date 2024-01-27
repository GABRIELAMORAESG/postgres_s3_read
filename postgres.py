
import psycopg2
import csv
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')

        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        cur.execute("SELECT * FROM users")

        #display numver of rows
        print("The number of parts: ", cur.rowcount)

        results = cur.fetchall()
        
        # Create a CSV writer
        with open("users_table.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([col[0] for col in cur.description])
            writer.writerows(results)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
