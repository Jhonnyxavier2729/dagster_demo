from dagster import Definitions, load_assets_from_modules

from car_data import assets # noqa: TID252
from . import activos_filtros
from . import count_cars

all_assets = load_assets_from_modules([assets,activos_filtros,count_cars])

defs = Definitions(
    assets=all_assets
)
