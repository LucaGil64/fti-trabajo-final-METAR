from automathon import DFA
import string

# Definimos los estados para la temperatura, la barra separadora y el punto de rocío
q = {
    'q0', 
    'q_temp_m', 'q_temp_1', 'q_temp_2',  # Primera parte (Temperatura)
    'q_barra',                           # Separador '/'
    'q_rocio_m', 'q_rocio_1', 'q_final'  # Segunda parte (Punto de rocío)
}

numeros = set(string.digits)
sigma = numeros.union({'M', '/'})

delta = {
    # --- PARTE 1: TEMPERATURA ---
    # Desde el inicio, puede leer una 'M' (bajo cero) o ir directo a los números (sobre cero)
    'q0': {
        'M': 'q_temp_m',
        **{n: 'q_temp_1' for n in numeros}
    },
    # Si leyó la 'M', ahora está obligado a leer el primer número
    'q_temp_m': {n: 'q_temp_1' for n in numeros},
    # Segundo número de la temperatura
    'q_temp_1': {n: 'q_temp_2' for n in numeros},
    
    # --- SEPARADOR ---
    'q_temp_2': {'/': 'q_barra'},
    
    # --- PARTE 2: PUNTO DE ROCÍO ---
    # La misma lógica: puede leer una 'M' o ir directo al número
    'q_barra': {
        'M': 'q_rocio_m',
        **{n: 'q_rocio_1' for n in numeros}
    },
    'q_rocio_m': {n: 'q_rocio_1' for n in numeros},
    # Último número y fin
    'q_rocio_1': {n: 'q_final' for n in numeros},
    
    'q_final': {}
}

initial_state = 'q0'
f = {'q_final'}

modulo_temperatura = DFA(q, sigma, delta, initial_state, f)
modulo_temperatura.view("Grafo_Temperatura")
print("¡Grafo del módulo Temperatura generado exitosamente!")