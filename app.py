from flask import Flask
import psycopg2

#RDS connection parameters
ENDPOINT= "database-1.cfgug4m84026.us-east-1.rds.amazonaws.com"
PORT= "5432"
USER= "postgres"
PASSWORD = "Student11"
REGION= "us-east-1"
DBNAME= "postgres"

app=Flask(__name__)

@app.route("/")

def index():
    return "index"

@app.route('/students')
def get_students():
    #gets the credentials from .aws/credentials
    try:
        conn = psycopg2.connect(host=ENDPOINT, port=PORT, database=DBNAME, user=USER, password=PASSWORD)
        cur = conn.cursor()
        cur.execute("""SELECT * from test""")
        query_results = cur.fetchall()
        print(query_results)
        return(query_results)
    except Exception as e:
        print("Database connection failed due to {}".format(e)) 
        return("Database connection failed due to {}".format(e))

if __name__ == "__main__":
    app.run(debug=True)