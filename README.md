# Configuración del Backend

Esta guía te ayudará a configurar y ejecutar el servidor backend del proyecto.

## Prerrequisitos

- Python 3.x instalado y agregado al PATH.

## Instalación y Configuración

1.  **Navega a la carpeta del backend:**
    Si no te encuentras en la carpeta `backend`, navega hacia ella.
    ```bash
    cd backend
    ```

2.  **Crea y activa un entorno virtual:**

    Abre tu terminal en la carpeta `backend` y ejecuta los siguientes comandos. Esto creará una carpeta para el entorno virtual llamada `venv`.

    *   **Para Windows:**
        ```bash
        # Crear el entorno virtual
        py -m venv venv

        # Activar el entorno virtual
        .\venv\Scripts\activate
        ```

    *   **Para macOS/Linux:**
        ```bash
        # Crear el entorno virtual
        python3 -m venv venv

        # Activar el entorno virtual
        source venv/bin/activate
        ```

3.  **Instala las dependencias:**

    Instala todos los paquetes necesarios desde el archivo `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplica las migraciones de la base de datos:**

    Este comando configurará las tablas necesarias en la base de datos.

    ```bash
    python manage.py migrate
    ```

5.  **Ejecuta el servidor de desarrollo:**

    Finalmente, inicia el servidor de desarrollo de Django.

    ```bash
    python manage.py runserver
    ```

    El servidor estará disponible en `http://127.0.0.1:8000/`. Ahora puedes acceder a la aplicación desde tu navegador web.
