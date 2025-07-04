import json
import os


# Diccionarios iniciales
diccionario_1 = {"kevin":1068813286,"juan": 1068813287, "matias": 1068813288, "manuel": 167813286}
diccionario_2= {"kevin":"jugar ajedrez","juan":"jugar futbol","matias":"jugar beisboll", "manuel": "jugar teniz"
}

# 1 imprimir valores de forma ascendente
def obtener_valores_ascendentes(diccionario):
    valores_ordenados = sorted(diccionario.values())
    print(valores_ordenados)

print("--- Valores ascendentes ---")
obtener_valores_ascendentes(diccionario_1)

# 2 comparar claves y valores de diccionarios
def comparar_claves_valores(diccionario1, diccionario2):
    """
    Compara si todas las claves y sus valores correspondientes
    en el primer diccionario son iguales en el segundo diccionario.
    """
    return all(diccionario1.get(clave) == diccionario2.get(clave) for clave in diccionario1)

print("\n--- Comparación de claves y valores ---")
print(comparar_claves_valores(diccionario_1, diccionario_2))

# 3 unir diccionarios
def unir_dos_diccionarios(diccionario1, diccionario2):
    """
    Une dos diccionarios, sobrescribiendo los valores del primero
    con los del segundo si las claves coinciden.
    """
    nuevo_diccionario_unido = diccionario2.copy()
    nuevo_diccionario_unido.update(diccionario1)
    return nuevo_diccionario_unido

print("\n--- Unir diccionarios ---")
print(unir_dos_diccionarios(diccionario_1, diccionario_2))

# 4. Filtrar personas por rango de edad
def filtrar_personas_por_edad(lista_de_personas, edad_minima, edad_maxima):
    """
    Filtra e imprime los nombres completos de las personas
    dentro de un rango de edad específico.
    """
    print(f"\n--- Personas entre {edad_minima} y {edad_maxima} años ---")
    for persona_info in lista_de_personas:
        if edad_minima <= persona_info["edad"] <= edad_maxima:
            print(f"{persona_info['nombre_completo']} {persona_info['apellido_completo']}")

# Lista de personas
base_de_datos_personas = [
    {"nombre_completo": "Pedro Julio", "apellido_completo": "Tristán Merchán", "edad": 101},
    {"nombre_completo": "Laura", "apellido_completo": "Ramírez", "edad": 25},
    {"nombre_completo": "Carlos", "apellido_completo": "Gómez", "edad": 30}
]

filtrar_personas_por_edad(base_de_datos_personas, 20, 40)

# funciones de archivos json
# Preparación: Crear una carpeta y un archivo JSON de ejemplo
os.makedirs("archivos_datos", exist_ok=True) # Cambiado de 'files' a 'archivos_datos'

datos_ventas = [
    {"Pais_Venta": "United Kingdom", "Tipo_Pago": "Visa"},
    {"Pais_Venta": "United Kingdom", "Tipo_Pago": "Mastercard"},
    {"Pais_Venta": "Colombia", "Tipo_Pago": "Visa"},
    {"Pais_Venta": "United Kingdom", "Tipo_Pago": "Visa"},
    {"Pais_Venta": "Colombia", "Tipo_Pago": "Visa"}
]

with open("archivos_datos/RegistroVentas2009.json", "w", encoding="utf-8") as f: # Cambiado nombre de archivo
    json.dump(datos_ventas, f, indent=4)

# 5. Contar compras por país
def contar_compras_por_pais(ruta_archivo, nombre_pais):
    """
    Cuenta el número de registros en un archivo JSON que coinciden con un país dado.
    """
    with open(ruta_archivo, encoding="utf-8") as f:
        datos_cargados = json.load(f)
    return sum(1 for registro in datos_cargados if registro["Pais_Venta"] == nombre_pais) # Cambiado 'Country' a 'Pais_Venta'

# 6. Contar compras por método de pago
def contar_compras_por_metodo_pago(ruta_archivo, metodo_pago):
    """
    Cuenta el número de registros en un archivo JSON que coinciden con un método de pago dado.
    """
    with open(ruta_archivo, encoding="utf-8") as f:
        datos_cargados = json.load(f)
    return sum(1 for registro in datos_cargados if registro["Tipo_Pago"] == metodo_pago) # Cambiado 'Payment_Type' a 'Tipo_Pago'

