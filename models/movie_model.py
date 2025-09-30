from database import get_db
import mysql.connector

def get_movie_by_id(id):
    cursor = None
    conn= None
    
    try:
        conn= get_db()
        cursor= conn.cursor(dictionary=True)
        query= "SELECT * FROM peliculas WHERE id= %s;"
        cursor.execute(query, (id,))
        row= cursor.fetchone()
        return row
    except mysql.connector.Error as err:
        print("Error al traer pelicula por id", err)
        return None
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

#obtener pelilculas con filtros personalizados
def get_movies_filter(genre=None, year_from=None, year_to=None, min_rating=None, order_by=None, desc=None):
    conn = None
    cursor = None
    try:
        conn = get_db()
        query = "SELECT * FROM peliculas"
        cursor = conn.cursor(dictionary=True)
        parts = []
        params = []
        if genre:
            parts.append("genero = %s")
            params.append(genre)
        if year_from:
            parts.append("anio >= %s")
            params.append(year_from)
        if year_to:
            parts.append("anio <= %s")
            params.append(year_to)
        if min_rating:
            parts.append("rating >= %s")
            params.append(min_rating)
        # Si vienen filtros del where
        if parts:
            query += " WHERE " + " OR ".join(parts) 
            
        if order_by in ["titulo", "anio", "genero", "rating", "director"]:
            if bool(desc) == True:
                query += f" ORDER BY {order_by} DESC"
            else:
                query += f" ORDER BY {order_by}"
      
        print("Query a ejecutar:", query)
        cursor.execute(query, tuple(params))
        row = cursor.fetchall()
        return row
    except mysql.connector.Error as err:
        print("Error al traer peliculas por filtro", err)
        return []
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def create_movie(titulo, director, anio, raing, genero, imagen):
    conn = None
    cursor = None
    try:
        conn = get_db()
        cursor = conn.cursor()
        query = "INSERT INTO peliculas (titulo, director, anio, rating, genero, imagen) VALUES (%s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (titulo, director, anio, raing, genero, imagen))
        conn.commit()
        last_id = cursor.lastrowid
        return last_id
    except mysql.connector.Error as err:
        print("Error al crear pelicula", err)
        return None
    finally:
        if cursor: cursor.close()
        if conn: conn.close()