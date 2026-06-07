import pandas as pd

from services.scraper_service import extrair_contatos

dados = pd.read_csv(
    "input_sites.csv"
)

for _, linha in dados.iterrows():

    site = linha["site"]

    print(f"\nAnalisando: {site}")

    resultado = extrair_contatos(site)

    print(resultado)