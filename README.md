# Lista de Exercícios — HTML, DOM e Beautiful Soup

> **Atividade acadêmica.** Este repositório contém a resolução de uma lista de exercícios proposta em sala de aula, com fins exclusivamente educacionais.

## Sobre a atividade

O objetivo é praticar a montagem de páginas HTML e a raspagem de dados (web scraping) com Python. Cada exercício tem:

- um `index.html` com uma página fictícia, servida localmente;
- um `raspagem.py` que acessa a página com `requests` e extrai os dados com `BeautifulSoup`.

Nenhum site real da Internet é usado: todas as páginas são servidas em `http://127.0.0.1:8000`.

## Exercícios

| Pasta          | Tema                   |
|----------------|------------------------|
| `exercicio_01` | Catálogo de cursos     |
| `exercicio_02` | Loja de informática    |
| `exercicio_03` | Portal de notícias     |
| `exercicio_04` | Biblioteca             |
| `exercicio_05` | Cardápio por categorias|
| `exercicio_06` | Agenda de eventos      |

## Como executar

Instale as dependências:

```
pip install requests beautifulsoup4
```

Para rodar todos os exercícios em sequência (o script sobe o servidor, executa a raspagem e encerra o servidor de cada exercício):

```
python rodar_todos.py
```

No Windows, também dá para dar dois cliques em `rodar_todos.bat`.

Para rodar um exercício sozinho, abra dois terminais dentro da pasta dele:

```
python -m http.server --bind 127.0.0.1 8000
python raspagem.py
```
