import pandas as pd

def salvar_csv(dados):

    df = pd.DataFrame(dados)

    df.to_csv(
        "output/agencias.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print("CSV salvo com sucesso!")