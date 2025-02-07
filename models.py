from database import get_connection

def create_tables():
    connect = get_connection()
    with connect.cursor() as cursor: 
        # Erstellen Tabelle 'bugs'
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bugs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                description TEXT NOT NULL,
                status ENUM('Neu','Bearbeitung','Behoben') DEFAULT 'Neu',
                priority ENUM ('Rot', 'Gelb','Grün') DEFAULT 'Grün'
            )
        """)
        # Erstellen Tabelle 'comments'
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS comments (
            id INT AUTO_INCREMENT PRIMARY KEY,  
            bug_id INT NOT NULL, 
            text TEXT NOT NULL, 
            FOREIGN KEY (bug_id) REFERENCES bugs(id) ON DELETE CASCADE
            )
        """)
        connect.commit() # Änderungen speichern
    connect.close() # Verbindung schließen