print("\n--- Conteo de compras ---")
print("Compras en UK:", contar_compras_por_pais("archivos_datos/RegistroVentas2009.json", "United Kingdom"))
print("Compras con Visa:", contar_compras_por_metodo_pago("archivos_datos/RegistroVentas2009.json", "Visa"))

# Preparación para funciones 7, 8 y 9: Crear un JSON de personas con deportes
datos_personas_deportes = {
    "usuario1": {"nombre_completo": "Ana", "apellido_completo": "García", "edad": 30, "deportes": ["fútbol", "natación"]},
    "usuario2": {"nombre_completo": "Juan", "apellido_completo": "Pérez", "edad": 22, "deportes": ["baloncesto", "fútbol"]},
    "usuario3": {"nombre_completo": "María", "apellido_completo": "López", "edad": 35, "deportes": ["natación", "ciclismo"]}
}
with open("archivos_datos/personas_deportes.json", "w", encoding="utf-8") as f:
    json.dump(datos_personas_deportes, f, indent=4)

# 7. Personas por deporte
def encontrar_personas_por_deporte(ruta_archivo_json, deporte_buscado):
    """
    Busca y imprime los nombres completos de las personas que practican un deporte específico.
    """
    with open(ruta_archivo_json, encoding='utf-8') as f:
        informacion_personas = json.load(f)

    print(f"\n--- Personas que practican {deporte_buscado} ---")
    for _id_usuario, detalles_persona in informacion_personas.items(): # Cambiado 'usuario' a '_id_usuario' y 'datos' a 'detalles_persona'
        if deporte_buscado in detalles_persona["deportes"]:
            print(f'{detalles_persona["nombre_completo"]} {detalles_persona["apellido_completo"]}')

encontrar_personas_por_deporte("archivos_datos/personas_deportes.json", "fútbol")

# 8. Personas por rango de edad desde JSON
def obtener_personas_por_rango_edad(ruta_archivo_json, edad_minima, edad_maxima):
    """
    Busca y imprime los nombres completos de las personas
    en un archivo JSON dentro de un rango de edad.
    """
    with open(ruta_archivo_json, encoding='utf-8') as f:
        informacion_personas = json.load(f)

    print(f"\n--- Personas entre {edad_minima} y {edad_maxima} años (desde JSON) ---")
    for detalles_persona in informacion_personas.values(): # Cambiado 'datos' a 'detalles_persona'
        if edad_minima <= detalles_persona["edad"] <= edad_maxima:
            print(f'{detalles_persona["nombre_completo"]} {detalles_persona["apellido_completo"]}')

obtener_personas_por_rango_edad("archivos_datos/personas_deportes.json", 20, 30)

# 9. Crear JSON organizado por deporte
def generar_json_por_deporte(ruta_archivo_entrada, ruta_archivo_salida):
    """
    Crea un nuevo archivo JSON que organiza a las personas
    por los deportes que practican.
    """
    with open(ruta_archivo_entrada, encoding='utf-8') as f:
        informacion_personas = json.load(f)

    deportes_y_usuarios = {}
    for id_usuario, detalles_persona in informacion_personas.items(): # Cambiado 'usuario' a 'id_usuario' y 'datos' a 'detalles_persona'
        for deporte_individual in detalles_persona["deportes"]: # Cambiado 'd' a 'deporte_individual'
            deportes_y_usuarios.setdefault(deporte_individual, []).append(id_usuario)

    with open(ruta_archivo_salida, "w", encoding="utf-8") as f_salida: # Cambiado 'f_out' a 'f_salida'
        json.dump(deportes_y_usuarios, f_salida, indent=4)

print("\n--- Generando JSON por deporte ---")
generar_json_por_deporte("archivos_datos/personas_deportes.json", "archivos_datos/deportes_clasificados.json")
print("Archivo 'deportes_clasificados.json' creado.")

