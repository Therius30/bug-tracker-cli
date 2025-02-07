import pymysql
 
def get_connection(): # Funktion Datenbankverbindung
    return pymysql.connect(
        host="localhost", # Host
        user="buguser", # Benutzer
        password="bugpassword", # Passwort
        database="bugtracker", # Datenbankname
        cursorclass=pymysql.cursors.DictCursor # Rückgabe der Abfrage
    )
