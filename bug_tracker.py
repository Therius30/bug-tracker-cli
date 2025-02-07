 
from database import get_connection  
from models import create_tables  
import time 

create_tables()

# Funktion zum Erstellen eines neuen Bugs
def create_bug():
    title = input("Titel des Bugs: ")  
    description = input("Beschreibung: ") 
    priority = input("Priorität (Rot, Gelb, Grün): ") 

    connect = get_connection()  # Verbindung zur Datenbank herstellen
    with connect.cursor() as cursor:
        cursor.execute("""
            INSERT INTO bugs (title, description, priority) VALUES (%s, %s, %s)
        """, (title, description, priority))  
        connect.commit()  
    connect.close()  
    print("Bug wurde hinzugefügt!")  

# Funktion zum Abrufen aller Bugs
def list_bugs():
    connect = get_connection()  
    with connect.cursor() as cursor:
        cursor.execute("SELECT * FROM bugs")  # alle Bugs abrufen
        bugs = cursor.fetchall()  # Alle gefundenen Bugs in einer Liste speichern
    connect.close()  
    
    if not bugs:  # Prüfen, ob Bugs vorhanden sind
        print("Keine Bugs gefunden.")
        return
    
    print("\n Liste aller Bugs:")
    for bug in bugs:
        print(f" [{bug['id']}] {bug['title']} - {bug['status']} (Priorität: {bug['priority']})")
    time.sleep(10)
# Aktualisieren des Status eines Bugs
def update_bug():
    list_bugs()  
    time.sleep(10)
    bug_id = input("ID des Bugs, den du aktualisieren willst: ") 
    status = input("Neuer Status (Neu, Bearbeitung , Behoben): ") 

    connect = get_connection()
    with connect.cursor() as cursor:
        cursor.execute("UPDATE bugs SET status = %s WHERE id = %s", (status, bug_id))  # Status aktualisieren
        connect.commit()
    connect.close()
    print("Bug-Status wurde aktualisiert!") 

# Hinzufügen eines Kommentars zu einem Bug
def add_comment():
    list_bugs()  
    time.sleep(10)
    bug_id = input("ID des Bugs, für den du einen Kommentar hinzufügen willst: ")  
    text = input("Kommentartext: ")  

    connect = get_connection()
    with connect.cursor() as cursor:
        cursor.execute("INSERT INTO comments (bug_id, text) VALUES (%s, %s)", (bug_id, text))
        connect.commit()
    connect.close()
    print("Kommentar hinzugefügt!")  

# Anzeigen aller Kommentare zu einem Bug
def list_comments():
    list_bugs()  
    time.sleep(10)
    bug_id = input("ID des Bugs, dessen Kommentare du sehen willst: ") 

    connect = get_connection()
    with connect.cursor() as cursor:
        cursor.execute("SELECT * FROM comments WHERE bug_id = %s", (bug_id,))
        comments = cursor.fetchall()
    connect.close()

    if not comments:  # Prüfen, ob Kommentare vorhanden sind
        print("Keine Kommentare zu diesem Bug gefunden.")
        return

    print("\nKommentare:")
    for comment in comments:
        print(f"{comment['text']}")

# Löschen eines Bugs
def delete_bug():
    list_bugs() 
    time.sleep(10)
    bug_id = input("ID des Bugs, den du löschen möchtest: ") 

    connect = get_connection()
    with connect.cursor() as cursor:
        cursor.execute("DELETE FROM bugs WHERE id = %s", (bug_id,)) 
        connect.commit()
    connect.close()
    print("Bug wurde gelöscht!") 

# Hauptmenü 
def menu():
    while True:
        print("\nBug-Tracking System\n")
        print("1.Bug erstellen")
        print("2.Alle Bugs anzeigen")
        print("3.Bug-Status aktualisieren")
        print("4.Kommentar zu Bug hinzufügen")
        print("5.Kommentare anzeigen")
        print("6.Bug löschen")
        print("7.Beenden")
        
        choice = input("Wähle eine Option: ")  

        if choice == "1":
            create_bug()
        elif choice == "2":
            list_bugs()
        elif choice == "3":
            update_bug()
        elif choice == "4":
            add_comment()
        elif choice == "5":
            list_comments()
        elif choice == "6":
            delete_bug()
        elif choice == "7":
            print("Tschüss!")
            break
        else:
            print("Ungültige Auswahl!")

if __name__ == "__main__":
    menu()
