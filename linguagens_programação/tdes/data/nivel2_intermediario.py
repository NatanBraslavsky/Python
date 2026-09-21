import requests
import pandas as pd

CABECALHOS = {"User-Agent": "webPython-TDES/1.0 (atividade academica)"}

CEPS = ["92010-020", "90010-150", "01001-000"]


def exercicio_2_1():
    print("=== Exercicio 2.1: consulta de CEPs no ViaCEP ===")
    resultados = []

    for cep in CEPS:
        cep_limpo = cep.replace("-", "").strip()
        url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
        resposta = requests.get(url, headers=CABECALHOS, timeout=10)
        dados = resposta.json()

        if dados.get("erro"):
            print(f"  CEP {cep} nao encontrado.")
            continue

        resultados.append(dados)
        print(f"  CEP {cep} -> {dados['logradouro']}, {dados['localidade']}/{dados['uf']}")

    df = pd.DataFrame(resultados)
    colunas = ["cep", "logradouro", "bairro", "localidade", "uf"]
    print("\nDataFrame dos CEPs:")
    print(df[colunas].to_string(index=False))
    print()
    return df


def download_seguro(url, caminho_destino):
    try:
        resposta = requests.get(url, headers=CABECALHOS, timeout=10)
        resposta.raise_for_status()
    except requests.exceptions.HTTPError as erro:
        print(f"  Falha HTTP ao baixar {url}: {erro.response.status_code} "
              f"({erro.response.reason}). Verifique o endereco informado.")
        return False
    except requests.exceptions.Timeout:
        print(f"  O servidor demorou demais para responder a {url}. Tente novamente.")
        return False
    except requests.exceptions.RequestException as erro:
        print(f"  Nao foi possivel completar a requisicao para {url}: {erro}")
        return False

    with open(caminho_destino, "wb") as arquivo:
        arquivo.write(resposta.content)

    print(f"  Arquivo salvo em '{caminho_destino}' "
          f"({len(resposta.content)} bytes).")
    return True


def exercicio_2_2():
    print("=== Exercicio 2.2: tratamento de erros com raise_for_status() ===")
    download_seguro(
        "https://jsonplaceholder.typicode.com/posts/999999",
        "nao_deve_existir.txt",
    )
    print()


def exercicio_2_3():
    print("=== Exercicio 2.3: download de imagem binaria ===")
    download_seguro("https://picsum.photos/400/400", "imagem_aleatoria.jpg")
    print()


if __name__ == "__main__":
    exercicio_2_1()
    exercicio_2_2()
    exercicio_2_3()
