# 1) Función para calcular el objetivo de agua
def calcular_objetivo_ml(peso_kg, nivel_actividad):
    base = peso_kg * 35

    if nivel_actividad == "bajo":
        objetivo = base * 0.9
    elif nivel_actividad == "medio":
        objetivo = base
    elif nivel_actividad == "alto":
        objetivo = base * 1.1
    else:
        objetivo = base  # por seguridad

    return objetivo


# 2) Función para evaluar el estado de hidratación
def estado_hidratacion(consumo_ml, objetivo_ml):
    if consumo_ml < objetivo_ml:
        porcentaje = ((objetivo_ml - consumo_ml) / objetivo_ml) * 100
        return f"Te falta un {porcentaje:.2f}% para llegar"
    
    elif consumo_ml == objetivo_ml:
        return "Has alcanzado tu objetivo"
    
    else:
        porcentaje = ((consumo_ml - objetivo_ml) / objetivo_ml) * 100
        return f"Has excedido tu objetivo en {porcentaje:.2f}%"


# Lista para guardar personas
personas = []

# Ciclo para cargar múltiples personas
while True:
    try:
        print("\n--- Nueva persona ---")
        
        peso = float(input("Ingrese su peso en kg: "))
        actividad = input("Nivel de actividad (bajo/medio/alto): ").lower()
        
        if actividad not in ["bajo", "medio", "alto"]:
            print("Nivel de actividad inválido")
            continue
        
        consumo = float(input("Ingrese consumo de agua en ml: "))

        # Calcular objetivo
        objetivo = calcular_objetivo_ml(peso, actividad)

        # Evaluar estado
        mensaje = estado_hidratacion(consumo, objetivo)

        # Mostrar resultados
        print(f"Objetivo diario: {objetivo:.2f} ml")
        print(mensaje)

        # Guardar datos en diccionario
        persona = {
            "peso": peso,
            "actividad": actividad,
            "consumo": consumo,
            "objetivo": objetivo
        }

        personas.append(persona)

    except ValueError:
        print("Error: Debe ingresar números válidos.")
        continue

    # Preguntar si quiere seguir
    seguir = input("¿Desea cargar otra persona? (si/no): ").lower()
    if seguir != "si":
        break


# Mostrar resumen final
print("\n--- Resumen de personas ---")
for i, p in enumerate(personas, start=1):
    print(f"\nPersona {i}:")
    print(f"Peso: {p['peso']} kg")
    print(f"Actividad: {p['actividad']}")
    print(f"Consumo: {p['consumo']} ml")
    print(f"Objetivo: {p['objetivo']:.2f} ml")
