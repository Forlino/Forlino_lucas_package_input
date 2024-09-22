def validate_number(numero, minimo, maximo):
    """Valida si un número está dentro de un rango."""
    return minimo <= numero <= maximo

def validate_length(cadena, longitud):
    """Valida si la longitud de la cadena es igual a la longitud esperada."""
    return len(cadena) == longitud