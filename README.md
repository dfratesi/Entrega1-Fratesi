# Preentrega Trabajo Final
## Requisitos de entrega
- [x] Herencia de HTML
- [x] Por lo menos 3 clases en modelos
- [ ] Un formulario para insertar datos a todas las clases de los modelos
- [x] Un formulario para buscar algo en la BD
- [ ] Readme que indique el orden en el que se prueban las cosas y/o donde están las funcionalidades.

## Equipo
@dfratesi :man_shrugging:

## Instalación en Linux
1. Crear environment
```
python3 -m venv env
```
2. Activar environment
```
source env/bin/activate
```
3. Actualizar pip e instalar Django
```
pip install --upgrade pip

pip install -r requirements.txt
```
4. Ejecutar el servidor
```
./manage.py runserver
```

## URLs
| URL | Descripción |
| --- | --- |
| / | Home del sitio |
| libros/ | Listado de los libros |
| libros/create/ | Formulario para cargar libros |
| libros/_int_/ | Ver detalle de un libro. Se reemplaza _int_ con el _id_ del libro. |