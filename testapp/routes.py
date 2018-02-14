from flask import *
from testapp import app

from_bd = [1, 2]


@app.route('/')
def main():
        return redirect(url_for('start'))


@app.route('/start')
def start():
        return render_template('Test.html', from_bd="", status="", code_client="")


@app.route('/post', methods=['POST'])
def do_entry():
        try:
                if not request.form['auth']:
                        return render_template('Test.html', res='Введите код клиента!!!')
                if request.form.get('inn'):
                        return render_template('Test.html', res=request.form['inn'] + ' Клиент ' +
                                                                request.form['auth'], code_client=request.form['auth'])
                if request.form.get('search'):
                        return render_template('Test.html', res=request.form['search']+' Клиент ' +
                                                                request.form['auth'], code_client=request.form['auth'])
        except BaseException as e:
                return render_template('Test.html', res=e)
