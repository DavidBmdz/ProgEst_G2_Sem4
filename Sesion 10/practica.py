# Variable global
contador = 0


def incrementar_contador():
    global contador  # Permite modificar la variable global
    contador += 1
    print(f"Contador dentro de la función: {contador}")


print(f"Contador inicial: {contador}")
incrementar_contador()
incrementar_contador()
print(f"Contador final fuera de la función: {contador}")