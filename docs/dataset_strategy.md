# Estrategia de dataset para MMM / Uplift

## Problema
El dataset base de ventas no trae variables de marketing suficientes para un ejercicio causal completo.

## Estrategias válidas
### Opción A: Marketing local
Agregar tablas locales con:
- spend por canal
- promo calendar
- impressions/clicks
- treatment/control por campaña

### Opción B: Marketing sintético
Generar una capa sintética con:
- spend por canal
- campañas activas por store-item o store-day
- treatment assignment
- response heterogénea simulada

## Recomendación de portfolio
Si usas capa sintética, documenta con transparencia:
- qué columnas simulaste
- con qué lógica
- qué supuestos introdujiste
- qué partes son reales vs sintéticas
