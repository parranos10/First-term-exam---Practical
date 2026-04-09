Laboratorio de Ciberseguridad: CRUD & Brute Force


Este proyecto implementa una API de gestión de usuarios y un script de prueba de penetración para demostrar la vulnerabilidad de credenciales débiles.


1. Ejecutar servidor: `python -m uvicorn main:app --reload`
2. Crear usuario víctima en `http://127.0.0.1:8000/docs`.
3. Ejecutar ataque: `python ataque.py`





aqui podemos evidenciar la cantidad de intentos, la contraseña, y el tiempo que tomo
<img width="574" height="84" alt="image" src="https://github.com/user-attachments/assets/fcc94697-e14f-4a83-939e-a8a7d4ce5818" />

en esta imagen se puede ver el ejemplo de los intentos que la contraseña fue erronea
<img width="556" height="174" alt="image" src="https://github.com/user-attachments/assets/f84f0f75-d606-4995-88d0-0fdf8b55cc02" />