# Preparación para función 10: Crear JSON de ejemplo para coincidencias
datos_json_uno = {"id1": "valorA", "id2": "valorB", "id3": "valorC"}
datos_json_dos = {"id2": "valorB", "id3": "valorX", "id4": "valorY"}
with open("archivos_datos/datos_comparar_1.json", "w", encoding="utf-8") as f:
    json.dump(datos_json_uno, f, indent=4)
with open("archivos_datos/datos_comparar_2.json", "w", encoding="utf-8") as f:
    json.dump(datos_json_dos, f, indent=4)

# 10. Encontrar coincidencias entre dos JSON
def encontrar_coincidencias_en_json(ruta_json1, ruta_json2, ruta_salida_json):
    """
    Encuentra y guarda en un nuevo JSON las coincidencias de clave-valor
    entre dos archivos JSON.
    """
    with open(ruta_json1, encoding='utf-8') as f_uno, open(ruta_json2, encoding='utf-8') as f_dos: # Cambiado 'f1' a 'f_uno', 'f2' a 'f_dos'
        contenido_json1 = json.load(f_uno) # Cambiado 'datos1' a 'contenido_json1'
        contenido_json2 = json.load(f_dos) # Cambiado 'datos2' a 'contenido_json2'

    registros_coincidentes = {clave: valor for clave, valor in contenido_json1.items() if clave in contenido_json2 and contenido_json2[clave] == valor} # Cambiado 'coincidencias' a 'registros_coincidentes'

    with open(ruta_salida_json, 'w', encoding='utf-8') as f_salida_coincidencias: # Cambiado 'fout' a 'f_salida_coincidencias'
        json.dump(registros_coincidentes, f_salida_coincidencias, indent=4)

print("\n--- Encontrando coincidencias entre JSON ---")
encontrar_coincidencias_en_json("archivos_datos/datos_comparar_1.json", "archivos_datos/datos_comparar_2.json", "archivos_datos/json_coincidencias.json")
print("Archivo 'json_coincidencias.json' creado.")

# Preparación para función 11: Crear JSON de ejemplo para promediar notas
datos_notas_estudiantes = {
    "EstudianteA": {"asignatura_1": [80, 90, 75], "asignatura_2": [60, 70]},
    "EstudianteB": {"asignatura_1": [95, 85, 90]},
    "EstudianteC": {"asignatura_3": []}
}
with open("archivos_datos/notas_estudiantes.json", "w", encoding="utf-8") as f:
    json.dump(datos_notas_estudiantes, f, indent=4)

# 11. Promediar notas de estudiantes desde JSON
def calcular_promedio_notas(ruta_archivo_json):
    """
    Calcula e imprime el promedio de notas por asignatura para cada estudiante.
    """
    with open(ruta_archivo_json, encoding='utf-8') as f:
        datos_de_notas = json.load(f) # Cambiado 'datos' a 'datos_de_notas'

    print("\n--- Promedio de notas por estudiante y asignatura ---")
    for nombre_estudiante, actividades_academicas in datos_de_notas.items(): # Cambiado 'estudiante' a 'nombre_estudiante', 'actividades' a 'actividades_academicas'
        for codigo_asignatura, lista_notas in actividades_academicas.items(): # Cambiado 'cod_asignatura' a 'codigo_asignatura', 'notas' a 'lista_notas'
            promedio_calculado = sum(lista_notas) / len(lista_notas) if lista_notas else 0 # Cambiado 'promedio' a 'promedio_calculado'
            print(f"{nombre_estudiante} - {codigo_asignatura}: {promedio_calculado:.2f}")

calcular_promedio_notas("archivos_datos/notas_estudiantes.json")

# Preparación para función 12: Crear JSON de ejemplo para desencriptar
datos_encriptados = {"mensaje1": "h$l$ c$m# #st$s", "mensaje2": "gr*c*$s p+r t+ *mp+rt$nc*"}
with open("archivos_datos/mensajes_encriptados.json", "w", encoding="utf-8") as f:
    json.dump(datos_encriptados, f, indent=4)

