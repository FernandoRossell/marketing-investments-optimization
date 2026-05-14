# Arquitectura del proyecto

## Resumen
Arquitectura por capas para separar ventas, marketing, calidad, preparación temporal, feature engineering de MMM/uplift, entrenamiento, serving, monitoreo y reporting.

## Capas
1. Sales data source (`data/raw/sales/`)
2. Marketing data source (`data/raw/marketing/` o `data/synthetic/`)
3. Raw layer
4. Quality layer
5. Time-series preparation layer
6. MMM / Causal Feature layer
7. Training & registry
8. Serving & optimization layer
9. Monitoring

## Principios
- sin licencias empresariales
- sin subir raw data al repo
- separación entre forecasting, MMM y uplift
- testing y documentación desde el diseño
