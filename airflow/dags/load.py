import json
import psycopg2
def load(json_data):
# Define your PostgreSQL database connection parameters
    conn = psycopg2.connect(
        host= "localhost",
        database= "spotiflow_tracks",
        user= "postgres",
        password= "postgres",
    )
    cur = conn.cursor()

    # Define the SQL query to create the table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS top_50_tracks (
        name VARCHAR,
        artist VARCHAR,
        album VARCHAR,
        explicit BOOLEAN,
        duration_ms INTEGER,
        url VARCHAR,
        extracted_date DATE,
        danceability FLOAT,
        energy FLOAT,
        key INTEGER,
        loudness FLOAT,
        mode INTEGER,
        speechiness FLOAT,
        acousticness FLOAT,
        instrumentalness FLOAT,
        liveness FLOAT,
        valence FLOAT,
        tempo FLOAT,
        id VARCHAR PRIMARY KEY,
        time_signature INTEGER
    )
    """

    # Execute the create table query
    cur.execute(create_table_query)

    # Commit the table creation
    conn.commit()

    # Your JSON data
    
    # Insert data into the table
    for data in json_data:
        insert_query = """
        INSERT INTO top_50_tracks (name, artist, album, explicit, duration_ms, url, extracted_date, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, id, time_signature)
        VALUES (%(name)s, %(artist)s, %(album)s, %(explicit)s, %(duration_ms)s, %(url)s, %(extracted_date)s, %(danceability)s, %(energy)s, %(key)s, %(loudness)s, %(mode)s, %(speechiness)s, %(acousticness)s, %(instrumentalness)s, %(liveness)s, %(valence)s, %(tempo)s, %(id)s, %(time_signature)s)
        """
        
        cur.execute(insert_query, data)

    # Commit the changes and close the cursor and connection
    conn.commit()
    cur.close()
    conn.close()