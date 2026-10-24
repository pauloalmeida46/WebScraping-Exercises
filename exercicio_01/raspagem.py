import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"

resposta = requests.get(URL)
resposta.encoding = "utf-8"
soup = BeautifulSoup(resposta.text, "html.parser")

print("=" * 50)
print("CATÁLOGO DE CURSOS")
print("=" * 50)

cursos = soup.find_all("div", class_="curso")

for i, curso in enumerate(cursos, start=1):
    nome = curso.find(class_="nome").get_text(strip=True)
    area = curso.find(class_="area").span.get_text(strip=True)
    carga = curso.find(class_="carga-horaria").span.get_text(strip=True)

    print(f"\nCurso {i}: {nome}")
    print(f"  Área: {area}")
    print(f"  Carga horária: {carga}")
    print("  Assuntos estudados:")
    for assunto in curso.find("ul", class_="assuntos").find_all("li"):
        print(f"    - {assunto.get_text(strip=True)}")

print(f"\nTotal de cursos encontrados: {len(cursos)}")
