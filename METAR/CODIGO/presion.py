from automathon import DFA
import string

# 1. Definimos los estados (Letra y 4 pasos numéricos)
q = {'q0', 'q_num1', 'q_num2', 'q_num3', 'q_num4', 'q_final'}

# 2. El alfabeto ahora usa el set de dígitos de string
numeros = set(string.digits)
sigma = numeros.union({'A', 'Q'})

# 3. Transiciones limpias
delta = {
    # Bifurcación inicial para la unidad de medida
    'q0': {
        'A': 'q_num1',
        'Q': 'q_num1'
    },
    
    # Pasillo lineal de 4 dígitos (se acepta cualquier número del 0 al 9 en cada paso)
    'q_num1': {n: 'q_num2' for n in numeros},  # 1er dígito
    'q_num2': {n: 'q_num3' for n in numeros},  # 2do dígito
    'q_num3': {n: 'q_num4' for n in numeros},  # 3er dígito
    'q_num4': {n: 'q_final' for n in numeros}, # 4to dígito
    
    'q_final': {}
}

initial_state = 'q0'
f = {'q_final'}

# Construcción
modulo_presion = DFA(q, sigma, delta, initial_state, f)