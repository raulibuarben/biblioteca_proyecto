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



