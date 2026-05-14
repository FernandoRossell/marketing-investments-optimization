# Plan de implementación de 6 semanas

> Objetivo: construir un proyecto **portfolio-ready** de **MMM + Uplift Modeling** usando el dataset base **Store Item Demand Forecasting** complementado con una capa de marketing local o sintética, con foco en **time series, causal inference, MLOps, testing y documentación**.

---

## Consideraciones clave antes de empezar

### 1. Sin licencias empresariales
Este plan asume herramientas open source y ejecución local.

### 2. Sin subir los CSV raw al repositorio
La data de ventas y marketing se tratará como insumo local.

### 3. Con testing desde el diseño
El plan incorpora pruebas y validaciones como parte del desarrollo.

### 4. Limitación del dataset base
El dataset de Kaggle está orientado a forecasting y no contiene spend/treatment. Por ello, parte del trabajo senior aquí es **diseñar correctamente la capa de marketing** que hará posible MMM y uplift.

---

## Cómo leer este plan
Cada semana incluye:
- **Qué**: qué debes construir o completar.
- **Por qué**: la razón técnica o estratégica del paso.
- **Para qué**: cómo aporta al objetivo final.
- **Cómo**: una guía breve y práctica.
- **Entregables**
- **Checklist**
- **Criterio de salida**

---

# Semana 1 — Fundaciones, dataset strategy y entendimiento temporal

## Objetivo general
Dejar el repo operable, entender el dataset de ventas, decidir la estrategia de capa de marketing y preparar configuración, calidad y política de datos.

## Archivos foco
- `README.md`
- `.env.example`
- `configs/base.yaml`
- `src/config.py`
- `src/logging_config.py`
- `src/ingestion/load_sales_data.py`
- `src/ingestion/load_marketing_data.py`
- `docs/dataset_strategy.md`
- `docs/data_dictionary_template.md`
- `notebooks/01_sales_eda.md`
- `notebooks/02_marketing_layer_design.md`
- `src/monitoring/data_quality.py`

## Qué hacer
### A. Configurar el proyecto base
**Qué:** centralizar configuración, rutas y logging.  
**Por qué:** evita hardcodes y facilita evolución.  
**Para qué:** cambiar paths, columnas o modos sintético/real sin tocar muchos archivos.  
**Cómo:** completa `.env.example`, YAMLs y módulos base.

### B. Definir la estrategia de dataset
**Qué:** decidir si usarás marketing local o sintético.  
**Por qué:** MMM/uplift no pueden construirse solo con `date/store/item/sales`.  
**Para qué:** convertir un dataset de forecasting en un proyecto serio de marketing analytics.  
**Cómo:** documenta en `docs/dataset_strategy.md` tus supuestos y columnas necesarias.

### C. Entender la serie temporal de ventas
**Qué:** perfilar la señal de ventas.  
**Por qué:** MMM y uplift se apoyan en una base temporal robusta.  
**Para qué:** conocer tendencia, estacionalidad, granularidad y heterogeneidad store-item.  
**Cómo:** resume hallazgos en `notebooks/01_sales_eda.md`.

### D. Definir calidad mínima
**Qué:** crear checks iniciales para ventas y marketing.  
**Por qué:** los problemas temporales y de joins causales son costosos si se detectan tarde.  
**Para qué:** tener una base confiable antes de crear features.  
**Cómo:** implementa runner de calidad y expectations mínimas.

## Entregables
- setup base
- estrategia clara de dataset
- política de no subir data raw
- EDA inicial de ventas
- validaciones mínimas de calidad

## Checklist
- [ ] Completar README y policy de datos.
- [ ] Completar configs base.
- [ ] Implementar módulos de config/logging.
- [ ] Definir estrategia de marketing local vs sintético.
- [ ] Documentar diccionario inicial.
- [ ] Documentar EDA temporal de ventas.
- [ ] Implementar ingestión base y quality checks mínimos.

## Criterio de salida
Ya sabes exactamente cómo vas a convertir el dataset de forecasting en uno apto para MMM/uplift y puedes cargarlo localmente sin errores.

---

# Semana 2 — Capa de marketing, preparación temporal y feature design

## Objetivo general
Construir la base conjunta de ventas + marketing y diseñar las features causales/temporales clave.

