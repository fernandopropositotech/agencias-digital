from apify_client import ApifyClient
from dotenv import load_dotenv
import os

load_dotenv()

client = ApifyClient(
    os.getenv("APIFY_TOKEN")
)


def filtrar_brasil(dados):

    filtrados = []

    for item in dados:

        address = str(
            item.get("address", "")
        ).lower()

        country = str(
            item.get("country", "")
        ).lower()

        if (
            "brasil" in address
            or "brazil" in address
            or country == "br"
            or country == "brazil"
            or country == "brasil"
        ):
            filtrados.append(item)

    return filtrados


def buscar_agencias_maps():

    run_input = {

        "searchStringsArray": [

            "agencia marketing digital",

            "trafego pago agencia",

            "social media agencia",

            "seo agencia",

            "marketing digital brasil"

        ],

        "locationQuery": "Brazil",

        "maxCrawledPlacesPerSearch": 5

    }

    run = client.actor(
        "2Mdma1N6Fd0y3QEjR"
    ).call(
        run_input=run_input
    )

    dataset_id = run.default_dataset_id

    dados = []

    for item in client.dataset(
        dataset_id
    ).iterate_items():

        dados.append(item)

    return filtrar_brasil(dados)