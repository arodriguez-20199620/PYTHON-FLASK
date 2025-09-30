# Documentación de la API de Películas

Esta API permite gestionar y consultar películas en una base de datos MySQL usando Flask.

---

## Endpoints

### 1. Obtener película por ID

**GET** `/movies/<id>`

- **Descripción:** Devuelve los datos de una película específica por su ID.
- **Respuesta exitosa:**  
  ```json
  {
    "id": 1,
    "titulo": "Nombre",
    "director": "Director",
    "anio": 2020,
    "rating": 8.5,
    "genero": "Acción",
    "imagen": "url"
  }
  ```
- **Error:**  
  ```json
  { "error": "Pelicula no encontrada" }
  ```

---

### 2. Obtener películas por filtro

**GET** `/movies/`

- **Descripción:** Devuelve una lista de películas filtradas por género, año, rating, orden, etc.
- **Parámetros de consulta:**
  - `genre`: Género de la película
  - `year_from`: Año mínimo
  - `year_to`: Año máximo
  - `min_rating`: Rating mínimo
  - `order_by`: Campo para ordenar (`titulo`, `anio`, `genero`, `rating`, `director`)
  - `desc`: Si es `True`, orden descendente
- **Respuesta exitosa:**  
  ```json
  [
    { "id": 1, "titulo": "...", ... },
    { "id": 2, "titulo": "...", ... }
  ]
  ```
- **Error:**  
  ```json
  { "error": "No se encontraron peliculas con los filtros proporcionados" }
  ```

---

### 3. Crear nueva película

**POST** `/movies/`

- **Descripción:** Crea una nueva película en la base de datos.
- **Body (JSON):**
  ```json
  {
    "titulo": "Nombre",
    "director": "Director",
    "anio": 2020,
    "rating": 8.5,
    "genero": "Acción",
    "imagen": "url"
  }
  ```
- **Respuesta exitosa:**  
  ```json
  { "message": "Pelicula creada", "id": 3 }
  ```
- **Errores:**
  - Faltan datos obligatorios:
    ```json
    { "error": "Faltan datos obligatorios" }
    ```
  - Rating inválido:
    ```json
    { "error": "El rating debe ser un numero" }
    ```

---

## Ejemplo de uso

```bash
curl -X GET "http://localhost:5000/movies/1"
curl -X GET "http://localhost:5000/movies/?genre=Acción&min_rating=7"
curl -X POST "http://localhost:5000/movies/" -H "Content-Type: application/json" -d '{"titulo":"Matrix","director":"Wachowski","anio":1999,"rating":9,"genero":"Sci-Fi","imagen":"url"}'
```