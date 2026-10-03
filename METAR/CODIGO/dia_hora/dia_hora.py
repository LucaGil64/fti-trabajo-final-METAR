from automathon import DFA
import string

# 1. Estados definidos para las bifurcaciones
q = {
    'q0', 
    'q_dia_0', 'q_dia_12', 'q_dia_3',  # Ramas para la unidad del día
    'q_hora', 'q_hora_01', 'q_hora_2', # Ramas para la unidad de la hora
    'q_min', 'q_min_dec',              # Ramas para el minuto
    'q_z', 'q_final'                   # Cierre
}

sigma = set(string.digits).union({'Z'})

# 2. Transiciones con validación de rangos
delta = {
    # DÍA (01-31)
    'q0': {
        '0': 'q_dia_0',
        '1': 'q_dia_12', '2': 'q_dia_12',
        '3': 'q_dia_3'
    },
    'q_dia_0':  {str(n): 'q_hora' for n in range(1, 10)}, # Si empieza con 0, acepta 1-9
    'q_dia_12': {str(n): 'q_hora' for n in range(10)},    # Si empieza con 1 o 2, acepta 0-9
    'q_dia_3':  {'0': 'q_hora', '1': 'q_hora'},           # Si empieza con 3, acepta 0-1

    # HORA (00-23)
    'q_hora': {
        '0': 'q_hora_01', '1': 'q_hora_01',
        '2': 'q_hora_2'
    },
    'q_hora_01': {str(n): 'q_min' for n in range(10)},    # Si empieza con 0 o 1, acepta 0-9
    'q_hora_2':  {str(n): 'q_min' for n in range(4)},     # Si empieza con 2, acepta 0-3

    # MINUTOS (00-59)
    'q_min': {str(n): 'q_min_dec' for n in range(6)},     # Acepta 0-5 para la decena
    'q_min_dec': {str(n): 'q_z' for n in range(10)},      # Acepta 0-9 para la unidad

    # LETRA Z (Obligatoria)
    'q_z': {'Z': 'q_final'},
    'q_final': {}
}

initial_state = 'q0'
f = {'q_final'}

modulo_dia_hora = DFA(q, sigma, delta, initial_state, f)
modulo_dia_hora.view("Grafo_Dia_Hora")
print("¡Grafo del módulo Día y Hora generado con validación estricta!")