## Archivos foco
- `src/simulation/generate_marketing_data.py`
- `src/preprocessing/clean_sales.py`
- `src/preprocessing/clean_marketing.py`
- `src/preprocessing/build_panel_data.py`
- `notebooks/03_feature_design.md`
- `tests/unit/`

## Qué hacer
### A. Construir o limpiar la capa de marketing
**Qué:** preparar spend, promo calendar o treatment flags.  
**Por qué:** sin esta capa no existe el problema de MMM/uplift.  
**Para qué:** habilitar estimación de contribución e incrementality.  
**Cómo:** o bien limpias tablas reales, o generas una capa sintética explícitamente documentada.

### B. Preparar panel temporal conjunto
**Qué:** construir un panel store-item-day o store-day con ventas + marketing.  
**Por qué:** MMM y uplift necesitan un dataset integrado temporalmente.  
**Para qué:** asegurar alineación temporal y granularidad consistente.  
**Cómo:** usa joins por fecha/entidad y valida integridad del panel final.

### C. Diseñar features antes de modelar
**Qué:** decidir lags, ventanas, adstock, saturation, seasonality, controls y treatment features.  
**Por qué:** la calidad del modelado depende de un diseño de variables correcto.  
**Para qué:** construir un pipeline defendible de marketing analytics.  
**Cómo:** documenta en `notebooks/03_feature_design.md` qué harás y por qué.

### D. Añadir primeras pruebas unitarias
**Qué:** probar funciones pequeñas como adstock o joins simples.  
**Por qué:** estas piezas se reutilizarán mucho.  
**Para qué:** reducir regresiones futuras.  
**Cómo:** agrega tests a transforms determinísticos y fixtures sintéticos.

## Entregables
- marketing layer lista
- panel temporal conjunto
- diseño de features documentado
- primeras pruebas unitarias

## Checklist
- [ ] Implementar/generar capa de marketing.
- [ ] Limpiar ventas y marketing.
- [ ] Construir panel temporal conjunto.
- [ ] Diseñar features MMM/uplift.
- [ ] Escribir primeras pruebas unitarias.

## Criterio de salida
Tienes un dataset panel coherente con ventas + marketing y una estrategia clara de features.

---

# Semana 3 — Features de MMM, contrafactual base y dataset causal

## Objetivo general
Construir el featureset final para MMM y uplift, incluyendo baseline temporal/contrafactual inicial.

## Archivos foco
- `src/features/calendar_features.py`
- `src/features/adstock.py`
- `src/features/saturation.py`
- `src/features/lag_features.py`
- `src/features/build_mmm_featureset.py`
- `src/features/build_uplift_dataset.py`
- `tests/unit/`
- `tests/fixtures/`

## Qué hacer
### A. Crear features temporales y controles
**Qué:** calendar, lags, moving averages, trend, estacionalidad.  
**Por qué:** MMM necesita separar marketing de comportamiento base de la serie.  
**Para qué:** evitar atribuir a marketing lo que es tendencia/seasonality.  
**Cómo:** implementa calendar features y lags bien documentados.

### B. Crear transformaciones de medios
**Qué:** adstock y saturation.  
**Por qué:** el efecto de marketing rara vez es lineal e instantáneo.  
**Para qué:** capturar carryover y diminishing returns.  
**Cómo:** implementa funciones reutilizables, parametrizables y testeables.

### C. Construir baseline / contrafactual temporal
**Qué:** una señal base sin marketing o un modelo de control.  
**Por qué:** MMM y uplift se benefician de un benchmark contrafactual.  
**Para qué:** medir incrementalidad sobre algo más sólido que pura correlación.  
**Cómo:** usa un baseline forecasting/regression y deja documentado su rol.

### D. Construir datasets finales
**Qué:** un featureset para MMM y otro dataset para uplift.  
**Por qué:** aunque relacionados, tienen estructuras y objetivos distintos.  
**Para qué:** poder comparar contribución agregada vs efecto individual/segmentado.  
**Cómo:** guarda outputs separados y valídalos con quality checks.

## Entregables
- funciones de adstock/saturation
- features temporales y de control
- baseline/contrafactual inicial
- featureset MMM y dataset uplift
- pruebas unitarias de transforms clave

## Checklist
- [ ] Implementar calendar features.
- [ ] Implementar lags y rolling features.
- [ ] Implementar adstock.
- [ ] Implementar saturation.
- [ ] Construir baseline temporal.
- [ ] Construir dataset MMM.
- [ ] Construir dataset uplift.
- [ ] Escribir tests para transforms clave.

