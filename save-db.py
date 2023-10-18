import sqlite3
import pandas as pd

# Conectar a la base de datos
conn = sqlite3.connect('base.db')
c = conn.cursor()

# Crear una tabla para almacenar preguntas y respuestas
c.execute('''CREATE TABLE IF NOT EXISTS base (question TEXT, answer TEXT)''')

# Función para agregar una pregunta y respuesta a la base de datos
def add_qa_pair(question, answer):
    c.execute("INSERT INTO base VALUES (?, ?)", (question, answer))
    conn.commit()

# Función para extraer datos del archivo Excel y agregarlos a la base de datos
def extract_from_excel(file_path):
    try:
        data = pd.read_excel(file_path)  # Lee el archivo Excel
        for index, row in data.iterrows():
            question = str(row['Pregunta'])  # Asume que la columna se llama 'Pregunta'
            answer = str(row['Respuesta'])   # Asume que la columna se llama 'Respuesta'
            add_qa_pair(question, answer)  # Agrega la pregunta y respuesta a la base de datos
        print("Datos extraídos y agregados a la base de datos con éxito.")
    except Exception as e:
        print(f"Error al extraer datos del archivo Excel: {str(e)}")

def main():
    print("¡Hola! Este script extraerá preguntas y respuestas de un archivo Excel y las agregará a la base de datos del bot.")
    file_path = input("Ruta del archivo Excel: ")
    
    extract_from_excel(file_path)

    conn.close()

if __name__ == "__main__":
    main()
