# activos_filtros.py

import dagster as dg
import polars as pl
import os


# Importación del archivo assets
from .assets import car_data_file

# --- Constantes ---
DATA_DIR = "data"
CSV_PATH = os.path.join(DATA_DIR, "carprice.csv")
FILTERED_CSV_PATH = os.path.join(DATA_DIR, "filtered_diesel_cars.csv")

# --- Activo de Filtrado ---
@dg.asset(deps=[car_data_file]) 
def diesel_four_door_cars(context: dg.AssetExecutionContext):
    """
    Filtra los datos para coches diésel, de cuatro puertas y con un
    precio menor a 50,000. Guarda el resultado en un nuevo archivo CSV.
    """
    context.log.info(f'Filtrando los datos con los criterios especificados.')
    df = pl.read_csv(CSV_PATH)

    filtered_df = df.filter(
        (pl.col("fuel-type") == "gas") &
        (pl.col("num-of-doors") == "four") &
        (pl.col("price") < 50000) &
        (pl.col("price").is_not_null())
    )
    
    filtered_df.write_csv(FILTERED_CSV_PATH)
    context.log.info(f'Se encontraron {len(filtered_df)} coches.')
    context.log.info(f'Datos filtrados guardados en: {FILTERED_CSV_PATH}')

  
#ACTIVO 2 LEER EL FILTRO Y LUEGO AGRUPARLO

@dg.asset(deps=[diesel_four_door_cars])
def filter_cars_brand(context:dg.AssetExecutionContext):
    """
    lee el archivo filtrado, luego agrupa y cuenta cada
    marca de carro que tip de gasolina usan 
    """
    context.log.info(f'leyendo datos filtrados de {FILTERED_CSV_PATH}')

    #Leé el archivo filtrado 
    df= pl.read_csv(FILTERED_CSV_PATH)

    # Agrupa y cuenta
    count_by_brand = df.group_by("make").agg(
        pl.len().alias("count")
    ).sort("count", descending=True) # Ordena para ver los más comunes primero

    context.log.info(f"Conteo de coches filtrados por marca:\n{count_by_brand}")



