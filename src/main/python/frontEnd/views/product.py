from flask import Blueprint, render_template, request, redirect

bp = Blueprint(__name__, __name__, template_folder='templates')


def productInfo():
    with open('frontEnd/notes/productInfoJson.json', 'r') as _file:
        jsonData = json.loads(_file.read())
        jsonData["GTX 1080TiDUKE11G OC"]

    _file.close()
    return product



@bp.route('/product', methods=['POST', 'GET'])
def show():
    return render_template('product.html', notes=productInfo)