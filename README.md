# PROYECTO SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS
## MAIN:
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/dd68fb78-98df-4d00-a3e8-501f3a611353)

Este script principal funciona como punto de entrada para el Sistema de Gestión de Activos. 
Dependiendo de la opción seleccionada por el usuario, lo redireccionará al menú correspondiente.


--------------------------------------------------------------------------------------------------
## MENU ACTIVOS:

Al comienzo del código, se incluyen las líneas de importación de las herramientas que serán utilizadas en las diversas operaciones a lo largo de la ejecución del programa.
Estas importaciones aseguran que las funcionalidades necesarias estén disponibles y listas para ser utilizadas en las diferentes partes del código.

### INFORMACIÓN:
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/f59607d8-de17-4e67-b225-0d185b71df7b)

Se llaman los datos de los archivos JSON que serán utilizados a lo largo del código.


### VALIDACIONES:
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/b47b06c5-2af7-4ac3-b9fa-df0e0d82594d)

Funciones que utilizo en la sección de publicar un nuevo activo para prevenir la repetición de datos específicos.


### AGREGAR ACTIVO:
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/a3058710-20ab-4ad4-917a-6b727a561487)

Creo un diccionario vacío y le agrego las llaves junto con sus valores correspondientes para crear el nuevo activo. 
Si alguna validación falla, no es necesario repetir todos los datos, ya que se van guardando mediante la función "if not".


Hay valores que están predefinidos, como por ejemplo "NroItem", que toma el número de ítem del último diccionario que está en el JSON y le suma 1. 
Si falla, es debido a que no se está siguiendo la estructura que debería en el JSON.

![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/5131889f-2e5d-4743-8054-172615fc029a)

Al final, se muestra al usuario el activo que acaba de diseñar y se le pregunta si está seguro de enviarlo a la base de datos.


### EDITAR  ACTIVO:
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/cdd03065-c775-468c-8593-5228a134d3e2)

Primero, se solicita que ingrese el ID del activo que desea editar y se verifica su existencia.
Luego, se muestra el activo y una tabla para que se seleccione qué desea editar. Si la selección es "ID", "idEstado", "Historial" o "asignaciones", se muestra un error ya que esas claves se editarán de otras maneras.
Después de seleccionar la opción que desea editar, se solicita al usuario que ingrese el nuevo valor para esa opción. Luego, se muestra cómo quedaría el activo editado. Finalmente, se pregunta si desea guardar la modificación.


### ELIMINAR ACTIVO ( DAR DE BAJA ):
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/b5a89ad2-b407-4c10-a701-1fa0454eff34)


Primero, se solicita que ingrese el ID del activo que desea dar de baja y se verifica su existencia y que no tenga una asignación registrada. Se muestra al usuario el activo y se le pregunta si está seguro de que desea darlo de baja. Al confirmar la acción, se pregunta quién está realizando el movimiento.
El ID ingresado debe estar en la base de datos de personas. Se crea un diccionario al cual se agrega la información para el historial del activo, siendo un movimiento de ID 2 que hace referencia a "Dado de baja". Se envian los cambios y se agrega al historial el movimiento realizado.


### BUSCAR ACTIVO:
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/2c41aeec-55ea-4ffd-a6fb-076b85caa434)

Creé un menú visual con distintas opciones que permiten al usuario buscar un activo específico de diferentes maneras.

![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/0c14bb2b-9345-448c-88ab-a3ca588e0318)

Dependiendo de la opción seleccionada, se dirige al filtro específico que ayuda a mostrar el activo según el dato ingresado.


--------------------------------------------------------------------------------------------------
## MENU PERSONAS:
Al comienzo del código, se incluyen las líneas de importación de las herramientas que serán utilizadas en las diversas operaciones a lo largo de la ejecución del programa.
Estas importaciones aseguran que las funcionalidades necesarias estén disponibles y listas para ser utilizadas en las diferentes partes del código.

![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/2e2b461f-f023-4954-abff-6441ab1fe28b)

Se llaman los datos de los archivos JSON que serán utilizados a lo largo del código.

### VALIDACIONES:
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/56f8d69f-d62b-46c2-a647-8fa36f568674)

