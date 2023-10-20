# Bot de Aprendizaje con Preguntas y Respuestas en Python

Este bot es capaz de responder preguntas basadas en una base de datos predefinida y también puede **aprender** nuevas preguntas y respuestas.

# Estructura del codigo:

<img align="right" height="400" width="400" alt="GIF" src="https://github.com/Yextep/Attiny85-Ducky/assets/114537444/c6e08da9-b125-44c5-85b3-ed958c36a34d"/>

**Conexión a la base de datos:** En esta sección, establecemos una conexión a la base de datos SQLite y creamos una tabla para almacenar las preguntas y respuestas.

**Función get_answer:** Esta función recibe una pregunta como entrada y busca la mejor coincidencia en la base de datos. Si encuentra una coincidencia, devuelve la respuesta correspondiente. De lo contrario, devuelve None.

**Función learn:** Esta función permite al bot aprender nuevas preguntas y respuestas. El usuario ingresa una respuesta, y la función la inserta en la base de datos.

**Función main:** Esta función es el punto de entrada del programa. Muestra un mensaje de bienvenida y luego entra en un bucle donde espera la entrada del usuario. Dependiendo de la entrada del usuario, el programa puede aprender nuevas preguntas y respuestas, buscar una respuesta en la base de datos o finalizar la ejecución.

# Excel

Este Excel automatiza el aprendizaje del bot, en el excel debes tener dos columnas, una que diga "Pregunta" y la otra "Respuesta" puedes buscar una cantidad inmensa de preguntas y respuestas para digitar en esas dos columnas, una vez ingresado esos datos lo DEBES guardar como **"datos.xlsx"**

# Excel en la misma carpeta del bot

Si tienes el archivo de Excel en la misma carpeta donde está ejecutando el bot, solo debes indicar que sí quieres cargar un Excel pero que no está en una ruta especifica, automaticamente el bot asumirá que el excel estará en la ruta actual del bot y se cargarán dichos datos.

Automaticamente la información guardada en el excel se pasará a la base de datos del bot, y si el bot aprende nuevas respuestas, al momento de ejecutar el comando "salir". Se guardará toda la nueva información que aprendió el bot tanto en la base de datos del bot como en el archivo de Excel.

# Excel en una ruta Especifica

Si tienes el archivo de Excel en una ruta específica, debes indicar que sí quieres cargar un Excel de una ruta especifica y luego indicas en qué ruta está ubicado. Ejemplo:

```bash
/home/user/Desktop/datos.xlsx
```

Automaticamente la información guardada en el excel se pasará a la base de datos del bot, y si el bot aprende nuevas respuestas, al momento de ejecutar el comando "salir". Se guardará toda la nueva información que aprendió el bot tanto en la base de datos del bot como en el archivo de Excel.


## Instalación

Clonamos el repositorio
```bash
git clone https://github.com/Yextep/Learning-Bot
```
Accedemos a la carpeta
```bash
cd Learning-Bot
```
Instalamos requerimientos
```bash
pip install -r requirements.txt
```
Actualizamos la biblioteca xlsxwriter a la última versión compatible con Pandas
```bash
pip install --upgrade xlsxwriter
```
Ejecutamos el bot
```bash
python3 tata.py
```


