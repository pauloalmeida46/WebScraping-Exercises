import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"

resposta = requests.get(URL)
resposta.encoding = "utf-8"
soup = BeautifulSoup(resposta.text, "html.parser")

produtos = []
for div in soup.find_all("div", class_="produto"):
    produtos.append({
        "nome": div.find(class_="nome").get_text(strip=True),
        "fabricante": div.find(class_="fabricante").span.get_text(strip=True),
        "categoria": div.find(class_="categoria").span.get_text(strip=True),
        "preco": div.find(class_="preco").span.get_text(strip=True),
        "estoque": div.find(class_="estoque").span.get_text(strip=True),
    })

print("=" * 50)
print("TODOS OS PRODUTOS")
print("=" * 50)
for p in produtos:
    print(f"\n{p['nome']}")
    print(f"  Fabricante: {p['fabricante']}")
    print(f"  Categoria:  {p['categoria']}")
    print(f"  Preço:      {p['preco']}")
    print(f"  Estoque:    {p['estoque']}")

print("\n" + "=" * 50)
print("PRODUTOS DISPONÍVEIS")
print("=" * 50)
for p in produtos:
    if p["estoque"] == "Disponível":
        print(f"- {p['nome']} ({p['fabricante']}) - {p['preco']}")
