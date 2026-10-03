from automathon import DFA

q = {
    'q0', 
    'q1_bajos', 'q1_alto', 'q2_cualquiera', 'q2_solo_cero',
    'q_letra_v', 'q_v_leida',
    'q3_bajos', 'q3_alto', 'q4_cualquiera', 'q4_solo_cero',
    'q_final'
}

# El alfabeto incluye las agrupaciones exactas que necesitamos para los límites
sigma = {'0-2', '3', '0-5', '6', '0-9', '0', 'V'}

delta = {
    # --- PRIMER ÁNGULO (000 a 360) ---
    'q0': {
        '0-2': 'q1_bajos',  # Si empieza con 0, 1 o 2, va holgado
        '3': 'q1_alto'      # Si empieza con 3, entra al camino estricto
    },
    
    # Camino holgado (ej: 299)
    'q1_bajos': {'0-9': 'q2_cualquiera'},
    
    # Camino estricto (ej: 359 o 360)
    'q1_alto': {
        '0-5': 'q2_cualquiera', # Permite hasta 35_
        '6': 'q2_solo_cero'     # Si llega a 36_, lo obliga a que el último sea 0
    },
    
    # Cierre del primer ángulo
    'q2_cualquiera': {'0-9': 'q_letra_v'},
    'q2_solo_cero': {'0': 'q_letra_v'},
    
    # --- LETRA V (Separador) ---
    'q_letra_v': {'V': 'q_v_leida'},
    
    # --- SEGUNDO ÁNGULO (000 a 360) ---
    # Aplica exactamente la misma lógica restrictiva
    'q_v_leida': {
        '0-2': 'q3_bajos',
        '3': 'q3_alto'
    },
    'q3_bajos': {'0-9': 'q4_cualquiera'},
    'q3_alto': {
        '0-5': 'q4_cualquiera',
        '6': 'q4_solo_cero'
    },
    'q4_cualquiera': {'0-9': 'q_final'},
    'q4_solo_cero': {'0': 'q_final'},
    
    'q_final': {}
}

initial_state = 'q0'
f = {'q_final'}

modulo_rango_variable = DFA(q, sigma, delta, initial_state, f)
modulo_rango_variable.view("Grafo_Viento_Variable_Limitado")
print("¡Grafo de rango variable (máximo 360) generado exitosamente!")