# Agenda de Contactos Personal

## 📋 Descripción del Proyecto

Una aplicación web desarrollada en Django para gestionar contactos personales de manera eficiente y organizada. Permite almacenar, buscar, editar y eliminar contactos con validaciones robustas de datos.

## ✨ Características Principales

- **Gestión Completa de Contactos**: Crear, leer, actualizar y eliminar contactos (CRUD)
- **Búsqueda Avanzada**: Buscar contactos por nombre, correo o teléfono
- **Validaciones de Datos**: 
  - Validación de formato de correo electrónico
  - Validación de formato de teléfono
  - Verificación de integridad de datos
- **Interfaz Moderna**: Diseño responsive con Tailwind CSS
- **Estructuras de Decisión**: Implementación de lógica condicional para validaciones

## 🛠 Tecnologías Utilizadas

- **Backend**: Django 5.2.6
- **Frontend**: HTML5, Tailwind CSS
- **Base de Datos**: SQLite (por defecto)
- **Lenguaje**: Python 3.12+
- **Validaciones**: Expresiones regulares, estructuras de decisión

## 📋 Requisitos del Sistema

### Requisitos Previos
- Python 3.12 o superior
- pip (gestor de paquetes de Python)
- Git (para clonar el repositorio)

### Dependencias del Proyecto

## 🚀 Instalación y Configuración

### 1. Clonar el Proyecto
```bash
git clone <url-del-repositorio>
cd ContactosPersonales
```
### 2. Crear entorno Virtual
```bash
python -m venv venv
```
### 3. Activar entorno  virtual
#### Windows
```bash
venv\Scripts\activate
```
### Linux/Mac
```bash
source venv/bin/activate
```
### 4. Instalar Dependencias
```bash
pip install django==5.2.6
```
### 5. Configurar Base de Datos
```bash
python manage.py makemigrations contactos
python manage.py migrate
```
### 6. Crear Usuario Administrador
```bash
python manage.py createsuperuser
```
### 7. Ejecutar Servidor de Desarrollo

```bash
python manage.py runserver
```
# 📁 Estructura del Proyecto

```txt
ContactosPersonales/
├── contactos/
│   ├── migrations/
│   ├── templates/
│   │   └── contactos/
│   │       ├── base.html
│   │       ├── agregar_contacto.html
│   │       ├── editar_contacto.html
│   │       ├── eliminar_contacto.html
│   │       ├── detalle_contacto.html
│   │       └── lista_contactos.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── ContactosPersonales/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```
# 👥 Uso de la Aplicación
## 1. Lista de Contactos
URL: `http://127.0.0.1:8000/contactos/`

Visualización: Muestra todos los contactos en una tabla ordenada

Búsqueda: Usa la barra de búsqueda para filtrar por nombre, correo o teléfono

Acciones Rápidas: Enlaces para ver, editar o eliminar cada contacto

Estadísticas: Muestra el número total de contactos

## 2. Agregar Nuevo Contacto
URL: `http://127.0.0.1:8000/contactos/agregar/`

Campos del Formulario:

-  Nombre (obligatorio): Mínimo 2 caracteres, solo letras y espacios

-  Teléfono (obligatorio): Formato chileno (+56 9 1234 5678) o variantes

-  Correo Electrónico (obligatorio): Formato de email válido

-  Dirección (opcional): Texto libre

Validaciones Implementadas:

```python
# Validación de correo
patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Validación de teléfono
patron = r'^(\+?56\s?9?\s?)?[0-9]{8,9}$'

# Validación de nombre
if len(nombre.strip()) < 2:
    raise ValidationError('El nombre debe tener al menos 2 caracteres')
```

## 3. Ver Detalles de Contacto
URL: `http://127.0.0.1:8000/contactos/detalle/<id>/`

Muestra información completa del contacto:

- Información de contacto

- Fecha de creación y última modificación

- Botones de acción (editar, eliminar)

## 4. Editar Contacto Existente
URL: `http://127.0.0.1:8000/contactos/editar/<id>/`

- Mismo formulario que "Agregar Contacto"

- Campos pre-cargados con datos existentes

- Mismas validaciones de integridad de datos

## 5. Eliminar Contacto
URL: `http://127.0.0.1:8000/contactos/eliminar/<id>/`

- Página de confirmación antes de eliminar

- Eliminación permanente del contacto

- Redirección a la lista de contactos después de eliminar

# 🔧 Estructuras de Decisión Implementadas

## 1. Validación de Correo Electrónico
```python
def validar_correo(self, correo):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, correo) is not None
```

## 2. Validación de Teléfono
```python
def validar_telefono(self, telefono):
    patron = r'^(\+?56\s?9?\s?)?[0-9]{8,9}$'
    telefono_limpio = telefono.replace(' ', '')
    return re.match(patron, telefono_limpio) is not None
```

## 3. Búsqueda de Contactos
```python
# Estructura de decisión para búsqueda
if query:
    contactos = contactos.filter(
        Q(nombre__icontains=query) | 
        Q(correo__icontains=query) |
        Q(telefono__icontains=query)
    )
```

## 4. Validación de Nombre
```python
def clean_nombre(self):
    nombre = self.cleaned_data['nombre']
    
    # Validar que el nombre solo contenga letras y espacios
    if not all(c.isalpha() or c.isspace() for c in nombre):
        raise forms.ValidationError('El nombre solo puede contener letras y espacios')
    
    # Validar longitud mínima
    if len(nombre.strip()) < 2:
        raise forms.ValidationError('El nombre debe tener al menos 2 caracteres')
    
    return nombre.strip()
```

## 🎨 Interfaz de Usuario
Diseño Responsive
- Tailwind CSS: Framework de CSS utility-first

- Mobile-First: Diseño optimizado para dispositivos móviles

- Componentes Visuales:

- * Tablas responsivas

- * Formularios estilizados

- * Mensajes de alerta

- * Botones con estados hover


## Navegación
- Header: Navegación principal entre secciones

- Breadcrumbs: Indicación de ubicación actual

- Footer: Información de copyright

## 📊 Modelo de Datos

Esquema de la Base de Datos
```python
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=100)
    direccion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
```
## Relaciones
- No hay relaciones con otros modelos (aplicación independiente)

- Cada contacto es un registro único


# 🔒 Validaciones y Seguridad
Validaciones del Lado del Servidor
- Formularios Django: Validación integrada

- Clean Methods: Validación personalizada en modelos

- Expresiones Regulares: Para formatos específicos

## Seguridad
- CSRF Protection: Protección contra Cross-Site Request Forgery

- XSS Protection: Escapado automático de HTML en templates

- SQL Injection: Prevención mediante ORM de Django

# 🧪 Testing
```bash
python manage.py test contactos
```
# 🐛 Solución de Problemas
Problemas Comunes y Soluciones

## 1. Error de migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```

2. Error de importación:

- Verificar que el entorno virtual esté activado

- Verificar la instalación de Django

3. Error de template no encontrado:

- Verificar la estructura de directorios de templates

- Verificar la configuración en settings.py

4. Error de base de datos:

- Ejecutar migraciones pendientes

- Verificar permisos de la base de datos

# 👨‍💻 Autor: Angel Olivares

GitHub: [Github profile]

Email: angel.olivares.rosas@gmail.com


[Github profile]: https://github.com/AngelOlivares842




