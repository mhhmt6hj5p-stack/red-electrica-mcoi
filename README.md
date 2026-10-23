# Red eléctrica · MCOI — versión de consulta

Copia pública de la aplicación Streamlit. Permite consultar seis escenarios reales ya resueltos, visualizar la red por horas y descargar tablas e informes. No instala gurobipy ni ejecuta Gurobi. Los parámetros y la biblioteca son de solo lectura; la selección de cada visitante es independiente.

## Ejecutar

Python 3.12. Instalar `requirements.txt` y ejecutar `streamlit run web.py`.

## Publicar gratuitamente

Streamlit Community Cloud: seleccionar este repositorio, rama `main`, archivo `web.py`, Python 3.12. No requiere secretos ni licencia de Gurobi.

El archivo App.py se conserva sin cambios para leer parámetros, duración y topología. La interfaz no llama a sus funciones de resolución. Las soluciones e informes conservan su fecha, parámetros, huellas y verificaciones de la ejecución original.

Para actualizar los resultados hay que resolver en la aplicación local y publicar una nueva instantánea validada. No se generan resultados nuevos en la web.

`consulta.zip` incluye el código y las instantáneas validadas; `web.py` lo abre en una carpeta temporal. No contiene credenciales ni Gurobi.
