import edades


def menu():
    print("""
        1. Ingresar edad
        2. Mostrar edad
        3. Evaluar edad
        4. Mostrar edad mayor y menor
        0. Salir
        Digite una opcion valida:
        """)
    opcion = int(input())
    return opcion


def main():
    while True:
        op = menu()

        if op == 1:
            edad = int(input("Digite una edad: "))
            edades.agregar(edad)

        elif op == 2:
            if len(edades.mostrar()) == 0:
                print("Ingrese una edad primero")
            else:
                print(edades.mostrar())

        elif op == 3:
            edades.evaluar()

        elif op == 4:
            print("La edad mayor es:", edades.mayor())
            print("La edad menor es:", edades.menor())

        elif op == 0:
            print("Adios...")
            break

        else:
            print("Opcion invalida...")


main()