import re

def calcular_operacion(operacion):
    try:
        # Evalúa la operación utilizando eval (asegúrate de que la entrada sea segura)
        resultado = eval(operacion)
        return resultado
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Calculadora básica en línea de comandos")
    print("Solo se permiten operaciones de suma y resta.")
    print("Escribe una operación (por ejemplo, 2 + 2) y presiona Enter para calcular.")
    print("Presiona 'c' para borrar la operación o 'q' para salir.")

    while True:
        operacion = input("> ")

        if operacion.lower() == 'c':
            print("Operación borrada. Escribe una nueva operación.")
            continue
        elif operacion.lower() == 'q':
            print("Saliendo de la calculadora...")
            break

        # Verificar si la operación es válida (solo números, +, -, y espacios)
        if not re.match(r'^[0-9+\- ]+$', operacion):
            print("Operación no válida. Solo se permiten números y operadores + y -.")
            continue

        resultado = calcular_operacion(operacion)
        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
