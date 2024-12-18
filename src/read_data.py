import pandas as pd


def read_data():
    # Load each dataset and drop 'Unnamed: 0' if present
    health_ins = pd.read_csv("./data/HealthIns.csv").drop(
        columns=["Unnamed: 0"], errors="ignore"
    )
    med_con = pd.read_csv("./data/MedCon.csv").drop(
        columns=["Unnamed: 0"], errors="ignore"
    )
    immuno = pd.read_csv("./data/Immuno.csv").drop(
        columns=["Unnamed: 0"], errors="ignore"
    )
    hep_q = pd.read_csv("./data/HepQ.csv").drop(columns=["Unnamed: 0"], errors="ignore")
    demo = pd.read_csv("./data/Demo.csv").drop(columns=["Unnamed: 0"], errors="ignore")

    health_ins["SEQN"] = health_ins["SEQN"].astype(int)
    med_con["SEQN"] = med_con["SEQN"].astype(int)
    immuno["SEQN"] = immuno["SEQN"].astype(int)
    hep_q["SEQN"] = hep_q["SEQN"].astype(int)
    demo["SEQN"] = demo["SEQN"].astype(int)

    hep_q["HEQ010"] = hep_q["HEQ010"].apply(lambda x: x == 1).astype(int)

    # Merge datasets on the 'SEQN' column with suffixes
    merged_data = (
        demo.merge(health_ins, on="SEQN", how="left", suffixes=("", "_health"))
        .merge(med_con, on="SEQN", how="left", suffixes=("", "_med"))
        .merge(immuno, on="SEQN", how="left", suffixes=("", "_immuno"))
        .merge(hep_q, on="SEQN", how="left", suffixes=("", "_hep"))
    )
    merged_data = merged_data.dropna(subset=["HEQ010"])
    return merged_data


if __name__ == "__main__":
    merged_data = read_data()
    # Display the shape and first few rows of the merged DataFrame
    print("Merged data shape:", merged_data.shape)
    print(merged_data.head())

    print(merged_data["HEQ010"].unique())
