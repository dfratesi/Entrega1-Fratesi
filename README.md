# Preentrega Trabajo Final

![GitHub language count](https://img.shields.io/github/languages/count/dfratesi/Entrega1-Fratesi)
![GitHub top language](https://img.shields.io/github/languages/top/dfratesi/Entrega1-Fratesi?style=plastic)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=plastic=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=plastic&logo=bootstrap&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=plastic&logo=visual-studio-code&logoColor=white)

## Requisitos de entrega

- [x] Herencia de HTML
- [x] Por lo menos 3 clases en modelos
- [ ] Un formulario para insertar datos a todas las clases de los modelos
- [x] Un formulario para buscar algo en la BD
- [ ] Readme que indique el orden en el que se prueban las cosas y/o donde están las funcionalidades.

## Equipo

@dfratesi :man_shrugging:

## Instalación en Linux

1. Crear entorno

    ```python
    python3 -m venv env
    ```

2. Activar entorno

    ```pyton
    source env/bin/activate
    ```

3. Actualizar pip e instalar Django

    ```python
    pip install --upgrade pip

    pip install -r requirements.txt
    ```

4. Ejecutar el servidor

    ```python
    ./manage.py runserver
    ```

## URLs

| URL | Descripción |
| --- | --- |
| / | Home del sitio |
| libros/ | Listado de los libros |
| libros/create/ | Formulario para cargar libros |
| libros/_int_/ | Ver detalle de un libro. Se reemplaza _int_ con el _id_ del libro. |
| libros/autores/ | Listado de los autores |
| libros/autores/create/ | Formulario para cargar autores |
| libros/autores/_int_/ | Ver detalle de un autor. Se reemplaza _int_ con el _id_ del autor. |
| libros/generos/ | Listado de los géneros literarios |
| libros/generos/create/ | Formulario para cargar géneros |
| libros/generos/_int_/ | Ver detalle de un género literario. Se reemplaza _int_ con el _id_ del género. |
| libros/idiomas/create/ | Formulario para cargar idiomas |
