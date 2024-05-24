"""
Código extraído y adaptado de la página:
https://es.stackoverflow.com/questions/51410/conversor-de-bases-decimal-binaria-hexadecimal-octal-en-python
"""

#Función de conversión entre sistemas numéricos
def convertir_numero(numero, base_origen, base_destino):
    numero_base10 = int(numero, base_origen)
    if base_destino == 2:
        return bin(numero_base10)[2:]
    elif base_destino == 3:
        return base_convert(numero_base10, 3)
    elif base_destino == 4:
        return base_convert(numero_base10, 4)
    elif base_destino == 8:
        return oct(numero_base10)[2:]
    elif base_destino == 10:
        return str(numero_base10)
    elif base_destino == 16:
        return hex(numero_base10)[2:].upper()
    else:
        raise ValueError("Base de destino no soportada")

def base_convert(numero, base):
    if numero == 0:
        return "0"
    digits = []
    while numero:
        digits.append(int(numero % base))
        numero = numero // base
    return ''.join(str(x) for x in digits[::-1])

#Función que convierte
def realizar_conversion(numero, s_origen, s_destino):
    base_origen = int(bases[s_origen])
    base_destino = int(bases[s_destino])
    try:
        resultado = convertir_numero(numero, base_origen, base_destino)
        return resultado
        salida.set(resultado)
    except ValueError as e:
        return e
        salida.set("Error: " + str(e))

#Crea diccionario de bases
bases = {"Binario": 2, "Ternario": 3, "Cuaternario": 4, "Octal": 8, "Decimal": 10, "Hexadecimal": 16}