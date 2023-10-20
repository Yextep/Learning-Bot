import sqlite3
import difflib
import pandas as pd
import os

# Conectar a la base de datos
conn = sqlite3.connect('base.db')
c = conn.cursor()

# Crear una tabla para almacenar preguntas y respuestas
c.execute('''CREATE TABLE IF NOT EXISTS base (question TEXT, answer TEXT)''')

# Inicializar una lista para almacenar los datos del usuario
user_data = []

# Función para obtener la respuesta de la base de datos o None si no se encuentra
def get_answer(question):
    c.execute("SELECT question, answer FROM base")
    data = c.fetchall()
    best_match = difflib.get_close_matches(question, [row[0] for row in data], n=1, cutoff=0.8)
    if best_match:
        best_match = best_match[0]
        idx = [row[0] for row in data].index(best_match)
        return data[idx][1]
    return None

# Función para que el bot aprenda
def learn():
    question = input("Pregunta: ")
    if question.lower() == 'salir':
        return False
    response = input("Respuesta: ")
    c.execute("INSERT INTO base VALUES (?, ?)", (question, response))
    conn.commit()
    user_data.append([question, response])  # Agregar datos a la lista
    print("Aprendido. ¿Puedo ayudarte con algo más?")
    return True

# Función para cargar datos desde un archivo Excel a la base de datos
def load_from_excel(file_path):
    try:
        data = pd.read_excel(file_path)
        for index, row in data.iterrows():
            question = str(row['Pregunta'])
            answer = str(row['Respuesta'])
            c.execute("INSERT INTO base VALUES (?, ?)", (question, answer))
        conn.commit()
        print("Datos cargados desde el archivo Excel.")
    except Exception as e:
        print(f"Error al cargar datos desde el archivo Excel: {str(e)}")

# Función para guardar datos en un archivo Excel
def save_to_excel(data, file_path):
    try:
        df = pd.DataFrame(data, columns=['Pregunta', 'Respuesta'])
        if os.path.isfile(file_path):
            existing_data = pd.read_excel(file_path)
            updated_data = pd.concat([existing_data, df], ignore_index=True)
            updated_data.to_excel(file_path, index=False)
        else:
            df.to_excel(file_path, index=False)
        print(f"Datos guardados en el archivo Excel '{file_path}'.")
    except Exception as e:
        print(f"Error al guardar datos en el archivo Excel: {str(e)}")

def main():
    print("¡Hola! Soy Tata, tu amigable bot de asistencia ¿En qué puedo ayudarte hoy?. Escribe 'salir' para finalizar.")
    
    # Pregunta al usuario si desea cargar datos desde un archivo Excel
    load_excel = input("¿Desea cargar una base de datos desde un archivo Excel? (si/no): ")
    if load_excel.lower() == 'si':
        file_path = input("¿El archivo Excel está en una ruta específica? (si/no): ")
        if file_path.lower() == 'si':
            excel_file_path = input("Por favor, ingrese la ruta del archivo Excel: ")
        else:
            excel_file_path = 'datos.xlsx'  # Verifica en la ruta actual

        if os.path.isfile(excel_file_path):
            # Cargar datos desde el archivo Excel
            load_from_excel(excel_file_path)
        else:
            print("No se encontró un archivo Excel en la ruta especificada o en la ruta actual. Continuando sin cargar datos.")

    while True:
        user_input = input("Tú: ")
        if user_input.lower() == 'aprender':
            if not learn():
                break
        elif user_input.lower() == 'salir':
            if load_excel.lower() == 'si':
                if user_data:
                    try:
                        save_to_excel(user_data, excel_file_path)
                    except Exception as e:
                        print(f"Error al guardar datos en el archivo Excel: {str(e)}")
            break
        else:
            response = get_answer(user_input)
            if response:
                print("Tata: " + response)
            else:
                print("Tata: No sé la respuesta. ¿Puedes proporcionarme información?")
                # El bot hará una pregunta
                question = user_input
                response = input("Respuesta: ")
                user_data.append([question, response])
                c.execute("INSERT INTO base VALUES (?, ?)", (question, response))
                conn.commit()
                print("Aprendido. ¿Puedo ayudarte con algo más?")

    conn.close()

if __name__ == "__main__":
    main()
