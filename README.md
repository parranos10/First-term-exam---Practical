Proyecto: API de Usuarios + Fuerza Bruta


Este proyecto consiste en una API REST desarrollada con FastAPI que permite gestionar usuarios mediante operaciones CRUD. Además, se implementa un script de fuerza bruta para probar la seguridad del endpoint de login.

se uso:
- Python
- FastAPI
- SQLModel
- Requests


iniciar api:
1. Instalar dependencias:
pip install fastapi uvicorn sqlmodel

Ejecutar el servidor:
uvicorn main:app --reload

Abrir en el navegador:
http://127.0.0.1:8000/docs
<img width="565" height="167" alt="image" src="https://github.com/user-attachments/assets/256e8ffd-a5b7-4e93-8a8b-5ce6b97399a2" />


Endpoints:
- POST /users → Crear usuario  
- GET /users → Listar usuarios  
- GET /users/{id} → Obtener usuario  
- PUT /users/{id} → Actualizar usuario  
- DELETE /users/{id} → Eliminar usuario  
- POST /login → Iniciar sesión  


Fuerza bruta
El archivo bruteForce.py realiza múltiples intentos de login probando diferentes contraseñas automáticamente hasta encontrar la correcta.

Ejecución:
python bruteForce.py
<img width="418" height="73" alt="image" src="https://github.com/user-attachments/assets/d282a2e4-b0aa-42a5-80ab-4c8c583c4230" />

