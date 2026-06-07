import pandas as pd

from services.scraper_service import extrair_contatos
from services.export_service import salvar_csv

dados = pd.read_csv(
    "input_sites.csv"
)

resultado_final = []

for _, linha in dados.iterrows():

    site = linha["site"]

    print(f"Analisando: {site}")

    resultado = extrair_contatos(site)

    resultado_final.append({

        "site": site,

        "email": (
            resultado["emails"][0]
            if resultado.get("emails")
            else ""
        ),

        "telefone": (
            resultado["telefones"][0]
            if resultado.get("telefones")
            else ""
        )

    })

salvar_csv(resultado_final)