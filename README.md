# 🔐 Sistema de Login con SQLite

Aplicación en Python que implementa un sistema de autenticación utilizando una base de datos SQLite.

## 🚀 Funcionalidades
- Validación de usuario y contraseña
- Control de intentos (máximo 3)
- Bloqueo tras múltiples intentos fallidos
- Persistencia de datos con SQLite

## 🛠️ Tecnologías utilizadas
- Python
- SQLite

## 📂 Estructura del proyecto

proyecto-login/

├── login.py  
├── init_db.py  
├── usuarios.db  
└── README.md  

## ▶️ Cómo ejecutar

1. Clonar el repositorio:

```bash
git clone https://github.com/jeremias1234-bit/proyecto-login.git
cd proyecto-login
```

2. Crear la base de datos (solo la primera vez):

```bash
python init_db.py
```

3. Ejecutar el sistema de login:

```bash
python login.py
```

## 📌 Notas
- Las contraseñas están almacenadas en texto plano (mejora futura: encriptación).
- Proyecto orientado a práctica de backend básico y manejo de bases de datos.

---

## 👨‍💻 Autor
Jeremías Scro
