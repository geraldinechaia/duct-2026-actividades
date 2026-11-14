# analizador.py
import matplotlib.pyplot as plt


def leer_texto(ruta):
    """Lee un archivo de texto y devuelve su contenido (o None si no existe)."""
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"Error: no se encontro el archivo '{ruta}'.")
        return None


def contar_frecuencias(texto):
    """
    Cuenta la frecuencia de cada palabra en un texto.

    Parametros:
        texto (str): el texto a analizar

    Retorna:
        dict: pares {palabra: frecuencia}
    """
    palabras = texto.lower().split()
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias


def graficar_top(frecuencias, top_n=10, salida="grafico_frecuencias.png"):
    """Genera y guarda un grafico de barras con las top_n palabras mas frecuentes."""
    top = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:top_n]
    palabras = [p for p, f in top]
    valores = [f for p, f in top]

    plt.figure(figsize=(10, 6))
    plt.barh(palabras[::-1], valores[::-1], color="steelblue")
    plt.title(f"Top {top_n} palabras mas frecuentes")
    plt.xlabel("Frecuencia")
    plt.tight_layout()
    plt.savefig(salida, dpi=150, bbox_inches="tight")
    plt.close()


def main():
    texto = leer_texto("texto_integradora.txt")
    if texto is None:
        return
    frecuencias = contar_frecuencias(texto)
    print(f"Palabras totales: {sum(frecuencias.values())}")
    print(f"Palabras distintas: {len(frecuencias)}")
    graficar_top(frecuencias)
    print("Grafico guardado en grafico_frecuencias.png")


if __name__ == "__main__":
    main()

