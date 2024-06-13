from flask import Flask, jsonify, request
import psycopg2
import json
import requests

app = Flask(__name__)

# Substitua com as credenciais do seu banco de dados PostgreSQL
db_host = "localhost"
db_name = "seu_banco_de_dados"
db_user = "pires"
db_password = "pires"
db_port = 5432

# Chave da API HG Brasil
api_key = "f39a02e2"


def get_hgbrasil_data():
    url = f"https://api.hgbrasil.com/finance/taxes?key={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["valid_key"]:
        return data["results"][0]
    else:
        raise Exception("Chave API inválida")


def save_data_to_postgres(data_json):
    # Carregue os dados do JSON
    try:
        data = json.loads(data_json)
    except json.JSONDecodeError as e:
        raise Exception(f"JSON inválido: {e}")

    # Extraia os valores dos dados (incluindo date, mesmo que não obrigatório)
    date = data.get("date")
    cdi = data["cdi"]
    selic = data["selic"]
    daily_factor = data["daily_factor"]
    selic_daily = data["selic_daily"]
    cdi_daily = data["cdi_daily"]

    # Validação opcional do campo "date" (se necessário)
    if date:
        # Verifique se o formato da data está correto (se necessário)
        # ...

    # Conecte ao banco de dados PostgreSQL
    conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password, port=db_port)
    cursor = conn.cursor()  # Indentation here

    # Verifique se a tabela existe e crie-a se necessário
    cursor.execute("CREATE TABLE IF NOT EXISTS hgbrasil_data (date DATE, cdi NUMERIC, selic NUMERIC, daily_factor NUMERIC, selic_daily NUMERIC, cdi_daily NUMERIC)")

    # Insira os dados na tabela
    cursor.execute("INSERT INTO hgbrasil_data (date, cdi, selic, daily_factor, selic_daily, cdi_daily) VALUES (%s, %s, %s, %s, %s, %s)", (date, cdi, selic, daily_factor, selic_daily, cdi_daily))

    # Confirme a transação e feche a conexão
    conn.commit()
    cursor.close()
    conn.close()


@app.route("/hgbrasil-data/update", methods=["POST"])
def update_hgbrasil_data_api():
    try:
        # Receba os dados da requisição POST
        data_json = request.get_data()

        # Salve os dados no banco de dados
        save_data_to_postgres(data_json)

        return jsonify({"message": "Dados da HG Brasil atualizados com sucesso!"})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
