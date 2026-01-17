# biblioteca_proyecto
Aplicación de gestion de una biblioteca con ***Django***.

## Modelos

### Libros
Representa los libros de la biblioteca

- 'id': clave UUID autogenerada única de identificación
- 'titulo': titulo del libro
- 'autores': autores del libro, pueden ser varios
- 'fecha_publicacion': fecha de publicación del libro
- 'isbn': número internacional normalizado del libro.

Relaciones:
- Un libro puede tener varios autores

### Autor

- 'id': clave autogenerada de ifentificación
- 'nombre': nombre del autor.
- 'apellido': apellidos del auto
- 'fecha_nacimiento': fecha de nacimiento del autor
- 'nacionalidad': pais de nacimiento del autor

Relaciones:
- Pertenece a un libro ('Foreignkey' a 'Libro')

## Mapa de URLs

El sistema de navegación de la aplicación está definido en `urls.py`, conectando las direcciones del navegador con las funciones lógicas de las vistas.

| Ruta | Nombre | Función Asociada | Descripción |
| :--- | :--- | :--- | :--- |
| `/` | `inicio` | `views.inicio` | Página de bienvenida de la biblioteca. |
| `/libros/` | `lista_libros` | `views.lista_libros` | Listado completo de libros registrados. |
| `/autores/` | `lista_autores` | `views.lista_autores` | Listado de todos los autores en la base de datos. |
| `/busqueda/` | `busquedalibro` | `views.libros_por_autor` | Interfaz de búsqueda manual por nombre y apellido. |
| `/insertarlibro/` | `insertar_libro` | `views.insertar_libro` | Formulario para la creación de nuevos libros. |
| `/insertarautor/` | `insertar_autor` | `views.insertar_autor` | Formulario para el registro de nuevos autores. |

---

## Vistas y Formularios (Lógica de Negocio)

### Vistas (`views.py`)

El archivo `views.py` gestiona la lógica de la aplicación, controlando el flujo de datos entre los modelos y las plantillas.

### Visualización de Listados
* **`inicio(request)`**: Renderiza la página principal del sitio (`inicio.html`).
* **`lista_libros(request)`**: Consulta todos los registros del modelo `Libro` y los muestra en una tabla organizada.
* **`lista_autores(request)`**: Recupera y muestra la relación completa de autores registrados.

### Gestión de Formularios (Inserción)
Estas vistas utilizan el método `POST` para procesar y validar datos antes de guardarlos en la base de datos:
* **`insertar_libro(request)`**: Gestiona el formulario `LibroForm`. Si los datos son válidos, guarda el nuevo libro y redirige al listado general de libros.
* **`insertar_autor(request)`**: Utiliza `AutorForm` para dar de alta nuevos autores, redirigiendo al listado de autores tras un registro exitoso.

### Motor de Búsqueda
* **`libros_por_autor(request)`**: 
    * Implementa una búsqueda manual procesada por el formulario `BusquedaAutorForm`.
    * **Lógica**: Obtiene el nombre y apellido del autor, busca el objeto coincidente y filtra los libros asociados mediante la relación `autores`.
    * **Seguridad**: Incluye manejo de excepciones con `try/except` para capturar errores de tipo `Autor.DoesNotExist` si los términos de búsqueda no coinciden con ningún registro.

### Formularios (`forms.py`)

El archivo `forms.py` define la estructura y validación de los datos de entrada, utilizando tanto formularios basados en modelos (`ModelForm`) como formularios estándar (`Form`).

### Gestión de Contenido
* **`LibroForm`**: 
    * **Tipo**: `ModelForm` (vinculado al modelo `Libro`).
    * **Campos**: `titulo`, `autores`, `fecha_publicacion`, e `isbn`.
    * **Personalización**: 
        * Utiliza un widget de tipo `date` para facilitar la selección de fechas.
        * Implementa `SelectMultiple` para gestionar la relación de múltiples autores por libro.

* **`AutorForm`**:
    * **Tipo**: `ModelForm` (vinculado al modelo `Autor`).
    * **Campos**: `nombre`, `apellido`, `fecha_nacimiento`, y `nacionalidad`.
    * **Personalización**: Incluye un selector de fecha nativo mediante el widget `DateInput`.

### Herramientas de Búsqueda
* **`BusquedaAutorForm`**:
    * **Tipo**: `Form` (formulario estándar de búsqueda).
    * **Propósito**: Captura criterios de filtrado manual para localizar libros por autor.
    * **Campos**: 
        * `nombre`: Texto limitado a 100 caracteres para el nombre del autor.
        * `apellido`: Texto limitado a 100 caracteres para el apellido del autor.
---

## Plantillas (Templates)

La interfaz está dividida en componentes reutilizables dentro de `bibliotecaApp/templates/bibliotecaApp/`:

* **`inicio.html`**: Landing page con diseño visual y acceso rápido.
* **`busquedalibro.html`**: Interfaz de búsqueda que muestra resultados dinámicos.
* **`lista_libros.html` y `lista_autores.html`**: Tablas organizadas para la visualización de datos.
* **`insertar_autor.html` e `insertar_libro.html`**: Formularios de entrada de datos.

---

## Archivos Estáticos (Assets)

Los estilos se gestionan de forma independiente para facilitar el mantenimiento en `static/bibliotecaApp/CSS/`:

* **`inicio.css`**: Gestiona el estilo visual del `main` y la transparencia de la imagen de fondo.
* **`busquedalibros.css`**: Estilos específicos para el formulario de búsqueda.
* **`lista_libros.css` / `lista_autores.css`**: Controlan la alineación de tablas y el diseño de celdas.

---



