import pandas as pd

def id_exists(search_id: int) -> bool:
    df = pd.read_csv("app/data/base_pesquisados.csv")
    return search_id in df["ID ÚNICO - RESPONDENTE"].values
