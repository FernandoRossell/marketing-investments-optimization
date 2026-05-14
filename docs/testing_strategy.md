# Estrategia de testing y mantenibilidad

## Objetivo
Asegurar que el proyecto pueda crecer, modificarse y refactorizarse sin romper el comportamiento esperado.

## Tipos de pruebas
### Unit tests
Funciones pequeñas y determinísticas:
- adstock
- saturation
- calendar features
- metrics MMM
- metrics uplift
- thresholding / targeting policy

### Integration tests
Validan colaboración entre módulos:
- merge ventas + marketing
- generation pipeline de features
- training pipeline de MMM
- training pipeline de uplift
- healthcheck de API

### Data quality checks
Complementan el testeo tradicional:
- unicidad temporal por entidad
- no missing crítico en spend/treatment
- consistencia de ventanas de tiempo
