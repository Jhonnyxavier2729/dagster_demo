import dagster as dg
import polars as pl 
import duckdb


CSV_URL = "https://raw.githubusercontent.com/Azure/carprice/refs/heads/master/dataset/carprice.csv"

CSV_PATH = "data/carprice.csv"

DUCKDB_PATH = "data/car_data.duckdb"

TABLE_NAME = "avg_price_per_brand"

#extrae archivo CSV y luego transforma los datos perdidos y precio a NULL
@dg.asset
def car_data_file(context: dg.AssetExecutionContext):
    """
    Downloads the CSV directly with polars and saves it locally.
    """
    context.log.info('Downloading CSV file')
    df = pl.read_csv(CSV_URL)

    df = df.with_columns([
        pl.col('normalized-losses').cast(pl.Float64, strict = False), 
        pl.col('price').cast(pl.Float64, strict = False),     
    ])
    df.write_csv(CSV_PATH)
    context.log.info(f'archivo guardado en:{CSV_PATH}')


#calcular el precio promedio por marca 

@dg.asset(deps=[car_data_file])
def avg_price_table(context: dg.AssetExecutionContext):
    """
    Computes average car price per brand, stores it in DuckDB,
    and displays the result visually in the logs.
    """
    context.log.info('Creating aggregated DuckDB table')

    df = pl.read_csv(CSV_PATH)
    df = df.drop_nulls(['price'])

    avg_price_df = df.group_by("make").agg(
        pl.col("price").mean().alias('avg_price')
    )
    
    # --- Tu código para guardar en DuckDB se mantiene igual ---
    with duckdb.connect(DUCKDB_PATH) as con:
        con.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")
        con.execute(f"CREATE TABLE {TABLE_NAME} (make TEXT, avg_price DOUBLE)")
        
        #  más directa de insertar desde Polars a DuckDB
        con.register('avg_price_df_temp', avg_price_df)
        con.execute(f"INSERT INTO {TABLE_NAME} SELECT * FROM avg_price_df_temp")

        # --- 2. Aquí para visualizar ---
        context.log.info("Displaying table from DuckDB:")

        # Ejecuta una consulta para seleccionar todo de la tabla
        results_df = con.execute(f"SELECT * FROM {TABLE_NAME} ORDER BY avg_price DESC").fetch_df()
        
        # Muestra el DataFrame de pandas en los logs de Dagster
        context.log.info(f"\n{results_df.to_string()}")