base_de_datos = {
    "jere" : "1234",
    "carlitos" : "abcd",
    "manu123" : "234bcd",
    "jose" : "12345"
}

while True:
    usuario = input("Ingresa tu nombre de ususario: ").strip()
    if usuario in base_de_datos:
        print("Usuario correcto")
#####################################################################d
        intentos = 0
        max_intentos = 3

        while intentos < max_intentos:
            contraseña = input("Ingrese contraseña: ")
            if contraseña == base_de_datos[usuario]:
                print("Acceso concedido.")
                break

            else:
                intentos += 1
                restantes = max_intentos-intentos
                print(f"Contraseña incorrecta intenta nuevament.Te quedan {restantes} intentos")

        if intentos == max_intentos:
            print("Bloqueado")  
        break

    else:
        print("Usuario inexistente. Intente nuevamente")
