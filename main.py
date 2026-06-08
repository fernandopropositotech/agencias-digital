import pandas as pd

from services.maps_service import buscar_agencias_maps
from services.scraper_service import (
    extrair_contatos,
    extrair_redes_sociais
)

dados = buscar_agencias_maps()

print(f"Total encontrados: {len(dados)}")

resultado = []

for item in dados:

    empresa = item.get("title", "")

    site_url = item.get("website", "")

    telefone = item.get("phone", "")

    cidade = (
        item.get("city")
        or item.get("address")
        or ""
    )

    contatos = {
        "emails": []
    }

    redes = {
        "instagram": "",
        "linkedin": "",
        "facebook": ""
    }

    if site_url:

        contatos = extrair_contatos(site_url)

        redes = extrair_redes_sociais(site_url)

    if redes["instagram"]:

        canal_contato = "Instagram"

    elif telefone:

        canal_contato = "WhatsApp"

    elif contatos["emails"]:

        canal_contato = "Email"

    elif redes["linkedin"]:

        canal_contato = "LinkedIn"

    else:

        canal_contato = ""

    resultado.append({

        "agencia": empresa,

        "cidade": cidade,

        "instagram": redes["instagram"],

        "whatsapp": (
            "Sim"
            if telefone
            else "Não"
        ),

        "site": (
            "Sim"
            if site_url
            else "Não"
        ),

        "site_url": site_url,

        "telefone": telefone,

        "email": (
            contatos["emails"][0]
            if contatos["emails"]
            else ""
        ),

        "linkedin": redes["linkedin"],

        "facebook": redes["facebook"],

        "responsavel": "",

        "nicho_principal": "",

        "canal_contato": canal_contato,

        "status": "Não contatada"

    })

df = pd.DataFrame(resultado)

df.to_csv(
    "output/agencias_qualificadas.csv",
    index=False,
    encoding="utf-8-sig"
)

print(df.head(20))

print(
    "\nArquivo salvo em: output/agencias_qualificadas.csv"
)