import os

nombre_archivo = "mi_fichero.txt"

# ==========================================
# 1. CREAR Y ESCRIBIR (Modo 'w')
# ==========================================
# Cuidado: Si el archivo ya existe, 'w' borrará todo su contenido previo.
with open(nombre_archivo, 'w', encoding='utf-8') as fichero:
    fichero.write("¡Hola! Esta es la primera línea de mi archivo.\n")
    fichero.write("Y esta es la segunda línea.\n")
print("✅ Archivo creado y texto escrito con éxito.")

# ==========================================
# 2. AÑADIR TEXTO (Modo 'a')
# ==========================================
# El modo 'a' (append) añade texto al final sin borrar nada.
with open(nombre_archivo, 'a', encoding='utf-8') as fichero:
    fichero.write("Esta tercera línea se ha añadido después.\n")
print("✅ Texto nuevo añadido al final.")

# ==========================================
# 3. LEER EL ARCHIVO (Modo 'r')
# ==========================================
print("\n--- Leyendo el contenido del archivo ---")
with open(nombre_archivo, 'r', encoding='utf-8') as fichero:
    # Leer todo de golpe:
    contenido = fichero.read()
    print(contenido)

# ==========================================
# 4. COMPROBAR SI EXISTE Y BORRAR (Opcional)
# ==========================================
# Si necesitas eliminar el archivo en algún momento, puedes usar la librería 'os'
if os.path.exists(nombre_archivo):
    print(f"ℹ️ El archivo '{nombre_archivo}' existe.")
    # Descomenta la siguiente línea si quieres que el script borre el archivo al terminar:
    # os.remove(nombre_archivo)
    # print("🗑️ Archivo borrado.")
else:
    print("El archivo no existe.")