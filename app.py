import tkinter as tk
from tkinter import messagebox
import re

# Importamos las 4 funciones de dibujo
from graficos import dibujar_brujula, dibujar_termometro, dibujar_presion, dibujar_grafico_nubes

from METAR.CODIGO.metar_speci import modulo_identificacion
from METAR.CODIGO.lugar import modulo_lugar
from METAR.CODIGO.dia_hora import modulo_dia_hora
from METAR.CODIGO.modificadores import modulo_mods
from METAR.CODIGO.viento_base import modulo_viento_base
from METAR.CODIGO.viento_variable import modulo_rango_variable
from METAR.CODIGO.visibilidad_general import modulo_vis_general
from METAR.CODIGO.visibilidad_pista import modulo_vis_pista
from METAR.CODIGO.cavok import modulo_cavok
from METAR.CODIGO.clima import modulo_clima
from METAR.CODIGO.nubes import modulo_nubes
from METAR.CODIGO.temperatura import modulo_temperatura
from METAR.CODIGO.presion import modulo_presion
from METAR.CODIGO.tendencias import modulo_tendencias

def abrir_ventana_graficos(datos_graficos, fragmentos):
    ventana_graf = tk.Toplevel(ventana)
    ventana_graf.title("Dashboard Visual METAR")
    ventana_graf.state('zoomed') 
    ventana_graf.configure(bg="#004d80") # Un azul apenitas más oscuro de fondo general

    canvas = tk.Canvas(ventana_graf, bg="#004d80", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)
    
    # ---------------------------------------------------------
    # FUNCIÓN INTERNA: Dibuja un panel con bordes redondeados
    # ---------------------------------------------------------
    def dibujar_tarjeta(x1, y1, x2, y2, color_fondo, titulo):
        radio = 15
        canvas.create_polygon(
            x1+radio, y1, x2-radio, y1, x2, y1+radio, x2, y2-radio, 
            x2-radio, y2, x1+radio, y2, x1, y2-radio, x1, y1+radio,
            fill=color_fondo, outline="", smooth=True
        )
        # Línea divisoria y título de la tarjeta
        canvas.create_line(x1 + 10, y1 + 35, x2 - 10, y1 + 35, fill="#003355")
        canvas.create_text((x1+x2)/2, y1 + 18, text=titulo, fill="white", font=("Arial", 11, "bold"))

    # ---------------------------------------------------------
    # 1. ENCABEZADO SUPERIOR DINÁMICO
    # ---------------------------------------------------------
    # Extraemos el código OACI (usualmente es el segundo elemento del reporte)
    codigo_oaci = fragmentos[1] if len(fragmentos) > 1 else "OACI"

    # Buscamos el token de fecha/hora y lo formateamos
    dia_hora_formateada = "Desconocida"
    for frag in fragmentos:
        if frag.endswith("Z") and len(frag) == 7 and frag[:-1].isdigit():
            dia = frag[0:2]
            hora = frag[2:4]
            minuto = frag[4:6]
            dia_hora_formateada = f"Día {dia} a las {hora}:{minuto} UTC"

    # Dibujamos la barra azul del encabezado
    canvas.create_rectangle(0, 0, 2000, 80, fill="#005AA0", outline="")
    
    # Texto de la Estación (Solo muestra el código, ej: "ESTACIÓN: SAVC")
    canvas.create_text(50, 40, text=f"REPORTE METAR - ESTACIÓN: {codigo_oaci}", 
                       fill="white", font=("Arial", 20, "bold"), anchor="w")
    
    # Texto de la hora (Alineado bien a la derecha, en X=1300)
    canvas.create_text(1300, 40, text=f"Emitido: {dia_hora_formateada}", 
                       fill="#4CB8C4", font=("Arial", 16, "bold"), anchor="e")

    # ---------------------------------------------------------
    # 2. TARJETAS DE INSTRUMENTOS (Fondos)
    # ---------------------------------------------------------
    # Tarjeta Viento
    dibujar_tarjeta(80, 120, 420, 500, "#005AA0", "VIENTO EN SUPERFICIE")
    # Tarjeta Clima (Temp + Presión)
    dibujar_tarjeta(450, 120, 850, 500, "#005AA0", "TEMPERATURA Y PRESIÓN")
    # Tarjeta Nubes (Ocupa a lo ancho a la derecha)
    dibujar_tarjeta(880, 120, 1300, 500, "#005AA0", "COBERTURA DE NUBES")

    # ---------------------------------------------------------
    # 3. DIBUJAR INSTRUMENTOS ADENTRO DE LAS TARJETAS
    # ---------------------------------------------------------
    if datos_graficos['viento']:
        dibujar_brujula(canvas, 250, 320, 110, datos_graficos['viento'][0], datos_graficos['viento'][1])
        
    if datos_graficos['temp']:
        dibujar_termometro(canvas, 550, 320, datos_graficos['temp'][0], datos_graficos['temp'][1])
        
    if datos_graficos['presion']:
        dibujar_presion(canvas, 750, 320, datos_graficos['presion'])
        
    if datos_graficos['nubes']:
        dibujar_grafico_nubes(canvas, 920, 180, 330, 250, datos_graficos['nubes'])

