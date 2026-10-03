from automathon import DFA

# 1. Definimos los estados: inicial, intermedios para cada palabra, y el final
q = {
    'q0', 
    'q1_c', 'q2_c',        # Camino COR
    'q1_a', 'q2_a', 'q3_a', # Camino AUTO
    'q1_n', 'q2_n',        # Camino NIL
    'q_final'
}

# 2. El alfabeto con las letras exactas necesarias
sigma = {'C', 'O', 'R', 'A', 'U', 'T', 'N', 'I', 'L'}

# 3. Diccionario de transiciones con bifurcación de 3 vías
delta = {
    # Bifurcación desde el inicio según la primera letra leída
    'q0': {'C': 'q1_c', 'A': 'q1_a', 'N': 'q1_n'},
    
    # Ruta estricta para formar "COR"
    'q1_c': {'O': 'q2_c'},
    'q2_c': {'R': 'q_final'},
    
    # Ruta estricta para formar "AUTO"
    'q1_a': {'U': 'q2_a'},
    'q2_a': {'T': 'q3_a'},
    'q3_a': {'O': 'q_final'},
    
    # Ruta estricta para formar "NIL"
    'q1_n': {'I': 'q2_n'},
    'q2_n': {'L': 'q_final'},
    
    'q_final': {}
}

initial_state = 'q0'
f = {'q_final'}

# Construcción y dibujo
modulo_mods = DFA(q, sigma, delta, initial_state, f)
modulo_mods.view("Grafo_Modificadores")
print("¡Grafo del módulo Modificadores generado exitosamente!")