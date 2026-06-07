import requests
import re
from bs4 import BeautifulSoup


def extrair_contatos(url):

    try:
        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        html = response.text

        emails = re.findall(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            html
        )

        telefones = re.findall(
            r"\(?\d{2}\)?\s?\d{4,5}-?\d{4}",
            html
        )

        return {
            "emails": list(set(emails)),
            "telefones": list(set(telefones))
        }

    except Exception as e:
        return {
            "erro": str(e)
        }