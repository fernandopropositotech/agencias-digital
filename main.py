from apify_client import ApifyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = ApifyClient(
    os.getenv("APIFY_TOKEN")
)

print("Conectado")