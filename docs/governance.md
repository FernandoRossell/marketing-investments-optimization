# Governance y estándares del proyecto

## Reproducibilidad
- configuración centralizada en `configs/`
- variables de entorno desacopladas
- versionado lógico de datasets/features/modelos

## Manejo de datos
- los archivos raw no se suben al repositorio
- los outputs pesados permanecen locales
- si se usa marketing sintético debe quedar explícitamente documentado

## Testing y mantenibilidad
Antes de considerar estable un módulo relevante, idealmente debe tener:
- logging
- contrato de entrada/salida claro
- al menos una prueba útil
- documentación mínima de uso
