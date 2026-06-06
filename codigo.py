
DISTANCIAS_A_CAPITAL = {
    "moron": 30,
    "ramos mejia": 240,
    "castelar": 33,
    "san justo": 25
}

def calcular_itinerario(ubicacion: str, es_ida_y_vuelta: bool = True, desvio_km: float = 0.0) -> float:

    # Normalizamos el texto para evitar problemas con mayúsculas
    origen = ubicacion.lower().strip()
    
    # Validación de existencia de la localidad
    if origen not in DISTANCIAS_A_CAPITAL:
        raise ValueError(f"Lo siento, la ubicación '{ubicacion}' no está registrada en el sistema.")
        
    distancia_base = DISTANCIAS_A_CAPITAL[origen]
    
    # Aplicamos la lógica del trayecto
    multiplicador_trayecto = 2 if es_ida_y_vuelta else 1
    distancia_total = (distancia_base * multiplicador_trayecto) + desvio_km
    
    return distancia_total

# --- Bloque Principal / Prueba del código ---
try:
    mi_ubicacion = "Morón"
    
    # Calculamos un viaje de ida y vuelta sumando 5km de un desvío (por ejemplo, pasar por una estación de servicio)
    km_totales = calcular_itinerario(ubicacion=mi_ubicacion, es_ida_y_vuelta=True, desvio_km=5.0)
    
    print(f"--- Reporte de Viaje ---")
    print(f"Origen: {mi_ubicacion.title()}")
    print(f"Distancia total calculada: {km_totales} km")

except ValueError as e:
    print(f"Error en el cálculo: {e}")