from services.scraper_service import extrair_contatos

resultado = extrair_contatos(
    "https://v4company.com"
)

print(resultado)