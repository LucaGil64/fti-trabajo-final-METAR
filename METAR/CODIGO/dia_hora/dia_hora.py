from automathon import DFA
import string

# 1. Estados para leer 6 números exactos y la letra Z
q = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q_final'}

numeros = set(string.digits)
sigma = numeros.union({'Z'})

# 2. Transiciones de avance lineal
delta = {
    'q0': {n: 'q1' for n in numeros},  # Día (decena)
    'q1': {n: 'q2' for n in numeros},  # Día (unidad)
    'q2': {n: 'q3' for n in numeros},  # Hora (decena)
    'q3': {n: 'q4' for n in numeros},  # Hora (unidad)
    'q4': {n: 'q5' for n in numeros},  # Minuto (decena)
    'q5': {n: 'q6' for n in numeros},  # Minuto (unidad)
    'q6': {'Z': 'q_final'},            # Letra Z obligatoria al final
    'q_final': {}
}

initial_state = 'q0'
f = {'q_final'}

modulo_dia_hora = DFA(q, sigma, delta, initial_state, f)
modulo_dia_hora.view("Grafo_Dia_Hora")
print("¡Grafo del módulo Día y Hora generado!")