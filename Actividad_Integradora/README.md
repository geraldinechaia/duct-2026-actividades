# Mi analizador de frecuencias

Este script lee el archivo `texto_integradora.txt`, cuenta cuántas veces aparece cada palabra y genera un gráfico de barras con las 10 palabras más frecuentes,que guarda como `grafico_frecuencias.png`. Si el archivo no existe, muestra un
mensaje de error en lugar de cortarse.

## Requisitos
- Python 3.12 o superior
- Bibliotecas: `matplotlib` y `pytest` (`pip install matplotlib pytest`)

## Cómo ejecutarlo
1. Dejá `analizador.py` y `texto_integradora.txt` en la misma carpeta.
2. Ejecutá: `python analizador.py`
3. Para correr las pruebas: `pytest -v`