Funciones que utilizo en la sección de publicar una nueva persona para prevenir la repetición de datos específicos.

### AGREGAR PERSONA:
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/9f8a4e28-3113-4449-8f9d-50e05c2e69eb)

Inicializo un diccionario vacío y solicito la información de la persona, la cual se añadirá al diccionario si cumple con las validaciones requeridas.

![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/94aafe80-03aa-48d0-99d2-84ed2a926deb)

Para los teléfonos, establezco la estructura que aparece en el JSON y solicito que se ingresen los números necesarios. Una vez validados, el valor "Teléfonos" del diccionario que contiene la información de la persona adquiere el valor de la variable que tiene la estructura de los teléfonos y su información.

Finalmente, se muestra la información de la persona recién creada y se le pregunta al usuario si desea confirmar el envío de esta nueva información a la base de datos.

### EDITAR PERSONA:
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/4432ac63-87f8-403c-8102-0dc154f5aac8)

Se pide que ingrese el ID de la persona que desea editar y se valida que la persona exista, se muestra la informacion de la persona y se muestra una tabla para que seleccione que desea editar.
se pide el nuevo valor y se reemplaza.

![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/de827d89-4299-4182-9eb6-2a619fae3525)

Si la opción seleccionada es "Teléfonos", se despliega una lista para elegir qué teléfono se desea editar. Una vez seleccionado, se solicita el nuevo valor para ese teléfono específico. Luego, se actualiza la ubicación del teléfono con el nuevo valor proporcionado.


Al final, se presenta la información actualizada y se consulta al usuario si desea enviar los cambios a la base de datos.

### ELIMINAR PERSONA:
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/7d7069be-e87e-4dcc-bcd6-c8fddf919fcc)

Se solicita al usuario que ingrese el ID de la persona que desea eliminar. Se verifica mediante un filtro si esa persona tiene algún activo asignado. Si no tiene ningún activo asignado, se muestra la información de la persona y se solicita confirmación para eliminarla.
En caso de que tenga un activo asignado, se muestra un mensaje de error y se impide la eliminación de la persona.

### BUSCAR PERSONA:
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/5ea3d233-02b4-4fc4-9f12-bf3d498bf2ff)

Creé un menú visual con distintas opciones que permiten al usuario buscar una persona específica de diferentes maneras.

![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/d7ed76d3-a153-40c6-836b-8c66db0b9a14)

Dependiendo de la opción seleccionada, se dirige al filtro específico que ayuda a mostrar la persona según el dato ingresado.


--------------------------------------------------------------------------------------------------
## MENU ZONAS:
Al comienzo del código, se incluyen las líneas de importación de las herramientas que serán utilizadas en las diversas operaciones a lo largo de la ejecución del programa.
Estas importaciones aseguran que las funcionalidades necesarias estén disponibles y listas para ser utilizadas en las diferentes partes del código.

![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/1c5cdbed-6ae1-42eb-bb14-d144949bd243)

Se llaman los datos de los archivos JSON que serán utilizados a lo largo del código.

### VALIDACIONES:
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/0563eb58-f098-4c63-9d7a-59b9aee935d3)

Funciones que utilizo en la sección de publicar una nueva zona para prevenir la repetición de datos específicos.

### AGREGAR ZONA:
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/49ac9f51-2ead-4cd1-937c-45d063302f1d)

Inicializo un diccionario vacío y solicito la información de la nueva zona, la cual se añadirá al diccionario si cumple con las validaciones requeridas.
Finalmente, se muestra la información de la zona recién creada y se le pregunta al usuario si desea confirmar el envío de esta nueva información a la base de datos.

### EDITAR ZONA:
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/2f84e6b9-b0c5-4633-8989-669157a36f93)

Se pide que ingrese el ID de la zona que desea editar y se valida que la zona exista, se muestra la informacion de la zona y se muestra una tabla para que seleccione que desea editar.
se pide el nuevo valor y se reemplaza. Al final, se presenta la información actualizada y se consulta al usuario si desea enviar los cambios a la base de datos.

### ELIMINAR ZONA:
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/e3b17279-2cd9-4d97-b243-dcbc4f60362e)

