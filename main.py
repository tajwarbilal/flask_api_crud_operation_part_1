from flask import Flask, jsonify, json, request

app = Flask(__name__, template_folder='templates')

products = [
                {
                    "id": 1,
                    "title": 'Dune',
                    "price": 'Frankfart'
                },
                {
                    "id": 2,
                    "title": 'shune',
                    "price": 'denman'
                },
                {
                    "id": 3,
                    "title": 'prone',
                    "price": 'shalmun'
                },
                {
                    "id": 4,
                    "title": 'clone',
                    "price": 'cronic'
                }
            ]

@app.route('/products', methods=['GET'])
def get_products():
    serialized = {
        'products':products
    }
    return jsonify(serialized)


@app.route('/products/<int:uid>', methods=['GET'])
def get_product(uid):
    product = next(product for product in products if product["id"] == uid)
    return jsonify(product)

@app.route('/products', methods=['POST'])
def post_product():
    request_json = request.get_json()

    try:
        title = request_json['title']
        price = request_json['price']
    except:
        return "Please provide a title and author", 400

    new_product = {
        'id': products[-1]['id'] + 1, 
        'title':title,
        'price':price
    }

    products.append(new_product)

    serialized = {
        'products':products
    }
    return jsonify(serialized)

if __name__ == '__main__':
    app.run(debug=True)