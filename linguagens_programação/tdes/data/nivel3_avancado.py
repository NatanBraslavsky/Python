import io

import requests
import pandas as pd
from bs4 import BeautifulSoup

CABECALHOS = {"User-Agent": "webPython-TDES/1.0 (atividade academica)"}

SITE_LIVROS = "https://books.toscrape.com/"
URL_WIKIPEDIA = "https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o"


def exercicio_3_1(url_base=SITE_LIVROS):
    print("=== Exercicio 3.1: verificacao do robots.txt ===")
    url_robots = url_base.rstrip("/") + "/robots.txt"

    resposta = requests.get(url_robots, headers=CABECALHOS, timeout=10)
    print(f"  URL consultada: {resposta.url} (status {resposta.status_code})")

    if resposta.status_code == 404:
        print("  O site nao publica robots.txt; nenhuma regra explicita de bloqueio.")
    else:
        print("  Conteudo do robots.txt:")
        for linha in resposta.text.strip().splitlines():
            print(f"    {linha}")
    print()


def exercicio_3_2():
    print("=== Exercicio 3.2: raspagem com BeautifulSoup ===")
    resposta = requests.get(SITE_LIVROS, headers=CABECALHOS, timeout=10)
    resposta.raise_for_status()
    resposta.encoding = "utf-8"

    sopa = BeautifulSoup(resposta.text, "html.parser")
    artigos = sopa.select("article.product_pod")[:5]

    livros = []
    for artigo in artigos:
        titulo = artigo.find("h3").find("a")["title"]
        preco = artigo.find("p", class_="price_color").get_text(strip=True)
        livros.append({"titulo": titulo, "preco": preco})
        print(f"  {titulo} - {preco}")

    print()
    return livros


def exercicio_3_3(livros, caminho="livros.csv"):
    print("=== Exercicio 3.3: exportacao para CSV ===")
    df = pd.DataFrame(livros)
    df.to_csv(caminho, index=False, encoding="utf-8-sig")
    print(f"  {len(df)} livros salvos em '{caminho}'.")
    print(df.to_string(index=False))
    print()
    return df


def exercicio_3_4():
    print("=== Exercicio 3.4: tabela da Wikipedia com read_html() ===")
    resposta = requests.get(URL_WIKIPEDIA, headers=CABECALHOS, timeout=10)
    resposta.raise_for_status()

    tabelas = pd.read_html(io.StringIO(resposta.text))
    print(f"  Tabelas encontradas na pagina: {len(tabelas)}")

    df = max(tabelas, key=len)
    print(f"  Tabela escolhida: {df.shape[0]} linhas x {df.shape[1]} colunas")
    print("\n  Primeiras 10 linhas:")
    print(df.head(10).to_string())

    df.to_csv("populacao_paises.csv", index=False, encoding="utf-8-sig")
    print("\n  Tabela salva em 'populacao_paises.csv'.")
    print()
    return df


if __name__ == "__main__":
    exercicio_3_1()
    livros = exercicio_3_2()
    exercicio_3_3(livros)
    exercicio_3_4()
