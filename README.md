# Proyecto Flask con MySQL

Este proyecto utiliza **Flask** y **MySQL**. A continuación se muestran los pasos para configurar y ejecutar el entorno correctamente.

---

## 🚀 Pasos para ejecutar el proyecto

### 1️⃣ Crear un entorno virtual
En Windows:
```bash
python -m venv venv
```

### 2️⃣ Activar el entorno virtual
```bash
venv\Scripts\activate
```

### 3️⃣ Instalar los paquetes
Con el entorno virtual activado, instala las dependencias desde el archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4️⃣ Crear el archivo `.env`
En la raíz del proyecto, crea un archivo llamado `.env` y define las siguientes variables:
```env
DB_HOST=localhost
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=tu_base_de_datos
```

### 5️⃣ Ejecutar el proyecto
Inicia el servidor con:
```bash
python app.py
```

---

### 🔴 Desactivar el entorno virtual

Cuando termines de trabajar en el proyecto, puedes salir del entorno virtual ejecutando:

```bash
deactivate