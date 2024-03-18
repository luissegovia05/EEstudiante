# Definir el diccionario de tipo Vuelo
vuelo = {
    'Aerolinea': 'Avianca',
    'Vuelo': 'AV3102',
    'Origen': 'CTG',
    'Destino': 'MDE',
    'Maletas_temáticas': ['Cabina', 'Mano', 'Bodega']
}

# Imprimir los valores del diccionario
print("Valores del diccionario:")
for key, value in vuelo.items():
    print(f"{key}: {value}")

# Imprimir los valores del tipo de maleta
print("\nTipos de maleta:")
for maleta in vuelo['Maletas_temáticas.']:
    print(maleta)
