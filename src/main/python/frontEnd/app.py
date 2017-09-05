from flask import Flask
from frontEnd.views.index import bp as index_bp
from frontEnd.views.createNote import bp as createNote_bp
from frontEnd.views.product import bp as product_bp

app = Flask(__name__)

app.register_blueprint(index_bp)
app.register_blueprint(createNote_bp)
app.register_blueprint(product_bp)
