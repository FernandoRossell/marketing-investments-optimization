# Market Forecasting & Media Mix Decision Engine

**Caso de negocio:** From Market-Level Forecasting to Budget Allocation via Media Mix Modeling

**Stack:** 

**Autor:** Abel Soto

---

## Visión general

Los equipos de marketing y crecimiento suelen enfrentar decisiones críticas bajo incertidumbre:  
¿En qué mercados invertir? ¿Qué mix de medios priorizar? ¿Cuál será el impacto esperado en ingresos o volumen?

Este proyecto desarrolla un **framework analítico para forecasting por mercados y simulación de decisiones de inversión publicitaria**, utilizando **Media Mix Modeling (MMM)** como eje central. El objetivo es pasar de análisis descriptivo a un **sistema de soporte a decisiones**, capaz de evaluar escenarios y trade-offs reales de negocio.

El enfoque está diseñado para reflejar problemas propios de **equipos senior de analytics en marketing, growth y estrategia comercial**.

---

## Objetivos del proyecto

- Desarrollar un **forecast de ventas / ingresos a nivel mercado** incorporando dinámica temporal y estacionalidad.
- Estimar el impacto incremental de distintos **canales de marketing** usando Media Mix Modeling.
- Descomponer el desempeño por:
  - Tendencias base
  - Estacionalidad
  - Inversión en medios
- Simular **escenarios de inversión** y reasignación de presupuesto entre mercados y canales.
- Evaluar decisiones utilizando métricas de negocio:
  - Revenue incremental
  - ROI
  - Marginal return por canal
- Traducir resultados analíticos en **recomendaciones accionables para la toma de decisiones estratégicas**.

---

## Fuente de los datos

### Dataset principal

El análisis se basa en un dataset público de ventas retail utilizado comúnmente para problemas de **forecasting de demanda** y análisis temporal:

**Store Item Demand Forecasting Dataset**  
- Plataforma: Kaggle  
- Frecuencia: Diaria  
- Nivel de granularidad: Tienda – Producto – Fecha  

El dataset contiene información histórica de ventas a nivel transaccional, incluyendo:
- Fecha
- Identificador de tienda
- Identificador de producto
- Unidades vendidas

Este tipo de dataset es representativo de entornos reales de retail y permite construir series de tiempo robustas para análisis por mercado.

---

### Construcción de mercados

Para los fines de este proyecto, las tiendas se agrupan en **mercados geográficos agregados** (por ejemplo, regiones o clusters de tiendas).  
Este paso permite escalar el análisis desde un nivel operativo hacia un **nivel estratégico**, alineado con decisiones de marketing y asignación presupuestaria.

El proceso incluye:
- Agregación temporal (diaria → semanal o mensual)
- Agregación espacial (tienda → mercado)
- Normalización de series para comparación entre mercados

---

### Variables de marketing (sintéticas)

Dado que los datasets públicos de retail no contienen información de inversión publicitaria, se generan variables de marketing **sintéticas pero realistas**, con el objetivo de habilitar el análisis mediante Media Mix Modeling.

Las variables incluyen:
- Inversión por canal (TV, Digital, Search, Social)
- Distribución temporal del gasto
- Diferencias de intensidad por mercado

Estas variables se construyen bajo supuestos explícitos y rangos razonables, y se utilizan exclusivamente para **simular escenarios de toma de decisión**, no para representar datos reales de una empresa específica.

---

### Justificación del uso de datos sintéticos

El uso de variables sintéticas en el componente de Media Mix Modeling es una práctica común en proyectos demostrativos, dado que:
- Los datos reales de inversión publicitaria suelen ser confidenciales
- La estructura del problema es más relevante que los valores exactos
- Permite evaluar decisiones, trade-offs y escenarios de forma controlada

Todos los supuestos asociados a estas variables son documentados y analizados en secciones posteriores del proyecto.

---

### Variables de marketing (sintéticas pero realistas)

Para el desarrollo del Media Mix Model se generan variables sintéticas documentadas, tales como:
- Inversión por canal (TV, Digital, Search, Social, etc.)
- Intensidad publicitaria
- Lags y efectos carry-over (adstock)

> Estas variables permiten simular un entorno de decisión realista, alineado con prácticas comunes en marketing analytics, sin representar datos específicos de una empresa real.

---

## Enfoque analítico

### Forecasting por mercado

- Modelos de series de tiempo:
  - Baseline estadístico (ARIMA / SARIMAX)
  - Modelos con regresores externos (marketing, estacionalidad)
- Validación temporal estricta
- Evaluación por mercado:
  - Error absoluto y relativo
  - Estabilidad del forecast

El forecast sirve como **baseline contrafactual** para medir impacto incremental.

---

### Media Mix Modeling (MMM)

El MMM busca estimar el impacto causal aproximado de cada canal sobre el resultado de negocio.

Componentes principales:
- Tendencia base
- Estacionalidad
- Variables de marketing con:
  - Adstock
  - Saturación
- Efectos específicos por mercado

El modelo permite responder preguntas como:
- ¿Qué canal genera mayor retorno marginal?
- ¿Dónde existe saturación?
- ¿Qué mercados responden mejor a inversión incremental?

---

### Simulación de escenarios

A partir del modelo estimado, se simulan escenarios como:
- Incremento/reducción de presupuesto total
- Reasignación entre canales
- Reasignación entre mercados

Cada escenario se evalúa usando KPIs de negocio para soportar decisiones estratégicas.

---

## Testing & Validación
*(Sección a completar)*

-  
-  
-  

---

## Análisis de Hot Spots del modelo
*(Sección a completar)*

-  
-  
-  

---

## Supuestos asumidos
*(Sección a completar)*

-  
-  
-  

---

## ¿Dónde se rompen los supuestos?
*(Sección a completar)*

-  
-  
-  

---

## Posible implementación en producción
*(Sección a completar)*

**Arquitectura propuesta**
-  
-  
-  

**Uso por negocio**
-  
-  
-  

---

## Resultados esperados

El sistema permite:

- Forecasts más robustos por mercado
- Cuantificar impacto incremental real de marketing
- Identificar canales y mercados con mayor retorno
- Optimizar la asignación de presupuesto bajo escenarios realistas

> Los valores numéricos dependen de los supuestos y escenarios modelados.

---

## Extensiones futuras

- Modelos jerárquicos entre mercados
- Incorporación de pricing y promociones
- Optimización automática de presupuesto
- Integración con dashboards de decisión ejecutiva

---

## Conclusión

Este proyecto demuestra cómo combinar **forecasting temporal y Media Mix Modeling** para evolucionar desde reporting descriptivo hacia un **motor de simulación y toma de decisiones estratégicas** en marketing.

El foco está en **impacto en negocio, escenarios y trade-offs**, reflejando el trabajo esperado de perfiles senior en marketing analytics y growth.

---