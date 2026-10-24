import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"
CATEGORIA_ESCOLHIDA = "Tecnologia"

resposta = requests.get(URL)
resposta.encoding = "utf-8"
soup = BeautifulSoup(resposta.text, "html.parser")

noticias = []
for artigo in soup.find_all("article", class_="noticia"):
    noticias.append({
        "categoria": artigo.find("span", class_="categoria").get_text(strip=True),
        "titulo": artigo.find("h2", class_="titulo").get_text(strip=True),
        "data": artigo.find("time", class_="data").get_text(strip=True),
        "resumo": artigo.find("p", class_="resumo").get_text(strip=True),
        "autor": artigo.find("p", class_="autor").strong.get_text(strip=True),
    })

print("=" * 60)
print("NOTÍCIAS")
print("=" * 60)
for n in noticias:
    print(f"\n[{n['categoria']}] {n['titulo']}")
    print(f"Data:   {n['data']}")
    print(f"Autor:  {n['autor']}")
    print(f"Resumo: {n['resumo']}")
    print("-" * 60)

print(f"\nTítulos da categoria '{CATEGORIA_ESCOLHIDA}':")
for n in noticias:
    if n["categoria"] == CATEGORIA_ESCOLHIDA:
        print(f"- {n['titulo']}")
