from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Data for users
users_data = [
    {"username": "sudeep", "userid": 1, "password": "1234"},
    {"username": "arjun", "userid": 2, "password": "1234"},
    {"username": "viraj", "userid": 3, "password": "1234"},
    {"username": "tejas", "userid": 4, "password": "1234"},
    {"username": "shivam", "userid": 5, "password": "1234"}
]

# Data for orders
orders_data = [
    {"userid": 1, "orderid": 121},
    {"userid": 2, "orderid": 122},
    {"userid": 3, "orderid": 123},
    {"userid": 4, "orderid": 124},
    {"userid": 5, "orderid": 125}
]

# Endpoint for users
@app.route('/api/users', methods=['GET'])
def get_users():
    username = request.args.get('username')
    password = request.args.get('password')

    if username and password:
        user = next((user for user in users_data if user["username"] == username and user["password"] == password), None)
        if user:
            return jsonify(user)
        else:
            return jsonify({"error": "User not found or incorrect credentials"}), 404

    return jsonify(users_data)

# Endpoint for orders
@app.route('/api/orders', methods=['GET'])
def get_orders():
    userid = request.args.get('userid', type=int)

    if userid is not None:
        user_orders = [order for order in orders_data if order["userid"] == userid]
        if user_orders:
            return jsonify(user_orders)
        else:
            return jsonify({"error": "No orders found for this user"}), 404

    return jsonify(orders_data)

# Sample data
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "name": "Sample API render",
        "description": "This is a simple JSON response from a Flask API",
        "status": "Success"
    }
    return jsonify(data)

# My name
@app.route('/api/myname', methods=['GET'])
def get_name():
    name = {
        "firstName": "Sudeep",
        "lastName": "Joshi"
    }
    return jsonify(name)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
