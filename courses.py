import sqlite3

params = {"course_professor": "Simon Scheidegger"}

def find_professor(params):
    query = 'SELECT * FROM courses'
    # Add filter clauses for each of the parameters
    if len(params) > 0:
        filters = ["{}=?".format(k) for k in params]
        query += " WHERE ".join(filters)
    # Create the tuple of values
    t = tuple(params.values())

    # Open connection to DB
    conn = sqlite3.connect("programmes.db")
    # Create a cursor
    c = conn.cursor()
    # Execute the query
    c.execute(query,t)
    # Return the results
    c.fetchall()

print(find_professor(params))