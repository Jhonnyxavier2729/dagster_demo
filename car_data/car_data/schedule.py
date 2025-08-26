import dagster as dg
from .jobs import car_price_job

car_price_schedules = dg.ScheduleDefinition(
    job = car_price_job,
    cron_schedule = "* * * * *", # Ejecutar cada minuto
)
