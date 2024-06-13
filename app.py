from flask import Flask, request, jsonify
 
app = Flask(__name__)
 
# Lista de usuários (in-memory)
users = []
 
# Função auxiliar para encontrar usuário por username ou email
def find_user_by_username(username):
    return next((user for user in users if user['username'] == username), None)
 
def find_user_by_email(email):
    return next((user for user in users if user['email'] == email), None)
 
# Rota para adicionar um usuário
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    age = data.get('age')
 
    # Verificar se todos os campos são fornecidos
    if not all([username, email, age]):
        return jsonify({'message': 'All fields (username, email, age) are required!'}), 400
 
    # Verificar se o username já existe
    if find_user_by_username(username):
        return jsonify({'message': 'Username already exists!'}), 400
 
    # Verificar se o email já existe
    if find_user_by_email(email):
        return jsonify({'message': 'Email already exists!'}), 400
 
    # Verificar se o usuário é maior de idade e menor que 100 anos
    if age < 18:
        return jsonify({'message': 'User must be at least 18 years old!'}), 400
 
    if age > 100:
        return jsonify({'message': 'User must be less than 100 years old!'}), 400
 
    # Adicionar o usuário à lista
    users.append({'username': username, 'email': email, 'age': age})
    return jsonify({'message': 'User added successfully!'}), 201
 
# Rota para listar todos os usuários
@app.route('/users', methods=['GET'])
def list_users():
    return jsonify(users), 200
 
if __name__ == '__main__':
    app.run(debug=True)