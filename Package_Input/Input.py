from .Validate import validate_number, validate_length

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    for intento in range(reintentos):
        try:
            numero = int(input(mensaje))
            if validate_number(numero, minimo, maximo):
                return numero
            else:
                print(mensaje_error)
        except ValueError:
            print(mensaje_error)
    return None

def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> float | None:
    for intento in range(reintentos):
        try:
            numero = float(input(mensaje))
            if validate_number(numero, minimo, maximo):
                return numero
            else:
                print(mensaje_error)
        except ValueError:
            print(mensaje_error)
    return None

def get_string(longitud: int) -> str | None:
    while True:
        cadena = input(f"Introduce una cadena de longitud {longitud}: ")
        if validate_length(cadena, longitud):
            return cadena
        else:
            print(f"Error: La cadena debe tener exactamente {longitud} caracteres. Inténtalo de nuevo.")
