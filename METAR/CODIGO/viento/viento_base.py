from automathon import DFA

q = {
    'q0',
    'q_dir1', 'q_dir2', 'q_dir3', 
    'q_vrb1', 'q_vrb2',
    'q_spd1', 'q_spd2',
    'q_g1', 'q_g2', 'q_g_done',
    'q_k1', 'q_m1', 'q_m2', 'q_final'
}

sigma = {'0-9', 'V', 'R', 'B', 'G', 'K', 'T', 'M', 'P', 'S', 'H'}

delta = {
    # 1. DIRECCIÓN (3 dígitos o VRB)
    'q0': {
        '0-9': 'q_dir1',
        'V': 'q_vrb1'
    },
    'q_dir1': {'0-9': 'q_dir2'},
    'q_dir2': {'0-9': 'q_dir3'},
    'q_vrb1': {'R': 'q_vrb2'},
    'q_vrb2': {'B': 'q_dir3'}, 
    
    # 2. VELOCIDAD BASE
    'q_dir3': {'0-9': 'q_spd1'},
    'q_spd1': {'0-9': 'q_spd2'},
    
    # 3. RÁFAGA (Opcional) o pase directo a unidades
    'q_spd2': {
        'G': 'q_g1', 
        'K': 'q_k1', 
        'M': 'q_m1'   
    },
    'q_g1': {'0-9': 'q_g2'},
    'q_g2': {'0-9': 'q_g_done'},
    'q_g_done': {
        'K': 'q_k1', 
        'M': 'q_m1'  
    },
    
    # 4. UNIDADES (KT, MPS, MPH)
    'q_k1': {'T': 'q_final'},
    'q_m1': {'P': 'q_m2'},
    'q_m2': {
        'S': 'q_final',
        'H': 'q_final'
    },
    
    'q_final': {}
}

initial_state = 'q0'
f = {'q_final'}

modulo_viento_base = DFA(q, sigma, delta, initial_state, f)
modulo_viento_base.view("Grafo_Viento_Base")
print("¡Grafo del viento principal generado!")