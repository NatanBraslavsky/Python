Atividade Prática: Explorando Dados na Web com Python
Nível 1: Básico (URLs, Parâmetros e Cabeçalhos)
Objetivo: Praticar a construção de requisições GET simples, envio de parâmetros e manipulação de cabeçalhos.
Exercício 1.1: Faça uma requisição GET para a API pública do JSONPlaceholder ([https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts)) ou para a API do IBGE.
Exercício 1.2: Utilize o argumento params para filtrar os resultados (por exemplo, buscando apenas o userId igual a 2 ou limitando a quantidade de resultados).
Exercício 1.3: Na sua requisição, inclua um dicionário de cabeçalhos (headers) passando um User-Agent personalizado com o nome do seu projeto.
Exercício 1.4: Imprima na tela o código de status HTTP (status_code) para confirmar o sucesso (código 200) e a URL final montada pelo requests (resposta.url). Lembre-se de sempre utilizar o parâmetro timeout (ex: timeout=10) para evitar que seu código fique travado indefinidamente.
Nível 2: Intermediário (JSON, Erros e Arquivos Binários)
Objetivo: Lidar com formatos de dados reais, criar códigos mais robustos contra falhas e fazer download de mídias.
Exercício 2.1: Crie uma lista com três CEPs diferentes e faça um loop para consultá-los na API do ViaCEP ([https://viacep.com.br/ws/](https://viacep.com.br/ws/){cep}/json/). Utilize o método .json() para converter as respostas e armazene os resultados em um DataFrame do Pandas.
Exercício 2.2: Escreva uma função de download segura utilizando um bloco try/except. Dentro dela, utilize resposta.raise_for_status() para capturar erros HTTP (como 404 ou 500) e imprima uma mensagem amigável caso a requisição falhe.
Exercício 2.3: Faça uma requisição para a URL [https://picsum.photos/400/400](https://picsum.photos/400/400) para baixar uma imagem aleatória. Salve o conteúdo bruto da resposta (acessado através de resposta.content) em um arquivo local com a extensão .jpg utilizando o modo de escrita em bytes ('wb').
Nível 3: Avançado (Webscraping e Ética)
Objetivo: Extrair dados de páginas HTML onde não há APIs estruturadas disponíveis, respeitando as boas práticas.
Exercício 3.1: Antes de fazer a raspagem, faça uma requisição para o arquivo robots.txt do site que deseja acessar para verificar as permissões de acesso, demonstrando responsabilidade ética na coleta de dados.
Exercício 3.2: Acesse o site voltado para estudos de raspagem [https://books.toscrape.com/](https://books.toscrape.com/). Utilize a biblioteca BeautifulSoup com o analisador 'html.parser' para localizar os elementos da página. Extraia o título e o preço dos 5 primeiros livros utilizando métodos como .find() ou .select().
Exercício 3.3: Salve os dados extraídos dos livros em um arquivo CSV utilizando o Pandas.
Exercício 3.4: Escolha uma página da Wikipedia que contenha uma tabela de dados (como listas de países ou populações). Utilize a função pandas.read_html() combinada com io.StringIO() para capturar a tabela da página e transformá-la diretamente em um DataFrame, sem a necessidade de usar o BeautifulSoup.
