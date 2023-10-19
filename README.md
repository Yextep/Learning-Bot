# Bot de Aprendizaje con Preguntas y Respuestas en Python

Este bot es capaz de responder preguntas basadas en una base de datos predefinida y también puede **aprender** nuevas preguntas y respuestas.

# Estructura del codigo:

<img align="right" height="400" width="400" alt="GIF" src="https://github.com/Yextep/Attiny85-Ducky/assets/114537444/c6e08da9-b125-44c5-85b3-ed958c36a34d"/>

**Conexión a la base de datos:** En esta sección, establecemos una conexión a la base de datos SQLite y creamos una tabla para almacenar las preguntas y respuestas.

**Función get_answer:** Esta función recibe una pregunta como entrada y busca la mejor coincidencia en la base de datos. Si encuentra una coincidencia, devuelve la respuesta correspondiente. De lo contrario, devuelve None.

**Función learn:** Esta función permite al bot aprender nuevas preguntas y respuestas. El usuario ingresa una pregunta y una respuesta, y la función las inserta en la base de datos.

**Función main:** Esta función es el punto de entrada del programa. Muestra un mensaje de bienvenida y luego entra en un bucle donde espera la entrada del usuario. Dependiendo de la entrada del usuario, el programa puede aprender nuevas preguntas y respuestas, buscar una respuesta en la base de datos o finalizar la ejecución.

**Save-db:** Este es un script que automatiza el aprendizaje del bot con un archivo de excel existente, más abajo están las instrucciones para que te guies.

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
Ejecutamos el bot
```bash
python3 bot.py
```
# Pasar información de un Excel a la base de datos del bot con el script save-db.py

Este es un script que automatiza el aprendizaje del bot con un archivo de excel existente, en el excel debes tener dos columnas, una que diga "Pregunta" y la otra "Respuesta" puedes buscar una cantidad inmensa de preguntas y respuestas para digitar en esas dos columnas, una vez ingresado esos datos en el excel y lo guardes, ejecutas el script save-db.py y colocas la ruta del excel. Automaticamente la información guardada en el excel se pasará a la base de datos del bot, haciendo que aprenda de manera más rapida.

```bash
python3 save-db.py
```
ahí te pedirá la ruta del excel, ejemplo. /home/user/Desktop/Excel.xlsx
