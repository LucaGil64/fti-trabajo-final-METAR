from automathon import DFA
import string

q = {
    'q0', 'q1_bajos', 'q1_alto', 'q2_cualquiera', 'q2_solo_cero',
    'q_letra_v', 'q_v_leida', 'q3_bajos', 'q3_alto', 'q4_cualquiera', 
    'q4_solo_cero', 'q_final'
}

numeros = set(string.digits)
sigma = numeros.union({'V'})

# Creamos listas para los rangos específicos
rango_0_2 = ['0', '1', '2']
rango_0_5 = ['0', '1', '2', '3', '4', '5']

delta = {
    'q0': {**{n: 'q1_bajos' for n in rango_0_2}, '3': 'q1_alto'},
    'q1_bajos': {n: 'q2_cualquiera' for n in numeros},
    'q1_alto': {**{n: 'q2_cualquiera' for n in rango_0_5}, '6': 'q2_solo_cero'},
    'q2_cualquiera': {n: 'q_letra_v' for n in numeros},
    'q2_solo_cero': {'0': 'q_letra_v'},
    
    'q_letra_v': {'V': 'q_v_leida'},
    
    'q_v_leida': {**{n: 'q3_bajos' for n in rango_0_2}, '3': 'q3_alto'},
    'q3_bajos': {n: 'q4_cualquiera' for n in numeros},
    'q3_alto': {**{n: 'q4_cualquiera' for n in rango_0_5}, '6': 'q4_solo_cero'},
    'q4_cualquiera': {n: 'q_final' for n in numeros},
    'q4_solo_cero': {'0': 'q_final'},
    
    'q_final': {}
}

initial_state = 'q0'
f = {'q_final'}
modulo_rango_variable = DFA(q, sigma, delta, initial_state, f)