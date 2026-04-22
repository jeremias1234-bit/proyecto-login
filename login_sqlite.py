import sqlite3

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

while True:
    usuario = input("Usuario: ").strip()

    # Buscar usuario en la DB
    cursor.execute("SELECT contraseña FROM usuarios WHERE usuario = ?", (usuario,))
    resultado = cursor.fetchone()

    if resultado is None:
        print("Usuario inexistente")
        continue

    print("Usuario correcto")

    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:
        contraseña = input("Contraseña: ")

        if contraseña == resultado[0]:
            print("Acceso correcto")
            conexion.close()
            break
        else:
            intentos += 1
            print(f"Incorrecta. Te quedan {max_intentos - intentos} intentos")

    print("Usuario bloqueado")
    break
