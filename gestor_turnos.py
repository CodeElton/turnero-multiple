from areas_tienda import *

print("Bienvenido al Turnero Multiple!!")

def menu_opciones():
    while True:
        try:
            seleccion = int(input("Menu de Areas \n"
                                  " 1. Perfumeria \n"
                                  " 2. Farmacia \n"
                                  " 3. Cosmeticos \n"
                                  " 4. Salir \n"
                                  "Selecciona una opcion: "))

            if seleccion < 1 or seleccion > 4:
                print("Opción no válida. Debes elegir un número entre 1 y 4.")
            else:
                return seleccion
        except ValueError:
            print("Por favor ingresa un número válido.")


def inicializar_generadores():
    p = perfumeria()
    f = farmacia()
    c = cosmeticos()
    return p, f, c

def seleccion_area():
    p, f, c = inicializar_generadores()

    while True:
        opcion = menu_opciones()
        if opcion == 1:
            print(f"Su turno es el: P-{next(p)}")
        elif opcion == 2:
            print(f"Su turno es el: F-{next(f)}")
        elif opcion == 3:
            print(f"Su turno es el: C-{next(c)}")
        elif opcion == 4:
            break


seleccion_area()