def analizar_metar():
    reporte_completo = entrada_texto.get().strip().upper()
    if not reporte_completo:
        messagebox.showwarning("Advertencia", "Por favor, ingresa un código METAR.")
        return

    fragmentos = reporte_completo.split()
    caja_resultados.delete(1.0, tk.END)
    errores = 0

    # Memoria temporal para guardar datos SI el autómata los acepta
    datos_graficos = {'viento': None, 'temp': None, 'presion': None, 'nubes': []}

    for fragmento in fragmentos:
        tipo_identificado = "Desconocido / Inválido"

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
            match = re.match(r'(\d{3}|VRB)(\d{2,3})', fragmento)
            if match and match.group(1) != "VRB":
                datos_graficos['viento'] = (int(match.group(1)), int(match.group(2)))
                
        elif modulo_rango_variable.accept(fragmento):
            tipo_identificado = "Viento Variable"
            
        elif modulo_temperatura.accept(fragmento):
            tipo_identificado = "Temperatura / Punto de Rocío"
            partes = fragmento.split("/")
            if len(partes) == 2:
                try:
                    str_temp = partes[0].replace("M", "-")
                    str_rocio = partes[1].replace("M", "-")
                    datos_graficos['temp'] = (int(str_temp), int(str_rocio))
                except ValueError:
                    pass
                    
        elif modulo_presion.accept(fragmento):
            tipo_identificado = "Presión (QNH/Altimetro)"
            qnh_valor = int(fragmento[1:]) if fragmento[1:].isdigit() else 1013
            if fragmento.startswith("A"):
                qnh_valor = int(qnh_valor * 33.8639 / 100)
            datos_graficos['presion'] = qnh_valor
            
        elif modulo_nubes.accept(fragmento):
            tipo_identificado = "Nubosidad"
            cantidad = fragmento[:3]
            if fragmento[3:].isdigit():
                altura_pies = int(fragmento[3:]) * 100
                datos_graficos['nubes'].append((cantidad, altura_pies))
                
        elif modulo_clima.accept(fragmento):
            tipo_identificado = "Fenómeno Climático"
        elif modulo_vis_general.accept(fragmento):
            tipo_identificado = "Visibilidad General"
        elif modulo_vis_pista.accept(fragmento):
            tipo_identificado = "Visibilidad en Pista (RVR)"
        elif modulo_lugar.accept(fragmento):
            tipo_identificado = "Identificador de Estación (OACI)"
        else:
            errores += 1

        if tipo_identificado == "Desconocido / Inválido":
            caja_resultados.insert(tk.END, f"❌ [{fragmento}] -> NO RECONOCIDO\n")
        else:
            caja_resultados.insert(tk.END, f"✅ [{fragmento}] -> {tipo_identificado}\n")

    caja_resultados.insert(tk.END, "-"*40 + "\n")
    
    # LA MAGIA DE LAS VENTANAS
    if errores == 0:
        caja_resultados.insert(tk.END, "Veredicto: SINTAXIS METAR VÁLIDA.\n>>> Abriendo Dashboard Visual...")
        abrir_ventana_graficos(datos_graficos, fragmentos)
    else:
        caja_resultados.insert(tk.END, f"Veredicto: SE ENCONTRARON {errores} ERROR(ES). CORRIGA EL REPORTE.")

# Crear la ventana principal de Consola
ventana = tk.Tk()
ventana.title("Validador Completo METAR - FTI")
ventana.geometry("700x550") # Ventana compacta, sin canvas acá
ventana.configure(bg="#005AA0")

etiqueta = tk.Label(ventana, text="Ingresa el reporte METAR completo:", font=("Arial", 14), bg="#005AA0", fg="white")
etiqueta.pack(pady=10)

entrada_texto = tk.Entry(ventana, font=("Arial", 12), width=65)
entrada_texto.pack(pady=5)

boton = tk.Button(ventana, text="Analizar Reporte", command=analizar_metar, font=("Arial", 11, "bold"), bg="lightblue")
boton.pack(pady=10)

caja_resultados = tk.Text(ventana, font=("Courier", 11), height=20, width=65, bg="#0F2027", fg="white")
caja_resultados.pack(pady=10)

ventana.mainloop()