import random
from functools import reduce

def elegir_palabra():
    """Elige una palabra aleatoria de la lista."""
    palabras = ["python", "visual", "studio", "codigo", "programa""algoritmo", "depuracion", "variable", "funcion", "ciclo", 
    "bucle", "compilar", "sintaxis", "desarrollador", "interfaz", "clase", "objeto", "api", "git", "repositorio", "ide", "stack", 
    "framework", "servidor"]
    return random.choice(palabras)

def mostrar_progreso(palabra, letras_adivinadas):
    """Muestra la palabra con las letras adivinadas y guiones para las letras restantes."""
    return " ".join(map(lambda letra: letra if letra in letras_adivinadas else "_", palabra))

def validar_entrada(letras_intentadas):
    """Solicita una letra y valida que sea una sola letra del alfabeto y no repetida."""
    while True:
        letra = input("Ingresa una letra: ").lower()
        if len(letra) == 1 and letra.isalpha():
            if letra in letras_intentadas:
                print("Ya intentaste con esa letra.")
            else:
                return letra
        else:
            print("Entrada no válida. Ingresa solo una letra.")

def verificar_victoria(palabra, letras_adivinadas):
    """Verifica si todas las letras han sido adivinadas."""
    return set(palabra).issubset(letras_adivinadas)

def actualizar_intentos(letra, palabra, intentos):
    """Reduce el número de intentos si la letra no está en la palabra."""
    return intentos - 1 if letra not in palabra else intentos

def jugar():
    """Ejecuta la lógica principal del juego del ahorcado."""
    palabra = elegir_palabra()
    letras_adivinadas = set()
    letras_intentadas = set()
    intentos = 6
    
    print("Bienvenido al juego del ahorcado!")
    
    while intentos > 0:
        print("\nPalabra:", mostrar_progreso(palabra, letras_adivinadas))
        letra = validar_entrada(letras_intentadas)
        letras_intentadas.add(letra)
        
        if letra in palabra:
            letras_adivinadas.add(letra)
            if verificar_victoria(palabra, letras_adivinadas):
                print("Felicidades! Adivinaste la palabra:", palabra)
                break
        else:
            intentos = actualizar_intentos(letra, palabra, intentos)
            print(f"Incorrecto! Te quedan {intentos} intentos.")
    else:
        print("Perdiste! La palabra era:", palabra)

   # Pausa al final del juego
    input("Presiona Enter para salir...")

if __name__ == "__main__":
    jugar()
