import os
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv

load_dotenv()

def load_to_postgresql(df, table_name):
    """Loads transformed DataFrame into a PostgreSQL database securely."""
    connection = None
    cursor = None
    
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        cursor = connection.cursor()

        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id SERIAL PRIMARY KEY,
            date DATE UNIQUE,
            avg_temperature NUMERIC(5, 2),
            max_temperature NUMERIC(5, 2),
            min_temperature NUMERIC(5, 2),
            avg_humidity NUMERIC(5, 2)
        );
        """
        cursor.execute(create_table_query)

        insert_query = f"""
        INSERT INTO {table_name} (date, avg_temperature, max_temperature, min_temperature, avg_humidity)
        VALUES %s
        ON CONFLICT (date) DO UPDATE SET
            avg_temperature = EXCLUDED.avg_temperature,
            max_temperature = EXCLUDED.max_temperature,
            min_temperature = EXCLUDED.min_temperature,
            avg_humidity = EXCLUDED.avg_humidity;
        """
        
        # --- A CORREÇÃO ESTÁ AQUI ---
        # Interamos sobre o dataframe e usamos '.item()' para forçar 
        # a conversão de tipos NumPy (np.float64) para tipos nativos do Python
        values = []
        for row in df.itertuples(index=False, name=None):
            clean_row = tuple(val.item() if hasattr(val, 'item') else val for val in row)
            values.append(clean_row)
        # ----------------------------

        execute_values(cursor, insert_query, values)
        connection.commit()
        
        print(f"Data successfully loaded into PostgreSQL table: '{table_name}'.")

    except psycopg2.Error as error:
        print(f"Database error: {error}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()