from collections import Counter

with open("mbox.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read()

vocales = set("aeiouAEIOU")
consonantes = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
contador_vocales = 0
contador_consonantes = 0
todas_las_palabras = []

for c in texto:
    if c.isalpha():
        if c in vocales:
            contador_vocales += 1
        elif c in consonantes:
            contador_consonantes += 1

lineas = texto.splitlines()
for linea in lineas:
    palabras = linea.strip().split()
    for palabra in palabras:
        palabra_limpia = "".join(c for c in palabra if c.isalnum())
        if palabra_limpia:
            todas_las_palabras.append(palabra_limpia.lower())

conteo = Counter(todas_las_palabras)
top_50 = conteo.most_common(50)

print("Cantidad de vocales:", contador_vocales)
print("Cantidad de consonantes:", contador_consonantes)
print("\nTop 50 palabras más comunes:")
for palabra, cantidad in top_50:
    print(f"{palabra}: {cantidad}")