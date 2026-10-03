from automathon import DFA

# Definimos los 10 estados necesarios: 1 inicial, 8 intermedios y 1 final (aceptación)
q = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q_final'}

# El alfabeto son las letras exactas que componen ambas palabras
sigma = {'M', 'E', 'T', 'A', 'R', 'S', 'P', 'C', 'I'}

# Diccionario de transiciones con la bifurcación inicial
delta = {
    'q0': {'M': 'q1', 'S': 'q5'},
    
    # Camino exclusivo para "METAR"
    'q1': {'E': 'q2'},
    'q2': {'T': 'q3'},
    'q3': {'A': 'q4'},
    'q4': {'R': 'q_final'},
    
    # Camino exclusivo para "SPECI"
    'q5': {'P': 'q6'},
    'q6': {'E': 'q7'},
    'q7': {'C': 'q8'},
    'q8': {'I': 'q_final'},
    
    # El estado final no tiene salidas en este módulo aislado
    'q_final': {}
}

initial_state = 'q0'
f = {'q_final'}

# Construcción del autómata
modulo_identificacion = DFA(q, sigma, delta, initial_state, f)

# Generación de la imagen del grafo
modulo_identificacion.view("Modulo_Identificacion")
print("Grafo del primer módulo generado exitosamente.")