Se solicita al usuario que ingrese el ID de la zona que desea eliminar. Se verifica mediante un filtro si esa zona tiene algún activo asignado. Si no tiene ningún activo asignado, se muestra la información de la zona y se solicita confirmación para eliminarla.
En caso de que tenga un activo asignado, se muestra un mensaje de error y se impide la eliminación de la zona.

### BUSCAR ZONA:
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/916a9eb4-fc0e-43b3-bbc7-513e16a47131)

Creé un menú visual con distintas opciones que permiten al usuario buscar una zona específica de diferentes maneras.

![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/b5490633-b4c5-4a26-8597-53dae05ecdd8)

Dependiendo de la opción seleccionada, se dirige al filtro específico que ayuda a mostrar la zona según el dato ingresado.


--------------------------------------------------------------------------------------------------
## MENU ASIGNACIONES:
Al comienzo del código, se incluyen las líneas de importación de las herramientas que serán utilizadas en las diversas operaciones a lo largo de la ejecución del programa.
Estas importaciones aseguran que las funcionalidades necesarias estén disponibles y listas para ser utilizadas en las diferentes partes del código.

![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/f0cf62fc-74e7-4dd6-9aa0-97754ec60a72)

Se llaman los datos de los archivos JSON que serán utilizados a lo largo del código.

![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/1b80586f-beeb-40e1-bfeb-d840cc697e6a)

Funciones para validar la existencia de una zona o de una persona.

### CREAR ASIGNACION:
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/954e3e20-604e-474f-bc0b-c24248179846)

Se solicita al usuario que ingrese el ID del activo que desea asignar. Se verifica que el activo exista y que no tenga asignaciones previas. Posteriormente, se cambia el estado del activo a "asignado" (ID 1) y se procede a recabar la información de la asignación. 
Se genera un ID automáticamente y se registra la fecha actual. Se consulta al usuario si la asignación es a una persona o a una zona, y se solicita el ID de la persona o zona a la que se está asignando. Se comprueba si la persona o la zona existe en el sistema.

![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/5799abee-6ecf-4428-b26e-d865a7663813)

Se pide confirmacion al usuario de realizar la asignacion. Si la respuesta es si, se pregunta quien realizo la asignacion, luego se crea un diccionario al cual se agrega la información para el historial del activo, siendo un movimiento de ID 1 que hace referencia a "Asignacion".
Se envian los cambios y se agrega al historial el movimiento realizado.

### BUSCAR ASIGNACION:
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/83458a65-0b73-412d-883d-3fecefa1cd37)

Primero, creé una función que genere una lista con todas las asignaciones registradas. Luego, se implementa otra función que devuelva una lista con la asignación específica según el ID o el número de asignación proporcionado.

--------------------------------------------------------------------------------------------------
## MENU REPORTES:
Al comienzo del código, se incluyen las líneas de importación de las herramientas que serán utilizadas en las diversas operaciones a lo largo de la ejecución del programa.
Estas importaciones aseguran que las funcionalidades necesarias estén disponibles y listas para ser utilizadas en las diferentes partes del código.

![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/0c7096f3-3f8a-49cd-8e4c-725b756ca0c5)

Se llaman los datos de los archivos JSON que serán utilizados a lo largo del código.

![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/4627514f-3c0d-4989-a7c7-71992d89252a)

Creé un menú visual con distintas opciones que permiten al usuario ver los reportes de los activos, sus historiales o sus asiganciones.

![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/cce2ceae-9d06-4787-aa50-05a9c4bd704b)

Si el usuario elige la primera opción, será dirigido al filtro que muestra toda la información de todos los activos registrados en la base de datos.

![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/d3259685-e999-4748-9139-c0c9afb80497)

Si elige la segunda opción, se desplegará una tabla con las categorías registradas. Al seleccionar una categoría, se mostrarán todos los activos que estén asociados a esa categoría en particular.

![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/4b68da52-f3e1-4c80-a88d-1cd87f921102)

En caso de seleccionar la tercera opción, el usuario será redirigido al filtro que presenta toda la información de los activos registrados con el estado de ID 2 (Dado de baja).

![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/b9a8442b-b1c6-4f7f-9275-29f92de1a403)

