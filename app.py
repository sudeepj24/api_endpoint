from flask import Flask, jsonify, request
import os

from graphene_flask import GraphQLView

import graphene

app = Flask(__name__)

# Data for Bikes
bikes = [
    {
        "bikeName": "Hero1 Splendor Plus XTEC (Sparkling Beta Blue)",
        "priceEMI": "₹1,598",
        "rating": "6.4",
        "numRatings": "1765",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike1.jpeg"
    },
    {
        "bikeName": "Bajaj Pulsar 150 Neon",
        "priceEMI": "₹1,850",
        "rating": "4.5",
        "numRatings": "1890",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike2.jpeg"
    },
    {
        "bikeName": "Honda CB Shine SP",
        "priceEMI": "₹1,700",
        "rating": "4.3",
        "numRatings": "1520",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike3.jpeg"
    },
    {
        "bikeName": "Yamaha FZ-S V3.0 FI",
        "priceEMI": "₹2,050",
        "rating": "4.6",
        "numRatings": "2100",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike4.jpeg"
    },
    {
        "bikeName": "TVS Apache RTR 160 4V",
        "priceEMI": "₹1,950",
        "rating": "4.4",
        "numRatings": "1620",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike5.jpeg"
    },
    {
        "bikeName": "Suzuki Gixxer SF",
        "priceEMI": "₹2,200",
        "rating": "4.5",
        "numRatings": "2045",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike6.jpeg"
    },
    {
        "bikeName": "Royal Enfield Classic 350",
        "priceEMI": "₹3,500",
        "rating": "4.8",
        "numRatings": "3000",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike7.jpeg"
    },
    {
        "bikeName": "Honda Hornet 2.0",
        "priceEMI": "₹2,150",
        "rating": "4.2",
        "numRatings": "1450",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike8.jpeg"
    },
    {
        "bikeName": "KTM Duke 250",
        "priceEMI": "₹3,150",
        "rating": "4.7",
        "numRatings": "2500",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike9.jpeg"
    },
    {
        "bikeName": "Bajaj Avenger Cruise 220",
        "priceEMI": "₹2,850",
        "rating": "4.5",
        "numRatings": "1800",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike10.jpeg"
    },
    {
        "bikeName": "Yamaha R15 V4",
        "priceEMI": "₹3,200",
        "rating": "4.7",
        "numRatings": "2750",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike11.jpeg"
    },
    {
        "bikeName": "Suzuki Intruder 150",
        "priceEMI": "₹2,000",
        "rating": "4.4",
        "numRatings": "1500",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike12.jpeg"
    },
    {
        "bikeName": "TVS Sport",
        "priceEMI": "₹1,300",
        "rating": "4.2",
        "numRatings": "1100",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike13.jpeg"
    },
    {
        "bikeName": "Royal Enfield Meteor 350",
        "priceEMI": "₹3,400",
        "rating": "4.7",
        "numRatings": "2900",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike14.jpeg"
    },
    {
        "bikeName": "Hero HF Deluxe",
        "priceEMI": "₹1,100",
        "rating": "4.1",
        "numRatings": "950",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike15.jpeg"
    },
    {
        "bikeName": "Bajaj CT 110X",
        "priceEMI": "₹1,200",
        "rating": "4.0",
        "numRatings": "850",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike16.jpeg"
    },
    {
        "bikeName": "Honda Unicorn",
        "priceEMI": "₹1,800",
        "rating": "4.3",
        "numRatings": "1450",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike17.jpeg"
    },
    {
        "bikeName": "Yamaha MT-15",
        "priceEMI": "₹2,750",
        "rating": "4.6",
        "numRatings": "2300",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike18.jpeg"
    },
    {
        "bikeName": "Suzuki Burgman Street",
        "priceEMI": "₹1,550",
        "rating": "4.3",
        "numRatings": "1250",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike19.jpeg"
    },
    {
        "bikeName": "TVS Raider 125",
        "priceEMI": "₹1,500",
        "rating": "4.2",
        "numRatings": "1175",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike20.jpeg"
    },
    {
        "bikeName": "Royal Enfield Himalayan",
        "priceEMI": "₹3,750",
        "rating": "4.8",
        "numRatings": "3200",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike21.jpeg"
    },
    {
        "bikeName": "Hero Passion Pro",
        "priceEMI": "₹1,350",
        "rating": "4.1",
        "numRatings": "1025",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike22.jpeg"
    },
    {
        "bikeName": "Bajaj Platina 110",
        "priceEMI": "₹1,150",
        "rating": "4.0",
        "numRatings": "925",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike23.jpeg"
    },
    {
        "bikeName": "Honda Activa 6G",
        "priceEMI": "₹1,250",
        "rating": "4.2",
        "numRatings": "1350",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike24.jpeg"
    },
    {
        "bikeName": "Yamaha Fascino 125",
        "priceEMI": "₹1,300",
        "rating": "4.2",
        "numRatings": "1450",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike25.jpeg"
    },
    {
        "bikeName": "TVS Jupiter",
        "priceEMI": "₹1,350",
        "rating": "4.1",
        "numRatings": "1150",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike26.jpeg"
    },
    {
        "bikeName": "Suzuki Access 125",
        "priceEMI": "₹1,400",
        "rating": "4.3",
        "numRatings": "1250",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike27.jpeg"
    },
    {
        "bikeName": "Bajaj Dominar 400",
        "priceEMI": "₹3,150",
        "rating": "4.7",
        "numRatings": "2700",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike28.jpeg"
    },
    {
        "bikeName": "Royal Enfield Thunderbird 350X",
        "priceEMI": "₹3,550",
        "rating": "4.6",
        "numRatings": "2800",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike29.jpeg"
    },
    {
        "bikeName": "Honda H'ness CB350",
        "priceEMI": "₹3,100",
        "rating": "4.7",
        "numRatings": "2500",
        "bikeImage": "/content/dam/bajajmall-site/bike_images/bike30.jpeg"
    }
]

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

# Bike JSON data
@app.route('/api/bikes', methods=['GET'])
def get_bikes():
    return jsonify(bikes)

# My name
@app.route('/api/myname', methods=['GET'])
def get_name():
    name = {
        "firstName": "Sudeep",
        "lastName": "Joshi"
    }
    return jsonify(name)

# Step 1: Define the GraphQL schema
class Query(graphene.ObjectType):
    name = graphene.String()
    description = graphene.String()
    status = graphene.String()

            # Step 2: Define resolvers for the fields
            def resolve_name(self, info):
                return "Sample API render"
        
            def resolve_description(self, info):
                return "This is a simple JSON response from a Flask API"
        
            def resolve_status(self, info):
                return "Success"

# Step 3: Create the schema object
schema = graphene.Schema(query=Query)

# Step 4: Add a GraphQL route to the Flask app
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Enable GraphiQL interface
    )
)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
