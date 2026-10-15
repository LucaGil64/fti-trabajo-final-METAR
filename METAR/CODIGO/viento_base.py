from automathon import DFA
import string

q = {
    'q0', 'q_dir1', 'q_dir2', 'q_dir3', 'q_vrb1', 'q_vrb2',
    'q_spd1', 'q_spd2', 'q_g1', 'q_g2', 'q_g_done',
    'q_k1', 'q_m1', 'q_m2', 'q_final'
}

numeros = set(string.digits) # Genera {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
sigma = numeros.union({'V', 'R', 'B', 'G', 'K', 'T', 'M', 'P', 'S', 'H'})

delta = {
    # Usamos **{...} para desempaquetar el diccionario de números y agregar la 'V'
    'q0': {**{n: 'q_dir1' for n in numeros}, 'V': 'q_vrb1'},
    'q_dir1': {n: 'q_dir2' for n in numeros},
    'q_dir2': {n: 'q_dir3' for n in numeros},
    'q_vrb1': {'R': 'q_vrb2'},
    'q_vrb2': {'B': 'q_dir3'},
    
    'q_dir3': {n: 'q_spd1' for n in numeros},
    'q_spd1': {n: 'q_spd2' for n in numeros},
    
    'q_spd2': {
        'G': 'q_g1', 
        'K': 'q_k1', 
        'M': 'q_m1'
    },
    'q_g1': {n: 'q_g2' for n in numeros},
    'q_g2': {n: 'q_g_done' for n in numeros},
    'q_g_done': {
        'K': 'q_k1', 
        'M': 'q_m1'
    },
    
    'q_k1': {'T': 'q_final'},
    'q_m1': {'P': 'q_m2'},
    'q_m2': {'S': 'q_final', 'H': 'q_final'},
    'q_final': {}
}

initial_state = 'q0'
f = {'q_final'}
modulo_viento_base = DFA(q, sigma, delta, initial_state, f)