# Bug-Tracking CLI mit Python & MariaDB

## Installation & Nutzung

### 1. Repository klonen
```bash
git clone https://github.com/Therius30/bug-tracker-cli.git
cd bug-tracker-cli
```

### 2. Virtuelle Umgebung erstellen & aktivieren
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### 3. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```

### 4. MariaDB einrichten
1. MariaDB starten
   ```bash
   sudo systemctl start mariadb  # Linux
   net start MariaDB  # Windows
   ```
2. Datenbank & Benutzer erstellen
   ```sql
   CREATE DATABASE bugtracker;
   CREATE USER 'buguser'@'localhost' IDENTIFIED BY 'bugpassword';
   GRANT ALL PRIVILEGES ON bugtracker.* TO 'buguser'@'localhost';
   FLUSH PRIVILEGES;
   ```

### 5. CLI-Tool starten
```bash
python bug_tracker.py
```

## Funktionen

| Funktion | Beschreibung |
|---------|-------------|
| `1` | Neuen Bug erstellen |
| `2` | Alle Bugs abrufen |
| `3` | Status eines Bugs aktualisieren |
| `4` | Kommentar zu einem Bug hinzufügen |
| `5` | Kommentare zu einem Bug anzeigen |
| `6` | Bug löschen |
| `7` | Programm beenden |

## Fehlerbehebung
Falls Probleme auftreten, prüfe Folgendes:

- MariaDB läuft nicht?
  ```bash
  sudo systemctl start mariadb  # Linux
  net start MariaDB  # Windows
  ```
- Fehlermeldung: `ModuleNotFoundError: No module named 'pymysql'`?
  ```bash
  pip install pymysql
  ```
- Datenbankverbindung fehlschlägt?
  ```sql
  SHOW DATABASES;
  ```


 
