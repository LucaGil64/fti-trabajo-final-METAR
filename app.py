import tkinter as tk 
from tkinter import messagebox 

# Importamos todos los módulos de autómatas adaptados a la nueva estructura de carpetas
from METAR.CODIGO.metar_speci import modulo_identificacion
from METAR.CODIGO.lugar import modulo_lugar
from METAR.CODIGO.dia_hora import modulo_dia_hora
from METAR.CODIGO.modificadores import modulo_mods
from METAR.CODIGO.viento_base import modulo_viento_base
from METAR.CODIGO.viento_variable import modulo_rango_variable
from METAR.CODIGO.visibilidad import modulo_vis
from METAR.CODIGO.cavok import modulo_cavok
from METAR.CODIGO.clima import modulo_clima
from METAR.CODIGO.nubes import modulo_nubes
from METAR.CODIGO.temperatura import modulo_temperatura
from METAR.CODIGO.presion import modulo_presion
from METAR.CODIGO.tendencias import modulo_tendencias

def analizar_metar():
    # 1. Obtenemos el reporte completo y lo dividimos por espacios
    reporte_completo = entrada_texto.get().strip().upper()
    
    if not reporte_completo:
        messagebox.showwarning("Advertencia", "Por favor, ingresa un código METAR.")
        return

    fragmentos = reporte_completo.split()
    
    # Limpiamos la caja de resultados
    caja_resultados.delete(1.0, tk.END)
    
    errores = 0

    # 2. Analizamos cada fragmento uno por uno
    for fragmento in fragmentos:
        tipo_identificado = "Desconocido / Inválido"
        
        # Evaluamos el fragmento contra los DFAs en orden de prioridad
        if modulo_identificacion.accept(fragmento):
            tipo_identificado = "Tipo de Reporte (METAR/SPECI)"
            
        elif modulo_cavok.accept(fragmento):
            tipo_identificado = "Condiciones CAVOK"
            
        elif modulo_mods.accept(fragmento):
            tipo_identificado = "Modificador (COR/AUTO/NIL)"
            
        elif modulo_tendencias.accept(fragmento):
            tipo_identificado = "Tendencia"
            
        elif modulo_dia_hora.accept(fragmento):
            tipo_identificado = "Día y Hora"
            
        elif modulo_viento_base.accept(fragmento):
            tipo_identificado = "Viento"
            
        elif modulo_rango_variable.accept(fragmento):
            tipo_identificado = "Viento Variable"
            
        elif modulo_temperatura.accept(fragmento):
            tipo_identificado = "Temperatura / Punto de Rocío"
            
        elif modulo_presion.accept(fragmento):
            tipo_identificado = "Presión (QNH/Altimetro)"
            
        elif modulo_nubes.accept(fragmento):
            tipo_identificado = "Nubosidad"
            
        elif modulo_clima.accept(fragmento):
            tipo_identificado = "Fenómeno Climático"
            
        elif modulo_vis.accept(fragmento):
            tipo_identificado = "Visibilidad"
            
        elif modulo_lugar.accept(fragmento):
            # Se evalúa casi al final porque son solo 4 letras y puede solaparse
            tipo_identificado = "Identificador de Estación (OACI)"
            
        else:
            errores += 1

        # 3. Imprimimos el resultado de este fragmento en la interfaz
        if tipo_identificado == "Desconocido / Inválido":
            caja_resultados.insert(tk.END, f"❌ [{fragmento}] -> NO RECONOCIDO\n")
        else:
            caja_resultados.insert(tk.END, f"✅ [{fragmento}] -> {tipo_identificado}\n")

    # 4. Mensaje final de estado
    caja_resultados.insert(tk.END, "-"*40 + "\n")
    if errores == 0:
        caja_resultados.insert(tk.END, "Veredicto: SINTAXIS METAR VÁLIDA.")
    else:
        caja_resultados.insert(tk.END, f"Veredicto: SE ENCONTRARON {errores} ERROR(ES).")

# Crear la ventana principal 
ventana = tk.Tk() 
ventana.title("Validador Completo METAR - FTI") 
ventana.geometry("700x550")  

etiqueta = tk.Label(ventana, text="Ingresa el reporte METAR completo:", font=("Arial", 14)) 
etiqueta.pack(pady=10)  

entrada_texto = tk.Entry(ventana, font=("Arial", 12), width=65)
entrada_texto.pack(pady=5)

boton = tk.Button(ventana, text="Analizar Reporte", command=analizar_metar, font=("Arial", 11), bg="lightblue") 
boton.pack(pady=10) 

# Usamos un widget Text para mostrar la lista desglosada
caja_resultados = tk.Text(ventana, font=("Courier", 11), height=20, width=65)
caja_resultados.pack(pady=10)

ventana.mainloop()