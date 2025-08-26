#  ETL Automatizado para Análisis de Datos 🚀

Este proyecto implementa un pipeline ETL (Extracción, Transformación y Carga) robusto y automatizado utilizando **Dagster**. El objetivo principal es ingestar datos desde [Menciona la fuente, ej: una API de ventas, archivos CSV, una base de datos], procesarlos para garantizar su calidad y estructura, y finalmente cargarlos en un destino [Menciona el destino, ej: un Data Warehouse como BigQuery, PostgreSQL] para su posterior análisis y visualización.

[<img width="2048" height="1556" alt="image" src="https://github.com/user-attachments/assets/9a336fea-ba36-4761-9b3f-edbebf1cf670" />]

---

## Índice

- [Acerca del Proyecto](#acerca-del-proyecto-)
- [Características Principales](#características-principales-)
- [Stack Tecnológico](#stack-tecnológico-️)
- [Estructura del Proyecto](#estructura-del-proyecto-)
- [Cómo Empezar](#cómo-empezar-)
- [Uso del Pipeline](#uso-del-pipeline-️)
- [Automatización](#automatización-⏰)


---

## Acerca del Proyecto 📊

En el mundo del análisis de datos, la calidad y disponibilidad de la información es crucial. Este proyecto aborda el desafío de recolectar datos crudos de diversas fuentes y transformarlos en un formato limpio, confiable y listo para ser analizado.

Utilizamos **Dagster** como orquestador central debido a su enfoque en el desarrollo local, la observabilidad y la declaración de dependencias explícitas entre los pasos del ETL. Esto nos permite construir pipelines de datos fiables, mantenibles y fáciles de depurar.

El pipeline realiza las siguientes acciones:
1.  **Extracción**: Conecta con [Fuente de datos] y extrae la información más reciente.
2.  **Transformación**: Limpia los datos, enriquece la información, aplica reglas de negocio y los modela para el análisis.
3.  **Carga**: Inserta los datos procesados en [Destino de datos], listos para ser consumidos por herramientas de BI o notebooks de análisis.

---

## Características Principales ✨

- **Orquestación Moderna**: Todo el flujo de trabajo es gestionado por Dagster, permitiendo visualizar el grafo de dependencias (DAG), monitorear ejecuciones y gestionar el estado.
- **Automatización**: El pipeline está programado para ejecutarse automáticamente, asegurando que los datos estén siempre actualizados.
- **Calidad de Datos**: Se implementan validaciones en los pasos de transformación para garantizar la integridad y consistencia de los datos.
- **Modularidad**: El código está organizado en "activos" (assets) de Dagster, lo que facilita la adición de nuevos pasos o la modificación de los existentes.
- **Entorno de Desarrollo Local**: Dagster permite ejecutar y probar todo el pipeline en un entorno local antes de desplegarlo a producción.

---

## Stack Tecnológico ⚙️

- **Lenguaje**: Python 3.9+
- **Orquestador ETL**: Dagster
- **Procesamiento de Datos**: Pandas / Polars 
- **Base de Datos / Data Warehouse**: Duckbd
- **Gestor de Dependencias**: pip / uv

---

