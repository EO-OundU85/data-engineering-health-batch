
import shutil
import os

def ingest():
    source = '/data/patients.csv'
    dest = '/shared/patients_ingested.csv'
    os.makedirs('/shared', exist_ok=True)
    shutil.copy(source, dest)
    print("Ingestion complete. Data copied to shared volume.")

if __name__ == "__main__":
    ingest()
