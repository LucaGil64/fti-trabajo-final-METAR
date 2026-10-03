from automathon import DFA
import string

# 1. Definimos los estados: inicial, 3 intermedios y 1 final (aceptación tras 4 pasos)
q = {'q0', 'q1', 'q2', 'q3', 'q_final'}

# 2. El alfabeto son las 26 letras mayúsculas de la A a la Z
sigma = set(string.ascii_uppercase)

# 3. Transiciones generadas automáticamente para aceptar cualquier letra en cada paso
delta = {
    'q0': {letra: 'q1' for letra in sigma},      # Lee la 1ra letra
    'q1': {letra: 'q2' for letra in sigma},      # Lee la 2da letra
    'q2': {letra: 'q3' for letra in sigma},      # Lee la 3ra letra
    'q3': {letra: 'q_final' for letra in sigma}, # Lee la 4ta letra y finaliza
    'q_final': {}
}

initial_state = 'q0'
f = {'q_final'}

# Construcción y dibujo del autómata
modulo_lugar = DFA(q, sigma, delta, initial_state, f)
modulo_lugar.view("Grafo_Lugar")
print("¡Grafo del módulo Lugar generado exitosamente!")