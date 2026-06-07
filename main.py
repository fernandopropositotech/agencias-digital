import pandas as pd

from services.maps_service import buscar_agencias_maps

dados = buscar_agencias_maps()

resultado = []

for item in dados:

    resultado.append({

        "empresa": item.get("title"),

        "site": item.get("website"),

        "telefone": item.get("phone")

    })

df = pd.DataFrame(resultado)

df.to_csv(
    "output/google_maps.csv",
    index=False,
    encoding="utf-8-sig"
)

print(df.head())