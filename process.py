
import pandas as pd

def process():
    df = pd.read_csv('/shared/patients_ingested.csv')
    agg = df['diagnosis'].value_counts()
    agg.to_csv('/shared/diagnosis_summary.csv')
    print("Processing complete. Summary written to shared volume.")

if __name__ == "__main__":
    process()
