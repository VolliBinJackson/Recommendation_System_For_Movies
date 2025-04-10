# 1. Wähle das Basis-Image (Python 3.10 wird hier als Beispiel verwendet)
FROM python:3.10-slim

# 2. Arbeitsverzeichnis im Container festlegen
WORKDIR /app

# 3. Kopiere nur die requirements.txt zuerst, um den Cache zu nutzen (falls sich die Abhängigkeiten nicht oft ändern)
COPY requirements.txt /app/

# 4. Installiere die Abhängigkeiten aus der requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Kopiere den gesamten Code (app, dataset, und tests Ordner)
COPY app /app/app
COPY dataset /app/dataset
COPY tests /app/tests

# 8. Der Befehl, um das Hauptskript auszuführen
CMD ["python", "app/main.py"]