## Criterio de salida
Tienes datasets finales y una base razonable para modelar contribución e incrementality.

---

# Semana 4 — Modelado MMM, uplift y evaluación

## Objetivo general
Entrenar modelos defendibles de MMM y uplift, con métricas correctas y narrativa de negocio.

## Archivos foco
- `src/evaluation/mmm_metrics.py`
- `src/evaluation/uplift_metrics.py`
- `src/evaluation/attribution_analysis.py`
- `src/training/train_mmm_baseline.py`
- `src/training/train_bayesian_mmm.py`
- `src/training/train_uplift_two_model.py`
- `src/training/train_uplift_meta_learners.py`
- `notebooks/04_mmm_results.md`
- `notebooks/05_uplift_results.md`
- `tests/unit/`

## Qué hacer
### A. Estandarizar métricas de MMM
**Qué:** definir cómo evaluar ajuste y capacidad de holdout.  
**Por qué:** sin una capa de métricas común no puedes comparar enfoques.  
**Para qué:** juzgar calidad de contribución y forecast-like fit.  
**Cómo:** implementa MAPE, SMAPE, WMAPE, holdout R² o lo que elijas.

### B. Entrenar MMM baseline y MMM principal
**Qué:** construir un baseline simple y un MMM más robusto (ridge o bayesiano).  
**Por qué:** necesitas una comparación honesta y una narrativa metodológica sólida.  
**Para qué:** estimar contribución de canales y curvas de respuesta.  
**Cómo:** empieza simple y luego añade adstock/saturation más sofisticados.

### C. Entrenar uplift model
**Qué:** construir al menos un enfoque two-model o T-learner.  
**Por qué:** response ≠ incrementality; necesitas estimar efecto diferencial del tratamiento.  
**Para qué:** priorizar persuadables y evitar sure things o sleeping dogs.  
**Cómo:** define treatment, control, outcome y evalúa con AUUC/Qini.

### D. Contar la historia de negocio
**Qué:** traducir resultados a decisiones de marketing.  
**Por qué:** un proyecto senior no termina en métricas.  
**Para qué:** demostrar impacto en budget allocation y targeting policy.  
**Cómo:** documenta contribución, ROI incremental y audiencias prioritarias.

## Entregables
- paquete de métricas MMM/uplift
- baseline MMM y modelo principal
- uplift model funcional
- narrativa inicial de contribución e incrementality
- más pruebas unitarias

## Checklist
- [ ] Implementar métricas MMM.
- [ ] Implementar métricas uplift.
- [ ] Entrenar MMM baseline.
- [ ] Entrenar MMM principal.
- [ ] Entrenar uplift model.
- [ ] Documentar resultados de MMM.
- [ ] Documentar resultados de uplift.
- [ ] Escribir tests de métricas.

## Criterio de salida
Tienes un modelo MMM defendible, un uplift model con evaluación apropiada y puedes convertir ambos en decisiones de marketing.

---

# Semana 5 — Pipelines, MLflow, scoring y optimización

## Objetivo general
Convertir el trabajo analítico en flujos reproducibles con tracking y outputs accionables.

## Archivos foco
- `src/pipelines/mmm_training_pipeline.py`
- `src/pipelines/uplift_training_pipeline.py`
- `src/inference/mmm_scoring.py`
- `src/inference/uplift_scoring.py`
- `src/optimization/budget_allocation.py`
- `scripts/run_mmm_train.py`
- `scripts/run_uplift_train.py`
- `scripts/run_scoring.py`
- `docs/model_card_template.md`
- `tests/integration/`

## Qué hacer
### A. Construir pipelines reproducibles
**Qué:** encapsular entrenamiento MMM y uplift en pipelines claros.  
**Por qué:** reduce dependencia de notebooks y mejora trazabilidad.  
**Para qué:** correr el proyecto end-to-end con comandos simples.  
**Cómo:** usa `src/pipelines/` y scripts de entrada limpios.

### B. Integrar MLflow
**Qué:** registrar params, metrics y artefactos.  
**Por qué:** convierte experimentación dispersa en proceso profesional.  
**Para qué:** demostrar MLOps de forma visible en el repo.  
**Cómo:** loggea datasets, versiones, métricas y gráficos clave.

