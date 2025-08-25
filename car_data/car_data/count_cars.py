
import dagster as dg
import polars as pl
import os

# Definimos la ruta al archivo como una constante
data_dir = "data"
CSV_PATH = os.path.join(data_dir, "carprice.csv")

@dg.asset
def brand_analysis(context: dg.AssetExecutionContext):
    """
    Este activo lee el archivo de coches, cuenta el número total de marcas
    y luego cuenta cuántos coches hay por cada marca, mostrando los
    resultados en los logs de Dagster.
    """
    context.log.info(f"Iniciando análisis de marcas desde el archivo: {CSV_PATH}")

   
    # --- 1. Cargar los datos del archivo CSV ---
    df = pl.read_csv(CSV_PATH)
    context.log.info(f"Se cargaron {len(df)} filas de datos.")

    # --- Tarea 1: Detectar cuántas marcas únicas hay ---
    total_brands = df.select(pl.col("make").n_unique()).item()
    context.log.info(f"TAREA 1 - Total de marcas de coches únicas: {total_brands}")

    # --- Tarea 2: Contar cuántos autos hay de cada marca ---
    cars_per_brand = df.group_by("make").len().sort("len", descending=True)
    context.log.info(f"TAREA 2 - Conteo de coches por marca:\n{cars_per_brand}")

    