CoreScope es una herramienta de monitoreo de recursos del sistema desarrollada en Python. Permite supervisar en tiempo real el estado del hardware principal y gestionar alertas automáticas basadas en el consumo de recursos.

Características

* Monitoreo de CPU: Seguimiento del porcentaje de uso con intervalos de actualización.
* Gestión de Memoria RAM: Visualización de memoria total, disponible y porcentaje de uso.
* Estado de Disco: Análisis de espacio utilizado y total en la unidad principal.
* Top 5 Procesos: Identificación de las aplicaciones que más memoria RAM están consumiendo actualmente.
* Sistema de Alertas: Registro automático de eventos críticos (uso > 80%) en un archivo alerts.json con marca de tiempo (Timestamp).

Tecnologías Utilizadas

* Lenguaje: Python 3.x
* Librerías: * psutil: Para la extracción de métricas del sistema y procesos.
    * json: Para la persistencia de datos y logs de alertas.
    * datetime: Para la gestión de registros temporales.

Instalación

1. Clona el repositorio:
   git clone [https://github.com/JuanMartinLadychuk/CoreScope.git](https://github.com/JuanMartinLadychuk/CoreScope.git)