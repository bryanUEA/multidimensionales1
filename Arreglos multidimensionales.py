# Definir las ciudades, días de la semana y semanas
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4  # Por ejemplo, 4 semanas

# Crear una matriz 3D con valores iniciales de temperatura (para demostración)
temperaturas = [[[0 for _ in range(semanas)] for _ in range(len(dias_semana))] for _ in range(len(ciudades))]

# Ingresar datos de temperaturas (reemplazar con datos reales)
# Por ejemplo, temperaturas[ciudad_idx][dia_idx][semana_idx] = valor_temperatura

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad_idx, ciudad in enumerate(ciudades):
    print(f"Promedio de temperaturas para {ciudad}:")
    for semana in range(semanas):
        suma_temperaturas = 0
        for dia_idx, dia in enumerate(dias_semana):
            # Aquí deberías obtener el valor real de temperatura para cada día
            # y sumarlo a suma_temperaturas
            # Ejemplo: suma_temperaturas += temperaturas[ciudad_idx][dia_idx][semana]
            pass
        promedio_semana = suma_temperaturas / len(dias_semana)
        print(f"Semana {semana + 1}: {promedio_semana:.2f}°C")


