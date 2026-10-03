from automathon import DFA

# 1. Definimos los estados: inicio, 4 intermedios y el final
q = {'q0', 'q1', 'q2', 'q3', 'q4', 'q_final'}

# 2. El alfabeto son exactamente las 5 letras de la palabra
sigma = {'C', 'A', 'V', 'O', 'K'}

# 3. Transiciones: ruta directa y obligatoria
delta = {
    'q0': {'C': 'q1'},
    'q1': {'A': 'q2'},
    'q2': {'V': 'q3'},
    'q3': {'O': 'q4'},
    'q4': {'K': 'q_final'},
    'q_final': {}
}

initial_state = 'q0'
f = {'q_final'}

# Construcción y dibujo
modulo_cavok = DFA(q, sigma, delta, initial_state, f)
modulo_cavok.view("Grafo_CAVOK_Solo")
print("¡Grafo individual de CAVOK generado exitosamente!")