# 12. Desencriptar vocales en un archivo JSON
def desencriptar_vocales_json(ruta_archivo_entrada, ruta_archivo_salida):
    """
    Desencripta vocales codificadas en un archivo JSON y guarda el resultado en uno nuevo.
    """
    mapa_desencriptacion = {'$': 'a', '#': 'e', '*': 'i', '=': 'o', '+': 'u'} # Cambiado 'mapa' a 'mapa_desencriptacion'

    with open(ruta_archivo_entrada, encoding='utf-8') as f:
        datos_a_desencriptar = json.load(f) # Cambiado 'datos' a 'datos_a_desencriptar'

    diccionario_resultado = {} # Cambiado 'resultado' a 'diccionario_resultado'
    for clave_original, valor_encriptado in datos_a_desencriptar.items(): # Cambiado 'clave' a 'clave_original', 'valor' a 'valor_encriptado'
        cadena_descodificada = ''.join(mapa_desencriptacion.get(caracter, caracter) for caracter in valor_encriptado) # Cambiado 'descodificado' a 'cadena_descodificada', 'c' a 'caracter'
        diccionario_resultado[clave_original] = cadena_descodificada

    with open(ruta_archivo_salida, 'w', encoding='utf-8') as f_salida_desencriptado: # Cambiado 'f_out' a 'f_salida_desencriptado'
        json.dump(diccionario_resultado, f_salida_desencriptado, indent=4)

print("\n--- Desencriptando vocales ---")
desencriptar_vocales_json("archivos_datos/mensajes_encriptados.json", "archivos_datos/mensajes_desencriptados.json")
print("Archivo 'mensajes_desencriptados.json' creado.")
#13 
def ejercicio_1():
    # Se cambia la lista para tener más elementos
    lista = [10, 20, 30, 40, 50, 60]
    try:
        # Se intenta acceder a una posición que sigue fuera del nuevo rango
        print(lista[7])
    except IndexError:
        print("Error: Intentas acceder a una posición que no está en el arreglo.")

#14

def ejercicio_2():
    def operar(a, b):
        return a * b

    try:
        a = int(input("Ingresa un número: "))
        # Se cambia el valor por defecto para que sea más claro el ejemplo de TypeError
        b = input("Ingresa algo (texto o número): ")
        print("Resultado:", operar(a, b))
    except TypeError:
        print("Error: Los tipos de datos no son compatibles para operar.")

#15 y 16

def ejercicio_3_4():
    def operar(a, b):
        return a + b

    try:
        a = int(input("Ingresa un número: "))
        # Se cambia el valor por defecto para que sea más claro el ejemplo de TypeError
        b = input("Ingresa otro valor: ")
        resultado = operar(a, b)
        print("Resultado:", resultado)
    except TypeError:
        print("Error: No puedes combinar tipos incompatibles.")
    except ValueError:
        print("Error: Entrada inválida.")
#17
def ejercicio_5():
    # Se cambian los valores del diccionario
    dic = {'Alice': 'Python', 'Bob': 'Java', 'Charlie': 'C++'}
    try:
        # Se intenta acceder a una clave que no existe
        print(dic['David'])
    except KeyError:
        print("Error: Esa clave no existe en el diccionario.")
#18
def ejercicio_6():
    # Se cambian los valores del diccionario
    dic = {'Alice': 'Python', 'Bob': 'Java', 'Charlie': 'C++'}
    try:
        # Se intenta acceder a una clave que no existe
        print(dic['Eve'])
    except KeyError as e:
        print(f"Error: La clave '{e.args[0]}' no existe en el diccionario.")


def menu():
    while True:
        print("\n MENÚ DE EJERCICIOS DE EXCEPCIONES")
        print("1. Acceso inválido en lista (IndexError)")
        print("2. Operación inválida por tipo de dato (TypeError 1)")
        print("3. Operación inválida suma int + str (TypeError 2)")
        print("4. Clave inexistente en diccionario (KeyError simple)")
        print("5. Clave inexistente con mensaje detallado (KeyError con clave)")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ejercicio_1()
        elif opcion == "2":
            ejercicio_2()
        elif opcion == "3":
            ejercicio_3_4()
        elif opcion == "4":
            ejercicio_5()
        elif opcion == "5":
            ejercicio_6()
        elif opcion == "0":
            print("¡Adiós!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

menu()