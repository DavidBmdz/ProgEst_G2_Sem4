edad = []


def agregar(edad_nueva):
    edad.append(edad_nueva)


def mostrar():
    return edad


def clasificacion(edad):
    if edad < 0:
        return "Edad inválida"
    elif edad <= 13:
        return "Niño"
    elif edad <= 18:
        return "Adolescente"
    elif edad <= 65:
        return "Adulto"
    else:
        return "Adulto mayor"


def evaluar():
    if len(edad) == 0:
        print("Ingrese una edad primero")
    else:
        for e in edad:
            print(e, "-", clasificacion(e))


def mayor():
    if len(edad) == 0:
        return "Ingrese una edad primero"
    return max(edad)


def menor():
    if len(edad) == 0:
        return "Ingrese una edad primero"
    return min(edad)