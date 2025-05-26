
# Batchbasierte Datenarchitektur – Gesundheitsdaten

## Beschreibung
Dieses Projekt zeigt eine einfache, lokal ausführbare Datenarchitektur zur Verarbeitung orthopädischer Patientendaten im Batch-Modus mit Docker Microservices.

## Starten
1. Stelle sicher, dass Docker installiert ist.
2. Im Projektordner:

```
docker-compose up --build
```

Die `ingest`-Service liest `patients.csv`, speichert es in einem Shared Volume. Die `process`-Service wertet die Diagnosen aus.

## Output
`/shared/diagnosis_summary.csv` enthält eine einfache Aggregation der Diagnosen.