En caso de seleccionar la cuarta opción, se extraerán todas las asignaciones registradas y se añadirá el nombre y el ID del activo al que pertenecen.

![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/79507e4d-c15c-476d-87ff-cbfaf05eda96)

Por último, si selecciona la última opción, se solicitará al usuario que ingrese el ID del activo del cual desea visualizar el historial.


--------------------------------------------------------------------------------------------------
## MENU MOVIMIENTO DE ACTIVOS:
Al comienzo del código, se incluyen las líneas de importación de las herramientas que serán utilizadas en las diversas operaciones a lo largo de la ejecución del programa.
Estas importaciones aseguran que las funcionalidades necesarias estén disponibles y listas para ser utilizadas en las diferentes partes del código.

![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/b579c354-b944-4c58-bf73-e70d7d6933fd)

Se llaman los datos de los archivos JSON que serán utilizados a lo largo del código.

![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/710987cd-48dd-441a-af4e-0eb8b5867709)

Funciones para validar la existencia de una zona o de una persona.

### RETORNO ACTIVO:
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/d5631b3b-36ad-4053-8c40-7c88849af2d3)

Se solicita al usuario que ingrese el ID del activo que desea retornar. Se verifica que el activo exista y que el estado sea diferente a " No Asigando ". Posteriormente, se cambia el estado del activo a "No asignado" (ID 0) y se procede a mostrar la información del activo. 
Se consulta al usuario si esta seguro de realizar el cambio. Si la respuesta es si, se pregunta quien realizo el retorno, luego se crea un diccionario al cual se agrega la información para el historial del activo, siendo un movimiento de ID 4 que hace referencia a "ReAsignacion" ya que se esta Reasignando el activo a Campus.
Se envian los cambios y se agrega al historial el movimiento realizado.

### DAR DE BAJA ACTIVO:
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/326d1c48-0dbc-4844-b37f-51a7f20095d3)

Primero, se solicita que ingrese el ID del activo que desea dar de baja y se verifica su existencia y que no tenga una asignación registrada. Se muestra al usuario el activo y se le pregunta si está seguro de que desea darlo de baja. Al confirmar la acción, se pregunta quién está realizando el movimiento.
El ID ingresado debe estar en la base de datos de personas. Se crea un diccionario al cual se agrega la información para el historial del activo, siendo un movimiento de ID 2 que hace referencia a "Dado de baja". Se envian los cambios y se agrega al historial el movimiento realizado.


### REASIGNAR:
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/4eb607d1-58f7-473e-bdd5-aba7ff40d73f)

Primero, se solicita que ingrese el ID del activo que desea reasignar y se verifica su existencia y que ya tenga una asignacion registrada. Creé un diccionario donde se va a agregar la nueva informacion de la asignacion,
se genera un ID automáticamente y se registra la fecha actual. Se consulta al usuario si la asignación es a una persona o a una zona, y se solicita el ID de la persona o zona a la que se está asignando. Se comprueba si la persona o la zona existe en el sistema.
Se muestra la nueva asignacion y se pide confirmacion al usuario de realizar la Reasignacion. Si la respuesta es si, se pregunta quien realizo la Reasignacion, luego se crea un diccionario al cual se agrega la información para el historial del activo, siendo un movimiento de ID 4 que hace referencia a "ReAsignacion".
Se envian los cambios y se agrega al historial el movimiento realizado.


### ENVIAR A GARANTIA:
![image](https://github.com/CristianDavidFajardoRojas/Proyecto-SISTEMA-DE-GESTION-DE-INVENTARIO-CAMPUSLANDS/assets/160773269/67d47ceb-51ed-45a5-8718-22f653c6624d)

Primero, se solicita que ingrese el ID del activo que desea enviar a garantia y se verifica su existencia y que no tenga una asignación registrada. Se muestra al usuario el activo y se le pregunta si está seguro de que desea enviarlo a garantia. Al confirmar la acción, se pregunta quién está realizando el movimiento.
El ID ingresado debe estar en la base de datos de personas. Se crea un diccionario al cual se agrega la información para el historial del activo, siendo un movimiento de ID 3 que hace referencia a "Garantia". Se envian los cambios y se agrega al historial el movimiento realizado.
































