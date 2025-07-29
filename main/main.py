from dataclasses import dataclass
import requests
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from flask_cors import CORS
from flask_migrate import Migrate
from producer import publish

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://vatsan1993:password@db:3306/main'

CORS(app)

db = SQLAlchemy(app)

@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

    def __repr__(self):
        return f'<Product {self.title}>'

@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='unique_user_product')

@app.route('/api/products')
def index():
    return jsonify(Product.query.all())


@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get('http://docker.for.mac.localhost:8000/api/users')
    publish('product_liked', id)
    data = req.json()

    try:
        productUser = ProductUser(user_id=data['id'], product_id=id)
        db.session.add(productUser)
        db.session.commit()
    except Exception as e:
        print(e)
        abort(400, 'You have already liked this product or an error occurred.')
        return jsonify({'error': str(e)}), 400
    return jsonify({'message': 'Product liked successfully!'}), 200






# migrating database
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)