from automathon import DFA

q = {'q0', 'q1'}
sigma = {'0', '1'}
delta = {
    'q0': {'0': 'q0', '1': 'q1'},
    'q1': {'0': 'q1', '1': 'q0'}
}
initial_state = 'q0'
f = {'q1'}

mi_automata = DFA(q, sigma, delta, initial_state, f)

# Esta línea es la que da la orden de crear el archivo de imagen
mi_automata.view("PrimerDibujo")
print("¡El código se ejecutó bien y la imagen debería estar lista!")