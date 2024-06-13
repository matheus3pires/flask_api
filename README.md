# Projeto Flask API
## Descrição
Este projeto consiste em uma aplicação web desenvolvida com Flask, que fornece duas APIs principais:

1. Uma API para gerenciar uma lista de usuários.
1. Uma API para consumir dados de uma API pública e armazená-los em um banco de dados PostgreSQL.

O projeto utiliza Docker para configurar e executar a segunda API.

## Participantes
* Juliana Antusa
* Matheus Pires
* Ryan Silva

## Estrutura do Projeto
O projeto possui a seguinte estrutura de pastas e arquivos:

flask_api/
  
  │
  
  ├── app.py
  
  ├── hg_api.py
  
  ├── Dockerfile
  
  ├── requirements.txt
  
  └── README.md

## Arquivos
* app.py: Contém o código principal da aplicação Flask para gerenciar usuários.
* hg_api.py: Contém o código da aplicação Flask que integra com a API pública HG Brasil e armazena os dados no PostgreSQL.
* Dockerfile: Define a imagem Docker para a aplicação Flask de integração com a API pública.
* requirements.txt: Lista as dependências do projeto para fácil instalação.
* README.md: Este arquivo, que fornece informações sobre o projeto.

## Dependências
Para executar o projeto, você precisará instalar as seguintes dependências Python:

* Flask
* psycopg2-binary
* requests
Você pode instalar todas as dependências usando o arquivo requirements.txt com o seguinte comando:

   ```sh
   pip install -r requirements.txt
   ```

# Primeira API
## 1. Gerenciamento de Usuários
### Adicionar Usuário
* Rota: /add_user
* Método: POST
* Descrição: Adiciona um novo usuário à lista.
* Corpo da Requisição: JSON
   ```sh
   {
  "username": "JohnDoe",
  "email": "johndoe@example.com",
  "age": 30
  }
   ```

#### Respostas:
* 201 Created: Usuário adicionado com sucesso.
* 400 Bad Request: Erro de validação (campo ausente, username/email duplicado, idade fora do intervalo permitido).
Ex:
![Anotação 2024-06-07 155241](https://github.com/matheus3pires/flask_api/assets/87993331/e4dc2399-b758-47b2-83bd-b18566d89530)
### Listar Usuários
* Rota: /users
* Método: GET
* Descrição: Lista todos os usuários cadastrados.
#### Respostas:
* 200 OK: Lista de usuários em formato JSON.
Ex:
![Anotação 2024-06-07 154705](https://github.com/matheus3pires/flask_api/assets/87993331/fb52db46-22ed-4f83-92e3-e0412f8924f0)

# Segunda API
### Integração com API Pública e Banco de Dados
* URL da API pública: https://api.hgbrasil.com/finance/taxes?key=f39a02e2
     ```sh
   {
  "by": "current",
  "valid_key": true,
  "results": [
    {
      "date": "2024-06-12",
      "cdi": 10.5,
      "selic": 10.5,
      "daily_factor": 1.0003927,
      "selic_daily": 10.4,
      "cdi_daily": 10.4
    }
  ],
  "execution_time": 0,
  "from_cache": true
  }
   ```
### Atualizar Dados da HG Brasil
* Rota: /hgbrasil-data/update
* Método: POST
* Descrição: Consome dados da API HG Brasil e os insere em um banco de dados PostgreSQL.
#### Respostas:
* 200 OK: Dados atualizados com sucesso.
* 400 Bad Request: Erro de validação (JSON inválido).
* 500 Internal Server Error: Erro interno do servidor.

## Executar a API com Docker
Para executar a aplicação usando Docker, siga os passos abaixo:
1. Navegue para o Diretório do Projeto.
2. Construa a Imagem Docker:
   
        docker build -t hg_api_image . 

![Captura de tela 2024-06-12 213920](https://github.com/matheus3pires/flask_api/assets/87993331/03d2a1c2-2911-4aed-843d-a6eba3cf6205)

3. Execute o Container Docker:
   
        docker run -p 5000:5000 hg_api_image

![Captura de tela 2024-06-12 221715](https://github.com/matheus3pires/flask_api/assets/87993331/4382992d-5792-453a-b9d3-72852bd73b54)
   
       
4. Interaja com o programa:
   * Uma vez que o container esteja em execução, o container irá subir o servidor Flask  com Docker, faça a requisição POST para popular o banco de dados.
   * A aplicação será executada localmente em http://127.0.0.1:5000
![Captura de tela 2024-06-12 214320](https://github.com/matheus3pires/flask_api/assets/87993331/35f696c6-c4d6-4049-b134-c42e0a600f8e)
![Captura de tela 2024-06-13 132319](https://github.com/matheus3pires/flask_api/assets/87993331/32fe5383-b8df-4505-b6f8-0a6a8204b3b3)

## Agradecimentos:
Agradecemos a todos os participantes por suas contribuições valiosas para o desenvolvimento deste projeto. Cada um de vocês desempenhou um papel crucial na criação e aprimoramento deste trabalho.
* Juliana Antusa: Sua expertise técnica e atenção aos detalhes foram fundamentais para a implementação das funcionalidades do projeto.
* Matheus Pires: Sua criatividade e capacidade de resolução de problemas contribuíram significativamente para a superação dos desafios encontrados durante o desenvolvimento.
* Ryan Silva: Sua dedicação e trabalho árduo garantiram o bom funcionamento do projeto e a entrega de resultados de alta qualidade.

O sucesso deste projeto é resultado do trabalho em equipe e da colaboração entre todos os participantes. Agradecemos a todos por sua paixão e compromisso com o projeto.
