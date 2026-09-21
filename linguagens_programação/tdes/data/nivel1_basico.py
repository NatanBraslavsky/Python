import requests

URL_POSTS = "https://jsonplaceholder.typicode.com/posts"

CABECALHOS = {"User-Agent": "webPython-TDES/1.0 (atividade academica)"}

PARAMETROS = {"userId": 2, "_limit": 5}


def exercicio_1_1():
    print("=== Exercicio 1.1: GET simples ===")
    resposta = requests.get(URL_POSTS, timeout=10)
    dados = resposta.json()
    print(f"Total de posts recebidos: {len(dados)}")
    print(f"Primeiro titulo: {dados[0]['title']}")
    print()


def exercicios_1_2_a_1_4():
    print("=== Exercicios 1.2, 1.3 e 1.4: params, headers e status ===")
    resposta = requests.get(
        URL_POSTS,
        params=PARAMETROS,
        headers=CABECALHOS,
        timeout=10,
    )

    print(f"Codigo de status HTTP: {resposta.status_code}")
    print(f"Sucesso (200)? {resposta.status_code == 200}")
    print(f"URL final montada: {resposta.url}")
    print(f"User-Agent enviado: {resposta.request.headers['User-Agent']}")

    posts = resposta.json()
    print(f"\nPosts retornados: {len(posts)}")
    for post in posts:
        print(f"  [userId={post['userId']} id={post['id']}] {post['title']}")
    print()


if __name__ == "__main__":
    exercicio_1_1()
    exercicios_1_2_a_1_4()
