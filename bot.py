import sqlite3
import difflib

# Conectar a la base de datos
conn = sqlite3.connect('base.db')
c = conn.cursor()

# Crear una tabla para almacenar preguntas y respuestas
c.execute('''CREATE TABLE IF NOT EXISTS base (question TEXT, answer TEXT)''')

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
    print("Aprendido. ¿Puedo ayudarte con algo más?")
    return True

def main():
    print("¡Hola! Soy un bot que puede responder algunas preguntas. Escribe 'salir' para finalizar.")
    
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == 'aprender':
            if not learn():
                break
        elif user_input.lower() == 'salir':
            break
        else:
            response = get_answer(user_input)
            if response:
                print("Bot: " + response)
            else:
                print("Bot: No sé la respuesta. ¿Puedes proporcionarme información?")
                if learn() is False:
                    break

    conn.close()

if __name__ == "__main__":
    main()
