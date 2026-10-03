from automathon import DFA

# 1. Definimos los vocabularios exactos del manual
# Nota: Para la primera prueba dejé una selección representativa. 
# Una vez que veas cómo funciona, podés descomentar y agregar todas las demás 
# para obtener el validador definitivo.
intensidades = ['+', '-']
proximidades = ['RE', 'VC']
caracteristicas = ['BC', 'FZ', 'SH', 'TS'] # Podés sumar: 'DR', 'MI', 'PR', 'BL'
tipos = ['BR', 'DZ', 'FG', 'RA', 'SN', 'GR'] # Podés sumar: 'DS', 'DU', 'FC', 'FU', 'GS', 'HZ', 'IC', 'PE', 'PO', 'PY', 'SA', 'SG', 'SQ', 'SS', 'UP', 'VA'

valid_words = []

# 2. Motor de combinaciones: Construye todas las variantes legales del reporte
for t in tipos:
    valid_words.append(t) # Solo el tipo (ej: RA)
    for c in caracteristicas:
        valid_words.append(c + t) # Caract + Tipo (ej: SHRA)
        for i in intensidades + proximidades:
            valid_words.append(i + c + t) # Int/Prox + Caract + Tipo (ej: +SHRA)
    for i in intensidades + proximidades:
        valid_words.append(i + t) # Int/Prox + Tipo (ej: -RA)

# 3. Algoritmo Trie: Construcción dinámica del Autómata Determinista
q = {'q0'}
sigma = set()
delta = {'q0': {}}
f = set()

state_counter = 1

for word in valid_words:
    current = 'q0'
    for char in word:
        sigma.add(char)
        # Si el carácter no tiene un camino trazado, creamos un nuevo nodo
        if char not in delta[current]:
            new_state = f'q{state_counter}'
            state_counter += 1
            q.add(new_state)          # Registramos el nuevo estado
            delta[new_state] = {}     # Le preparamos sus salidas vacías
            delta[current][char] = new_state # Trazamos la flecha
        
        # Avanzamos el puntero al siguiente nodo
        current = delta[current][char]
    
    # El último estado al terminar una palabra válida es de aceptación
    f.add(current)

initial_state = 'q0'

# 4. Generación gráfica
modulo_clima = DFA(q, sigma, delta, initial_state, f)
modulo_clima.view("Grafo_Clima_Diccionario_Completo")

print(f"¡Grafo generado algorítmicamente con éxito!")
print(f"Python creó {len(q)} estados y {len(valid_words)} rutas válidas automáticamente.")