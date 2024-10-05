# Proyecto_IngChar_MCD_SM-E

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Este proyecto se creó para completar asignaciones dentro de la maestría en ciencia de datos. Se analizará una posible relación entre el campo de salud mental y el de la educación en la población méxicana juvenil. 

**Objetivo**

Nuestro objetivo con este proyecto es lograr encontrar relaciones y/o hallazgos que nos ayuden responder de manera satisfactoria las preguntas: 

*¿ Habrá alguna correlación entre el desempeño acádemico y la salud mental de los estudiantes jovenes?*

*¿ En que parte de la republica es más probable de abandonar la escuela, y/o tener problemas de salud mental?¿Estarán relacionados/vínculados?*

Esperamos poder hallar resolución a estas incognitas y lograr comunicar nuestros hallazgos tanto al público general como directivos del área de educación.

**Acerca de las fuentes de datos**

Para la información relacionada con la educación en México, optamos por utilizar los resultados de encuestas del INEGI y un reporte del SEP de indicadores educativos:
Nos apoyaremos del Censo General de Población y Vivienda de varios años para obtener información georeferencial y temporal sobre la población méxicana que estudia. La Encuesta Nacional sobre Acceso y Permanencia en la Educación (ENAPE) 2021 nos permitrá generar información estadística sobre el acceso y permanencia de la población de 0 a 29 años en el Sistema Educativo Nacional.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
├── helpers            <- Esta carpeta se utiliza para colocar funciones de utilidad
│                         o archivos auxiliares que pueden ser reutilizados en todo el
│                         proyecto.
│        
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         salud_mental-educacion and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── salud_mental-educacion   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes salud_mental-educacion a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

    Instalación y configuración de proyecto

- Instalar pip: https://pypi.org/project/pip/

- Instalar python: https://www.python.org/downloads/

- Con pip crear entorno virtual: python3 -m venv nombre_del_entorno

- Activar entorno virtual: 
    - Windows:
        nombre_del_entorno\Scripts\activate
    - macOS/Linux:
        source nombre_del_entorno/bin/activate

- Ejecutar : pip install -r requirements.txt
 
- Con pip instalar : pip install cookiecutter-data-science
 