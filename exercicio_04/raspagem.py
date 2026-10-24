import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"

resposta = requests.get(URL)
resposta.encoding = "utf-8"
soup = BeautifulSoup(resposta.text, "html.parser")

livros = []
for div in soup.find_all("div", class_="livro"):
    palavras = [li.get_text(strip=True) for li in div.find("ul", class_="palavras-chave").find_all("li")]
    livros.append({
        "titulo": div.find(class_="titulo").get_text(strip=True),
        "autor": div.find(class_="autor").span.get_text(strip=True),
        "ano": div.find(class_="ano").span.get_text(strip=True),
        "genero": div.find(class_="genero").span.get_text(strip=True),
        "situacao": div.find(class_="situacao").span.get_text(strip=True),
        "palavras": palavras,
    })

print("=" * 50)
print("ACERVO DA BIBLIOTECA")
print("=" * 50)
for l in livros:
    print(f"\n{l['titulo']}")
    print(f"  Autor:    {l['autor']}")
    print(f"  Ano:      {l['ano']}")
    print(f"  Gênero:   {l['genero']}")
    print(f"  Situação: {l['situacao']}")
    print("  Palavras-chave:")
    for palavra in l["palavras"]:
        print(f"    - {palavra}")

print("\n" + "=" * 50)
print("LIVROS DISPONÍVEIS")
print("=" * 50)
for l in livros:
    if l["situacao"] == "Disponível":
        print(f"- {l['titulo']} ({l['autor']}, {l['ano']})")
