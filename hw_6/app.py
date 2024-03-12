from flask import Flask, request, jsonify
from database import db, User, Order, Product
from app import User as UserPydantic, Order as OrderPydantic, Product as ProductPydantic

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db.init_app(app)


'''Работа с пользователями'''


# Создание пользователя
@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(UserPydantic.from_orm(new_user))


# Получение пользователя по ID
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    return jsonify(UserPydantic.from_orm(user))


# Обновление пользователя по ID
@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = User.query.get(user_id)
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return jsonify(UserPydantic.from_orm(user))


# Удаление пользователя по ID
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted'})


'''Работа с заказами'''


# Создание заказа
@app.route('/order', methods=['POST'])
def create_order():
    data = request.json
    new_order = Order(**data)
    db.session.add(new_order)
    db.session.commit()
    return jsonify(OrderPydantic.from_orm(new_order))


# Получение заказа по ID
@app.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get(order_id)
    return jsonify(OrderPydantic.from_orm(order))


# Обновление заказа по ID
@app.route('/order/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.json
    order = Order.query.get(order_id)
    for key, value in data.items():
        setattr(order, key, value)
    db.session.commit()
    return jsonify(OrderPydantic.from_orm(order))


# Удаление заказа по ID
@app.route('/order/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = Order.query.get(order_id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted'})


'''Работа с товаром'''


# Создание товара
@app.route('/product', methods=['POST'])
def create_product():
    data = request.json
    new_product = Product(**data)
    db.session.add(new_product)
    db.session.commit()
    return jsonify(ProductPydantic.from_orm(new_product))


# Получение товара по ID
@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    return jsonify(ProductPydantic.from_orm(product))


# Обновление товара по ID
@app.route('/product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    product = Product.query.get(product_id)
    for key, value in data.items():
        setattr(product, key, value)
    db.session.commit()
    return jsonify(ProductPydantic.from_orm(product))


# Удаление товара по ID
@app.route('/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'})


if __name__ == '__main__':
    app.run(debug=True)
