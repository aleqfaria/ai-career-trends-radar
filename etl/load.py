import pandas as pd

def save_dataframe(df: pd.DataFrame, path: str, format: str = "csv"):
    """
    Salva um DataFrame como CSV ou JSON.

    Args:
        df (pd.DataFrame): O DataFrame a ser salvo.
        path (str): Caminho do arquivo de saída.
        format (str): Formato de saída: "csv" ou "json".
    """
    try:
        if format == "csv":
            df.to_csv(path, index=False, encoding="utf-8")
            print(f"[LOAD] CSV salvo com sucesso: {path}")
        elif format == "json":
            df.to_json(path, orient="records", force_ascii=False, indent=4)
            print(f"[LOAD] JSON salvo com sucesso: {path}")
        else:
            raise ValueError(f"Formato '{format}' não suportado. Use 'csv' ou 'json'.")
    except Exception as e:
        print(f"[ERRO] Falha ao salvar arquivo: {e}")