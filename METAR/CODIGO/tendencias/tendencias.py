from automathon import DFA

# 1. Definimos los estados para todos los caminos
q = {
    'q0',
    'q_b1', 'q_b2', 'q_b3', 'q_b4',         # Ruta BECMG
    'q_t1', 'q_t2', 'q_t3', 'q_t4',         # Ruta TEMPO / TL
    'q_p1', 'q_p2', 'q_p3', 'q_p4', 'q_p5', # Ruta PROB30 / PROB40
    'q_f1',                                 # Ruta FM
    'q_a1',                                 # Ruta AT
    'q_final'
}

# 2. Alfabeto con las letras y números involucrados
sigma = {'B', 'E', 'C', 'M', 'G', 'T', 'P', 'O', 'R', '3', '4', '0', 'F', 'L', 'A'}

# 3. Transiciones
delta = {
    # Bifurcación inicial según la primera letra
    'q0': {'B': 'q_b1', 'T': 'q_t1', 'P': 'q_p1', 'F': 'q_f1', 'A': 'q_a1'},

    # Camino BECMG (Permanente)
    'q_b1': {'E': 'q_b2'}, 'q_b2': {'C': 'q_b3'},
    'q_b3': {'M': 'q_b4'}, 'q_b4': {'G': 'q_final'},

    # Caminos TEMPO (Temporal) y TL (Hasta)
    'q_t1': {
        'E': 'q_t2',       # Sigue hacia TEMPO
        'L': 'q_final'     # Cierra en TL
    }, 
    'q_t2': {'M': 'q_t3'}, 'q_t3': {'P': 'q_t4'}, 'q_t4': {'O': 'q_final'},

    # Caminos PROB30 y PROB40 (Probabilidad)
    'q_p1': {'R': 'q_p2'}, 'q_p2': {'O': 'q_p3'}, 'q_p3': {'B': 'q_p4'},
    'q_p4': {
        '3': 'q_p5',       # Sigue hacia 30
        '4': 'q_p5'        # Sigue hacia 40
    },
    'q_p5': {'0': 'q_final'},

    # Camino FM (Desde)
    'q_f1': {'M': 'q_final'},

    # Camino AT (A las)
    'q_a1': {'T': 'q_final'},

    'q_final': {}
}

initial_state = 'q0'
f = {'q_final'}

# Construcción y dibujo
modulo_tendencias = DFA(q, sigma, delta, initial_state, f)
modulo_tendencias.view("Grafo_Tendencias")
print("¡Grafo del módulo Tendencias generado exitosamente!")