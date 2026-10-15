from automathon import DFA
import string

q = {
    'q0', 'q_r', 'q_rw0', 'q_rw12', 'q_rw3', 'q_rw_num', 'q_rw_pos',
    'q_slash', 'q_v1', 'q_v2', 'q_v3', 'q_v4', 'q_tend'
}

numeros = set(string.digits)
sigma = numeros.union({'R', 'L', 'C', 'U', 'D', 'N', '/'})

delta = {
    'q0': {'R': 'q_r'},
    
    # Validación estricta del número de pista (01 a 36)
    'q_r': {
        '0': 'q_rw0',
        '1': 'q_rw12', '2': 'q_rw12',
        '3': 'q_rw3'
    },
    'q_rw0': {str(n): 'q_rw_num' for n in range(1, 10)}, # Acepta 01-09
    'q_rw12': {str(n): 'q_rw_num' for n in range(10)},   # Acepta 10-29
    'q_rw3': {str(n): 'q_rw_num' for n in range(7)},     # Acepta 30-36
    
    # Letra de posición opcional (L, C, R) o pase directo a la barra
    'q_rw_num': {
        'L': 'q_rw_pos', 'C': 'q_rw_pos', 'R': 'q_rw_pos',
        '/': 'q_slash'
    },
    'q_rw_pos': {'/': 'q_slash'},
    
    # 4 dígitos indicando visibilidad
    'q_slash': {n: 'q_v1' for n in numeros},
    'q_v1': {n: 'q_v2' for n in numeros},
    'q_v2': {n: 'q_v3' for n in numeros},
    'q_v3': {n: 'q_v4' for n in numeros},
    
    # Tendencia opcional final
    'q_v4': {
        'U': 'q_tend', 'D': 'q_tend', 'N': 'q_tend'
    },
    'q_tend': {}
}

initial_state = 'q0'
# Es válido terminar en los 4 dígitos o después de la letra de tendencia
f = {'q_v4', 'q_tend'} 

modulo_vis_pista = DFA(q, sigma, delta, initial_state, f)