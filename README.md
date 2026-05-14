# Retail Marketing MMM & Uplift Modeling Platform

Proyecto esqueleto para construir una plataforma end-to-end de **Marketing Mix Modeling (MMM)** y **Uplift Modeling / Incrementality** usando como base el dataset público **Store Item Demand Forecasting** y una capa de marketing adicional local o sintética.

> **Propósito del repositorio**
> Este proyecto está diseñado como **ejercicio de portafolio** para demostrar habilidades de data science senior / ML aplicado a marketing analytics, causal inference, time series, MLOps y software quality.
> No está pensado como sistema productivo final ni requiere licencias empresariales o servicios de pago.

---

## Qué demuestra este proyecto
- Forecasting y análisis temporal orientado a ventas retail
- Marketing Mix Modeling (adstock, saturation, contribución, ROI)
- Uplift modeling / heterogeneous treatment effects
- Diseño de datasets causales y contrafactuales
- Orquestación con Airflow
- Experiment tracking y model registry con MLflow
- Data quality, monitoring y governance
- Testing para mantenimiento y evolución futura

## Restricciones consideradas
### 1. Sin licencias de pago
La arquitectura se apoya en herramientas open source y ejecución local.

### 2. Sin subir CSV raw al repositorio
La data raw se descarga manualmente y se mantiene fuera del control de versiones.

### 3. Testing para mantenimiento futuro
El repo ya incluye estructura de pruebas unitarias, integración y fixtures sintéticos.

### 4. Limitación importante del dataset base
El dataset de Kaggle está orientado a forecasting de demanda y contiene fundamentalmente `date`, `store`, `item` y `sales`. Para un proyecto de MMM/uplift necesitas **variables adicionales de marketing** (por ejemplo spend, impressions, promos, campañas, grupos treatment/control). Este repo asume una de estas dos opciones:
- **Opción A:** tú aportarás una tabla local de marketing / campañas.
- **Opción B:** generarás una capa sintética de marketing para demostrar metodología causal y de MMM.

---

## Política de datos
**Sí se sube:** código, documentación, DAGs, configs, tests, muestras sintéticas pequeñas.  
**No se sube:** raw CSV, outputs pesados, modelos binarios grandes, credenciales.

Ver también:
- `docs/assumptions_and_constraints.md`
- `docs/testing_strategy.md`
- `docs/implementation_plan_6_weeks.md`

---

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
docker compose up -d
make test
```

---

## Rutas clave
- `data/raw/sales/` → aquí colocas manualmente los CSV de Kaggle
- `data/raw/marketing/` → aquí colocas manualmente tu dataset de campañas / spend si lo tienes
- `data/synthetic/` → aquí puedes generar marketing sintético localmente
- `data/processed/` → salidas intermedias locales
- `data/features/` → featuresets locales
- `docs/implementation_plan_6_weeks.md` → plan principal de trabajo
- `docs/testing_strategy.md` → estrategia de testeo y mantenibilidad
