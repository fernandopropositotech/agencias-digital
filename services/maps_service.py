from apify_client import ApifyClient
from dotenv import load_dotenv
import os

load_dotenv()

client = ApifyClient(
    os.getenv("APIFY_TOKEN")
)

def buscar_agencias_maps():

    run_input = {
        "searchStringsArray": [
            "agencia de marketing digital sao paulo"
        ],
        "maxCrawledPlacesPerSearch": 4
    }

    run = client.actor(
        "2Mdma1N6Fd0y3QEjR"
    ).call(
        run_input=run_input
    )

    print(run)

    dataset_id = run.default_dataset_id

    dados = []

    for item in client.dataset(
        dataset_id
    ).iterate_items():

        dados.append(item)

    return dados