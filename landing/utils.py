def estimar_huella(
    transporte, pasajeros, distancia_km,
    energia_kwh, gas_m3,
    tipo_combustible, litros_combustible
):
    # Transporte público
    emisiones_transporte = 0
    if transporte == 'bus':
        emisiones_transporte = 0.105 * distancia_km * pasajeros
    elif transporte == 'train':
        emisiones_transporte = 0.041 * distancia_km * pasajeros
    elif transporte == 'bike':
        emisiones_transporte = 0
    elif transporte == 'car':
        # supondremos 0.192 kg CO₂/km por defecto por auto particular
        emisiones_transporte = 0.192 * distancia_km

    # Electricidad
    emisiones_energia = energia_kwh * 0.233

    # Gas natural
    emisiones_gas = gas_m3 * 2.0

    # Combustible particular
    if tipo_combustible == 'petrol':
        emisiones_auto = litros_combustible * 2.31
    elif tipo_combustible == 'diesel':
        emisiones_auto = litros_combustible * 2.68
    else:
        emisiones_auto = 0

    # Total
    total = emisiones_transporte + emisiones_energia + emisiones_gas + emisiones_auto
    return round(total, 2)


# Tabla de emisiones de CO₂ por fuente de energía y transporte
#| Fuente           | Emisión estimada           |
#| ---------------- | -------------------------- |
#| 🚗 Auto (petrol) | 2.31 kg CO₂ / litro        |
#| 🚙 Auto (diesel) | 2.68 kg CO₂ / litro        |
#| 🚌 Bus           | 0.105 kg CO₂ / pasajero·km |
#| 🚆 Tren          | 0.041 kg CO₂ / pasajero·km |
#| 🚲 Bicicleta     | 0 kg CO₂                   |
#| ⚡ Electricidad   | 0.233 kg CO₂ / kWh         |
#| 🔥 Gas natural   | 2.0 kg CO₂ / m³            |
