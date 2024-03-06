import sqlite3

def create_database():
    conn = sqlite3.connect('perguntasbd2.db')
    c = conn.cursor()

    # Cria a tabela de perguntas
    c.execute('''
        CREATE TABLE questions (
            id INTEGER PRIMARY KEY,
            question TEXT NOT NULL,
            options TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    ''')

    # Insere algumas perguntas
    c.execute("INSERT INTO questions (question, options, answer) VALUES (?, ?, ?)",
              ("Qual animal é o melhor amigo do homem?\n", "a) Gato\nb) Cachorro\nc) Pássaro\nd) Peixe\n", 'b\n'))
    c.execute("INSERT INTO questions (question, options, answer) VALUES (?, ?, ?)",
              ("Como é a tradução da palavra 'mouse' em português?\n", "a) Gato\nb) Elefante\nc) Rato\nd) Cobra\n", "c\n"))

    conn.commit()
    conn.close()

create_database()