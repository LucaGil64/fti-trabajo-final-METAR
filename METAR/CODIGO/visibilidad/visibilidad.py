from automathon import DFA

q = {
    'q0',
    # Pasos numéricos
    'q_num1', 'q_num2', 'q_num3', 'q_num4',
    # Camino imperial (Fracciones y SM)
    'q_barra', 'q_denominador', 'q_s_letra', 'q_sm_final',
    # Caminos direccionales y NDV (se abren después de los 4 dígitos)
    'q_dir_n', 'q_dir_ne', 'q_dir_nw', 'q_nd', 'q_ndv',
    'q_dir_s', 'q_dir_se', 'q_dir_sw',
    'q_dir_e', 'q_dir_w'
}

sigma = {'0-9', '/', 'S', 'M', 'N', 'D', 'V', 'E', 'W'}

delta = {
    # Arranque: lee el primer número
    'q0': {'0-9': 'q_num1'},

    # Desde el primer o segundo número puede ir a fracciones o cerrar en SM (Ej: 3SM, 15SM, 3/4SM)
    'q_num1': {
        '0-9': 'q_num2',
        '/': 'q_barra',
        'S': 'q_s_letra'
    },
    'q_num2': {
        '0-9': 'q_num3',
        '/': 'q_barra',
        'S': 'q_s_letra'
    },
    'q_num3': {'0-9': 'q_num4'},

    # --- RUTA IMPERIAL (Millas / SM) ---
    'q_barra': {'0-9': 'q_denominador'},
    'q_denominador': {'S': 'q_s_letra'},
    'q_s_letra': {'M': 'q_sm_final'},

    # --- RUTA INTERNACIONAL (4 dígitos / Metros) ---
    # Al llegar a q_num4 (ej: 5000), puede terminar ahí o seguir hacia una dirección
    'q_num4': {
        'N': 'q_dir_n',
        'S': 'q_dir_s',
        'E': 'q_dir_e',
        'W': 'q_dir_w'
    },

    # Variantes del Norte y NDV
    'q_dir_n': {
        'E': 'q_dir_ne',
        'W': 'q_dir_nw',
        'D': 'q_nd'       # Para formar N-D-V
    },
    'q_nd': {'V': 'q_ndv'},

    # Variantes del Sur
    'q_dir_s': {
        'E': 'q_dir_se',
        'W': 'q_dir_sw'
    },

    # Estados finales cerrados (sin salidas)
    'q_sm_final': {}, 'q_ndv': {},
    'q_dir_ne': {}, 'q_dir_nw': {}, 'q_dir_se': {}, 'q_dir_sw': {},
    'q_dir_e': {}, 'q_dir_w': {}
}

initial_state = 'q0'

# Hay muchos estados válidos de aceptación: 
# Los 4 dígitos limpios, la ruta SM, y todas las direcciones cardinales.
f = {
    'q_num4', 'q_sm_final', 'q_ndv',
    'q_dir_n', 'q_dir_s', 'q_dir_e', 'q_dir_w', 
    'q_dir_ne', 'q_dir_nw', 'q_dir_se', 'q_dir_sw'
}

modulo_vis = DFA(q, sigma, delta, initial_state, f)
modulo_vis.view("Grafo_Visibilidad_Avanzada")
print("¡Grafo de visibilidad con normas ICAO y FAA generado!")