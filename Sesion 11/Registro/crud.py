#Registro de estudiantes
"""
Registrar notas de n cantidad de estudiantes
"""

notas = []

def agregar(nota):
    notas.append(nota)

def mostrar():
    return(notas)

def evaluarNotas():
    for nota in notas:
        if nota >= 70:
            print(f"{nota}. Aprobado")
        else:
            print(f"{nota}. Reprobado")