### C. Implementar scoring y optimización
**Qué:** usar los modelos para recomendar targeting y budget allocation.  
**Por qué:** esto es lo que más acerca el proyecto a decisiones reales de marketing.  
**Para qué:** pasar de análisis a acción.  
**Cómo:** genera scores, rankings de uplift y propuestas de redistribución de gasto.

### D. Añadir integration tests
**Qué:** probar flujos pequeños pero completos.  
**Por qué:** detectan roturas entre módulos más rápido que los unit tests aislados.  
**Para qué:** hacer el repo mantenible.  
**Cómo:** usa fixtures sintéticos y prueba training/scoring smoke tests.

## Entregables
- pipelines reproducibles
- corridas visibles en MLflow
- scoring MMM/uplift funcional
- módulo de optimización inicial
- model card inicial
- integration tests básicos

## Checklist
- [ ] Implementar pipeline de MMM.
- [ ] Implementar pipeline de uplift.
- [ ] Integrar MLflow.
- [ ] Implementar scoring MMM.
- [ ] Implementar scoring uplift.
- [ ] Implementar budget allocation básico.
- [ ] Añadir pruebas de integración.
- [ ] Completar model card.

## Criterio de salida
Puedes correr entrenamiento y scoring con trazabilidad, y ya existen outputs que apoyan targeting y budget allocation.

---

# Semana 6 — Airflow, monitoreo, API y polish final

## Objetivo general
Orquestar el flujo completo, añadir monitoreo básico y dejar el repo listo para mostrarse como pieza de portafolio senior.

## Archivos foco
- `airflow/dags/sales_ingestion_dag.py`
- `airflow/dags/marketing_ingestion_dag.py`
- `airflow/dags/feature_pipeline_dag.py`
- `airflow/dags/mmm_training_dag.py`
- `airflow/dags/uplift_training_dag.py`
- `airflow/dags/scoring_and_budget_dag.py`
- `airflow/dags/monitoring_dag.py`
- `src/monitoring/drift.py`
- `src/monitoring/alerts.py`
- `src/pipelines/monitoring_pipeline.py`
- `api/app.py`
- `tests/unit/`
- `tests/integration/`
- `docs/governance.md`
- `docs/architecture.md`
- `README.md`

## Qué hacer
### A. Conectar DAGs a lógica real
**Qué:** reemplazar placeholders por funciones reales.  
**Por qué:** Airflow debe demostrar orquestación real.  
**Para qué:** cerrar el ciclo datos → features → entrenamiento → scoring → monitoreo.  
**Cómo:** importa funciones desde `src/` o `scripts/` y evita lógica pesada en el DAG.

### B. Implementar monitoreo y drift
**Qué:** medir cambios en ventas, spend, treatments y scores.  
**Por qué:** marketing mix y uplift son sensibles a cambios de estacionalidad y campañas.  
**Para qué:** demostrar madurez de lifecycle y observabilidad.  
**Cómo:** compara referencia vs actual y define umbrales simples de alerta.

### C. Exponer una API mínima
**Qué:** crear endpoints simples para health, model-info y recomendaciones.  
**Por qué:** suma valor curricular y muestra serving básico.  
**Para qué:** exponer scoring o recomendaciones de targeting/budget.  
**Cómo:** implementa schemas y endpoints ligeros en FastAPI.

### D. Completar tests y documentación final
**Qué:** cerrar el proyecto de forma mantenible.  
**Por qué:** un repo fuerte debe ser entendible y modificable.  
**Para qué:** maximizar valor para entrevistas y revisiones técnicas.  
**Cómo:** añade tests finales, actualiza docs y pule README con resultados y limitaciones.

## Entregables
- DAGs conectados
- monitoreo básico
- API mínima funcional
- tests básicos finales
- documentación final robusta

## Checklist
- [ ] Conectar DAGs de ingestión, features, entrenamiento, scoring y monitoreo.
- [ ] Implementar drift y alertas.
- [ ] Implementar monitoring pipeline.
- [ ] Implementar API mínima.
- [ ] Escribir tests finales.
- [ ] Actualizar governance y arquitectura.
- [ ] Hacer polish final del README.

## Criterio de salida
El proyecto ya comunica una solución end-to-end coherente, mantenible y demostrable para MMM + uplift modeling.
