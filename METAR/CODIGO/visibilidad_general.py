from automathon import DFA
import string

# Estados basados en el grafo de Visibilidad general
q = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8'}

numeros = set(string.digits)
sigma = numeros.union({'S', 'M', '/'})

delta = {
    'q0': {n: 'q1' for n in numeros},
    
    # Desde q1 puede ir a q2 (más números), q7 (letra S) o q5 (fracción)
    'q1': {
        **{n: 'q2' for n in numeros},
        'S': 'q7',
        '/': 'q5'
    },
    
    # Desde q2 puede ir a q3 (hacia los 4 dígitos) o q7 (letra S)
    'q2': {
        **{n: 'q3' for n in numeros},
        'S': 'q7'
    },
    
    'q3': {n: 'q4' for n in numeros}, # 4to dígito, fin de metros
    
    # Ruta de fracciones
    'q5': {n: 'q6' for n in numeros},
    'q6': {
        **{n: 'q8' for n in numeros},
        'S': 'q7'
    },
    'q8': {'S': 'q7'},
    
    # Cierre de Millas (SM)
    'q7': {'M': 'q4'},
    'q4': {}
}

initial_state = 'q0'
f = {'q4'} # El único estado de aceptación es q4 para ambos caminos

modulo_vis_general = DFA(q, sigma, delta, initial_state, f)