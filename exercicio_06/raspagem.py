import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"

resposta = requests.get(URL)
resposta.encoding = "utf-8"
soup = BeautifulSoup(resposta.text, "html.parser")

print("=" * 55)
print("AGENDA DE EVENTOS")
print("=" * 55)

for evento in soup.find_all("div", class_="evento"):
    nome = evento.find(class_="nome").get_text(strip=True)
    data = evento.find(class_="data").span.get_text(strip=True)
    horario = evento.find(class_="horario").span.get_text(strip=True)
    local = evento.find(class_="local").span.get_text(strip=True)
    palestrantes = [p.get_text(strip=True) for p in evento.find_all("span", class_="palestrante")]
    link = evento.find("a", class_="inscricao")

    print(f"\n{nome}")
    print(f"  Data:    {data} às {horario}")
    print(f"  Local:   {local}")
    print(f"  Palestrante(s): {', '.join(palestrantes)}")
    print(f"  Inscrição: '{link.get_text(strip=True)}' -> {link['href']}")
    if len(palestrantes) > 1:
        print(f"  * Evento com mais de um palestrante ({len(palestrantes)} palestrantes)")
