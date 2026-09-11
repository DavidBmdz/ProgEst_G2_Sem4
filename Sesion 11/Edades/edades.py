#Registro de edades, clasificar si son niños, jovenes, adultos o ancianos y mostrar el mas joven y mas anciano

edades = []

edad_joven = 1000
edad_anciano = 0

def agregarEdad(edad):
    edades.append(edad)

def clasificarEdad(edad):
    while True:
        if edad <= 12:
            return "Niño"
        elif edad <= 17:
            return "Joven"
        elif edad <= 59:
            return "Adulto"
        elif edad >= 60:
            return "Anciano"
        else:
            return "Edad inválida"

def joven_anciano(edad):
    global edad_joven, edad_anciano
    if edad < edad_joven:
        edad_joven = edad
    if edad > edad_anciano:
        edad_anciano = edad

def registrarEdades():
    while True:
        try:
            edad = int(input("Ingrese una edad: "))
            if edad < 0 and edad > 150:
                print("Edad inválida. Intente nuevamente.")
            else:
                agregarEdad(edad)
                break

            