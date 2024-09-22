from Package_Input.Input import get_int, get_float, get_string

if __name__ == "__main__":
    resultado_int = get_int("Introduce un número entero (1-10): ", "Error, fuera de rango.", 1, 10, 3)
    resultado_float = get_float("Introduce un número decimal (1.0-10.0): ", "Error, fuera de rango.", 1.0, 10.0, 3)
    resultado_string = get_string(5)  

    print(f"Número entero: {resultado_int}")
    print(f"Número decimal: {resultado_float}")
    print(f"Cadena ingresada: {resultado_string}")




