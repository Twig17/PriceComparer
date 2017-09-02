from flask import Blueprint, render_template, request, redirect
import random

bp = Blueprint(__name__, __name__, template_folder='templates')


def random_string(length=16):
    final_string = ''
    chars = 'abcdefghijklmnopqrstuvwxyz123456789'

    for i in range(0, length):
        final_string += chars[random.randint(0, len(chars)-1)]

    return final_string


@bp.route('/createNote', methods=['POST', 'GET'])
def show():
    if request.method == 'POST':
        if request.form.get('createNote'):
            text = request.form.get('noteText')

            with open('frontEnd/notes/{}.note'.format(random_string()), 'w+') as _file:
                _file.write(text)

            _file.close()

            return redirect('/')

    return render_template('createNote.html')
