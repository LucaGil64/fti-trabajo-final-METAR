from automathon import DFA

# 1. Definimos los estados (Letra y 4 pasos numéricos)
q = {'q0', 'q_num1', 'q_num2', 'q_num3', 'q_num4', 'q_final'}

# 2. El alfabeto ahora usa la etiqueta agrupada para los números
sigma = {'0-9', 'A', 'Q'}

# 3. Transiciones limpias
delta = {
    # Bifurcación inicial para la unidad de medida
    'q0': {
        'A': 'q_num1',
        'Q': 'q_num1'
    },
    
    # Pasillo lineal de 4 dígitos usando la etiqueta limpia
    'q_num1': {'0-9': 'q_num2'},  # 1er dígito
    'q_num2': {'0-9': 'q_num3'},  # 2do dígito
    'q_num3': {'0-9': 'q_num4'},  # 3er dígito
    'q_num4': {'0-9': 'q_final'}, # 4to dígito
    
    'q_final': {}
}

initial_state = 'q0'
f = {'q_final'}

# Construcción y dibujo
modulo_presion = DFA(q, sigma, delta, initial_state, f)
modulo_presion.view("Grafo_Presion_Limpio")
print("¡Grafo de presión unificado y limpio generado exitosamente!")