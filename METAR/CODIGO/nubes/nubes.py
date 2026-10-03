from automathon import DFA
import string

q = {
    'q0',
    # Estados para coberturas estándar y SKC (comparten la S)
    'q_f1', 'q_f2',            
    'q_s1', 'q_sc1', 'q_sk1',  
    'q_b1', 'q_b2',            
    'q_o1', 'q_o2',            
    'q_v1',                    # VV (Visibilidad vertical)
    
    # Estados para códigos especiales (NSC, NCD, CLR)
    'q_n1', 'q_ns1', 'q_nc1',  
    'q_c1', 'q_cl1',           
    
    # Estados numéricos y sufijos opcionales
    'q_alt1', 'q_alt2', 'q_alt3', 'q_final_layer', 
    'q_cb1',                   # Para CB
    'q_tcu1', 'q_tcu2',        # Para TCU
    'q_sl1', 'q_sl2',          # Para ///
    'q_final_special'          # Estado final para códigos sin nubes
}

letras = set(string.ascii_uppercase)
numeros = set(string.digits)
sigma = letras.union(numeros).union({' ', '/'})

delta = {
    # Bifurcación inicial masiva
    'q0': {
        'F': 'q_f1', 'B': 'q_b1', 'O': 'q_o1', 
        'S': 'q_s1', 'V': 'q_v1', 'N': 'q_n1', 'C': 'q_c1'
    },
    
    # --- RUTAS DE 3 LETRAS + ALTITUD ---
    'q_f1': {'E': 'q_f2'}, 'q_f2': {'W': 'q_alt1'},          # FEW
    'q_b1': {'K': 'q_b2'}, 'q_b2': {'N': 'q_alt1'},          # BKN
    'q_o1': {'V': 'q_o2'}, 'q_o2': {'C': 'q_alt1'},          # OVC
    'q_v1': {'V': 'q_alt1'},                                 # VV
    
    # La letra 'S' bifurca en SCT (pide altitud) o SKC (estado final directo)
    'q_s1': {'C': 'q_sc1', 'K': 'q_sk1'},
    'q_sc1': {'T': 'q_alt1'},
    'q_sk1': {'C': 'q_final_special'},
    
    # --- RUTAS DE CÓDIGOS ESPECIALES ---
    # La letra 'N' bifurca en NSC o NCD
    'q_n1': {'S': 'q_ns1', 'C': 'q_nc1'},
    'q_ns1': {'C': 'q_final_special'},
    'q_nc1': {'D': 'q_final_special'},
    
    # CLR
    'q_c1': {'L': 'q_cl1'},
    'q_cl1': {'R': 'q_final_special'},
    
    # --- LECTURA DE ALTITUD (3 NÚMEROS) ---
    'q_alt1': {n: 'q_alt2' for n in numeros},
    'q_alt2': {n: 'q_alt3' for n in numeros},
    'q_alt3': {n: 'q_final_layer' for n in numeros},
    
    # --- SUFIJOS Y BUCLE MULTICAPA ---
    'q_final_layer': {
        ' ': 'q0',        # Vuelve al inicio para leer otra capa de nubes
        'C': 'q_cb1',     # Inicia sufijo CB
        'T': 'q_tcu1',    # Inicia sufijo TCU
        '/': 'q_sl1'      # Inicia sufijo ///
    },
    
    # Completando los sufijos (todos vuelven a q_final_layer para permitir el bucle)
    'q_cb1': {'B': 'q_final_layer'},
    'q_tcu1': {'C': 'q_tcu2'},
    'q_tcu2': {'U': 'q_final_layer'},
    'q_sl1': {'/': 'q_sl2'},
    'q_sl2': {'/': 'q_final_layer'},
    
    # Cierre de códigos especiales (sin salidas)
    'q_final_special': {}
}

initial_state = 'q0'
# Ambos estados finales son válidos de aceptación
f = {'q_final_layer', 'q_final_special'}

modulo_nubes = DFA(q, sigma, delta, initial_state, f)
modulo_nubes.view("Grafo_Nubes_Completo")
print("¡Grafo avanzado de nubes generado!")