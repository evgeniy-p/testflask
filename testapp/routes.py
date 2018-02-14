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
                if not request.form['client_code']:
                        return render_template('Test.html', res='Введите код клиента!!!')
                if request.form.get('text_sumb_form'):
                        return render_template('Test.html', res=request.form['text_sumb_form'] + ' Клиент ' +
                                                                request.form['client_code'], code_client=request.form['client_code'])
                if request.form.get('searchbutt'):
                        return render_template('Test.html', res=request.form['searchbutt']+' Клиент ' +
                                                                request.form['client_code'], code_client=request.form['client_code'])
        except BaseException as e:
                return render_template('Test.html', res=e)
          