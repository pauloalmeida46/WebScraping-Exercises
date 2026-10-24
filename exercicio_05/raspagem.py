import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"

resposta = requests.get(URL)
resposta.encoding = "utf-8"
soup = BeautifulSoup(resposta.text, "html.parser")

print("=" * 50)
print("CARDÁPIO")
print("=" * 50)

for secao in soup.find_all("section", class_="secao"):
    categoria = secao.find("h2", class_="categoria").get_text(strip=True)
    print(f"\n### {categoria.upper()} ###")

    for item in secao.find_all("div", class_="item"):
        nome = item.find(class_="nome").get_text(strip=True)
        descricao = item.find(class_="descricao").get_text(strip=True)
        preco = item.find(class_="preco").get_text(strip=True)
        print(f"  {nome} - {preco}")
        print(f"    {descricao}")
