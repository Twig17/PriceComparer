from flask import Blueprint, render_template
import glob
import json

bp = Blueprint(__name__, __name__, template_folder='templates')


def fetch_notes():
        final_products = []
        productFileList = glob.glob('frontEnd/notes/productInfoJson.json')
        with open(productFileList[0]) as _file:
            jsonData = json.loads(_file.read())

        for model in jsonData.keys():
            final_products.append(model)

        _file.close()
        return final_products


@bp.route('/')
def show():
    return render_template('index.html', notes=fetch_notes())
