from dagster import Definitions, load_assets_from_modules

from car_data import assets # noqa: TID252
from . import activos_filtros
from . import count_cars
from .jobs import car_price_job
from .schedule import car_price_schedules

all_assets = load_assets_from_modules([assets,activos_filtros,count_cars])
all_jobs = [car_price_job]
all_schedules = [car_price_schedules]

defs = Definitions(
    assets=all_assets,
    jobs=all_jobs,
    schedules=all_schedules,
)
