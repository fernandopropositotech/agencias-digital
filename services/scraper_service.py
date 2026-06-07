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
            r"(?:\+55\s?)?(?:\(?\d{2}\)?\s?)?(?:9?\d{4})[- ]?\d{4}",
            html
        )

        return {
            "emails": list(set(emails)),
            "telefones": list(set(telefones))
        }

    except Exception as e:

        return {
            "emails": [],
            "telefones": [],
            "erro": str(e)
        }


def extrair_redes_sociais(url):

    try:

        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        instagram = ""
        linkedin = ""
        facebook = ""

        for link in soup.find_all("a", href=True):

            href = link["href"]

            if "instagram.com" in href:
                instagram = href

            elif "linkedin.com" in href:
                linkedin = href

            elif "facebook.com" in href:
                facebook = href

        return {
            "instagram": instagram,
            "linkedin": linkedin,
            "facebook": facebook
        }

    except Exception:

        return {
            "instagram": "",
            "linkedin": "",
            "facebook": ""
        }