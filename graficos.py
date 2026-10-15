import tkinter as tk
import math

def dibujar_brujula(canvas, centro_x, centro_y, radio, grados, velocidad_kt):
    # 1. Fondo del instrumento (estilo panel oscuro)
    canvas.create_oval(centro_x - radio, centro_y - radio, 
                       centro_x + radio, centro_y + radio, 
                       fill="#0F2027", outline="#203A43", width=4)
    
    # 2. Puntos cardinales
    opciones_texto = {"fill": "white", "font": ("Arial", 12, "bold")}
    canvas.create_text(centro_x, centro_y - radio + 15, text="N", **opciones_texto)
    canvas.create_text(centro_x, centro_y + radio - 15, text="S", **opciones_texto)
    canvas.create_text(centro_x + radio - 15, centro_y, text="E", **opciones_texto)
    canvas.create_text(centro_x - radio + 15, centro_y, text="W", **opciones_texto)
    
    # 3. Matemática para la aguja
    # En aviación la dirección es de dónde VIENE el viento.
    # Sumamos 180° para que la punta indique hacia dónde VA.
    # Restamos 90° para sincronizar el 0° con el Norte (arriba).
    angulo_rad = math.radians(grados + 180 - 90)
    largo_aguja = radio - 25
    
    punta_x = centro_x + largo_aguja * math.cos(angulo_rad)
    punta_y = centro_y + largo_aguja * math.sin(angulo_rad)
    
    # 4. Dibujar la aguja indicadora y el centro
    canvas.create_line(centro_x, centro_y, punta_x, punta_y, fill="#FF4B2B", width=4, arrow=tk.LAST)
    canvas.create_oval(centro_x - 6, centro_y - 6, centro_x + 6, centro_y + 6, fill="white")
    
    # 5. Etiqueta inferior con la velocidad
    canvas.create_text(centro_x, centro_y + radio + 20, 
                       text=f"{velocidad_kt} KT", fill="black", font=("Arial", 14, "bold"))

def dibujar_termometro(canvas, x_centro, y_base, temp_c, rocio_c):
    # Fondo del panel (estilo oscuro para que combine)
    canvas.create_rectangle(x_centro - 60, y_base - 130, x_centro + 60, y_base + 60, fill="#0F2027", outline="#203A43", width=3)
    
    # Textos de título y punto de rocío
    canvas.create_text(x_centro, y_base - 115, text="TEMP", fill="white", font=("Arial", 10, "bold"))
    canvas.create_text(x_centro, y_base + 45, text=f"Rocío: {rocio_c}°C", fill="#4CB8C4", font=("Arial", 10, "bold"))

    # Dibujamos el tubo de vidrio vacío
    canvas.create_rectangle(x_centro - 10, y_base - 90, x_centro + 10, y_base, fill="#2C3E50", outline="gray")
    
    # Matemática para la altura del líquido (escala aproximada de -10°C a 50°C)
    # 50°C llenaría todo el tubo (90px). 0°C llena un poco.
    altura_liquido = max(0, min(90, (temp_c + 10) * 1.5))
    
    # Color del líquido: Rojo si hace calor (>15), Celeste si hace frío
    color_liq = "#FF4B2B" if temp_c > 15 else "#4CB8C4"
    
    # Bulbo inferior y líquido dentro del tubo
    canvas.create_oval(x_centro - 20, y_base - 10, x_centro + 20, y_base + 30, fill=color_liq, outline="gray")
    canvas.create_rectangle(x_centro - 5, y_base - altura_liquido, x_centro + 5, y_base, fill=color_liq, outline="")
    
    # Etiqueta con los grados exactos al lado del tubo
    canvas.create_text(x_centro + 35, y_base - altura_liquido, text=f"{temp_c}°C", fill="white", font=("Arial", 12, "bold"))

def dibujar_presion(canvas, x_centro, y_centro, qnh):
    # Fondo del panel (haciendo juego con el termómetro)
    canvas.create_rectangle(x_centro - 60, y_centro - 40, x_centro + 60, y_centro + 40, 
                            fill="#0F2027", outline="#203A43", width=3)
    
    # Título superior
    canvas.create_text(x_centro, y_centro - 20, text="PRESIÓN", 
                       fill="#4CB8C4", font=("Arial", 10, "bold"))
    
    # Valor del QNH en grande
    canvas.create_text(x_centro, y_centro + 10, text=f"{qnh} hPa", 
                       fill="white", font=("Arial", 16, "bold"))

def dibujar_grafico_nubes(canvas, x_base, y_base, ancho, alto, lista_nubes):
    # 1. Dibujar el eje vertical (la regla)
    canvas.create_line(x_base, y_base, x_base, y_base + alto, fill="#4CB8C4", width=2)
    
    # 2. Dibujar las líneas horizontales de altitud (0, 1000, 2000... hasta 5000 ft)
    for i in range(1, 6):
        altura_escala = i * 1000
        y_linea = y_base + alto - (altura_escala / 5000) * alto
        # Línea de fondo
        canvas.create_line(x_base, y_linea, x_base + ancho, y_linea, fill="#203A43", width=1)
        # Texto de la altura en la regla
        canvas.create_text(x_base - 25, y_linea, text=f"{altura_escala:,}", fill="#4CB8C4", font=("Arial", 10))
    
    # Etiqueta base de 0 ft
    canvas.create_text(x_base - 25, y_base + alto, text="0 ft", fill="#4CB8C4", font=("Arial", 10))

    # 3. Dibujar cada capa de nube
    for (cantidad, alt_pies) in lista_nubes:
        # Si la nube está a más de 5000 pies, la dibujamos en el tope del gráfico para que no se salga
        alt_visual = min(alt_pies, 5000) 
        y_nube = y_base + alto - (alt_visual / 5000) * alto
        
        # Dibujamos los 3 círculos que forman la nube blanca
        x_nube = x_base + 80
        canvas.create_oval(x_nube - 30, y_nube - 15, x_nube + 10, y_nube + 15, fill="white", outline="")
        canvas.create_oval(x_nube - 15, y_nube - 25, x_nube + 25, y_nube + 15, fill="white", outline="")
        canvas.create_oval(x_nube + 10, y_nube - 15, x_nube + 40, y_nube + 15, fill="white", outline="")
        
        # Dibujamos la tarjetita estilo "FEW 4,500" a la derecha de la nube
        x_tag = x_base + 200
        canvas.create_rectangle(x_tag - 40, y_nube - 12, x_tag + 40, y_nube + 12, 
                                fill="#0F2027", outline="#4CB8C4", width=1)
        canvas.create_text(x_tag, y_nube, text=f"{cantidad} {alt_pies:,}", fill="white", font=("Arial", 9, "bold"))