# Grupo 8

## Diseño
[Diseño plantillas](https://www.figma.com/file/foeCJgr3Mo0N2j0mOmZZyd/Mi-primer-diseño-en-figma?node-id=0%3A1)

## Como iniciar

- Descargar python de la pagina oficial en [https://python.org/downloads](https://www.python.org/downloads/)

- Instalar python

- Descargar Git de la pagina oficial en [https://git-scm.com/downloads](https://git-scm.com/downloads)

- Instalar Git

- Abrir la ventana de ejecutar tareas con la combinacion `win+r`

- Escribir `cmd`

- Clonar el repositorio con

```cmd
git clone https://github.com/Grupo-8-Mintic-Uninorte/grupo8.git
```

- Ingresar a la carpeta del proyecto

```cmd
cd grupo8/src
```

- Crear un servidor local

```cmd
python -m venv venv
```

- Activar el servidor

```cmd
powershell
.\venv\Scripts\activate
```

- Instalar las dependencias

```cmd
pip install flask Flask-WTF python-dotenv jinja-partials
```

- Iniciar el servidor

```cmd
flask run
```

## Aportes a la aplicación

- ## Estructura de carpetas

```yml
📦grupo8
 ┣ 📂design         # Fase de diseño
 ┃ ┣ 📂diagrams         # creacion de diagramas
 ┃ ┣ 📂production       # documentos producidos
 ┣ 📂src            # Codigo de la aplicacion
 ┃ ┣ 📂controllers      # controladores
 ┃ ┣ 📂static           # documentos estaticos
 ┃ ┃ ┣ 📂css                # hojas de estilos
 ┃ ┃ ┣ 📂fonts              # fuentes
 ┃ ┃ ┣ 📂images             # imagenes
 ┃ ┃ ┗ 📂js                 # scripts
 ┃ ┣ 📂templates    # Plantillas
 ┃ ┃ ┣ 📂components     # plantillas de componentes
 ┃ ┃ ┣ 📂layouts        # plantillas de diseños
 ┃ ┃ ┗ 📂pages          # paginas
 ┃ ┣ 📜.flaskenv    # Variables de desarrollo
 ┃ ┣ 📜app.py       # Inicializador de la aplicacion
 ┃ ┣ 📜routes.py    # rutas necesarias del proyecto
 ┃ ┗ 📜views.py     # definiciones con las vistas
 ┣ 📜.gitignore
 ┣ 📜LICENSE
 ┣ 📜README.md
 ┣ 📜CONTRIB.md
 ┗ 📜.editorconfig  # configuracion básica para el desarrollo
                    # requiere la instalacion de editorconfig en vscode
```

- ## Librerias de flask para ayuda en el desarrollo

- ### [python-dotenv](https://pypi.org/project/python-dotenv/)

  - gestiona los ficheros con extensión ```.env``` donde se encuentran registros del tipo clave-valor, convirtiéndolos en variables de entorno que se pueden leer desde Python

- ### [jinja](https://jinja.palletsprojects.com/en/3.0.x/templates/)

  - motor de plantilla desarrollado en Python. Flask utiliza jinja2 para generar documentos HTML válidos

- ### [Flask-WTF](https://flask-wtf.readthedocs.io/en/latest/)

  - Permite trabajar con la librería WTForm de python, que nos facilita la generación y validación de formularios HTML

- ### [jinja-partials](https://github.com/mikeckennedy/jinja_partials)

  - Extension de jinja usado para reutilizar fragmentos de codigo html

- ## Framework css

  - Para agilizar el proceso de estilos se hace uso de [Bootstrap 5](https://getbootstrap.com/docs/5.1/getting-started/introduction/)

- ## Vistas

  - Al agregar una nueva vista se debe referenciar a una ruta en la carpeta routes
