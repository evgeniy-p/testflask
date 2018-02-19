from flask import *
from testapp import app, mysql
from testapp import table as table_class

html_file = 'Test.html'
from_bd = [1, 2]

@app.route('/')
def main():
        return redirect(url_for('start'))


@app.route('/start')
def start():
        return render_template(html_file, from_bd="", status="", code_client="")


@app.route('/post', methods=['POST'])
def do_entry():
        print('posted:', request.form['auth'])
        if not request.form['auth']:
                return render_template(html_file, res='Введите код клиента!!!', have_text=request.form['inntext'])
        client_id = table_class.Table(request.form['auth'], mysql)
        print('!!!!!!!!!!!!!test', request.form['inntext'])
        try:
                if request.form.get('inn'):
                        if client_id.exist and request.form.get('inntext'):
                                client_id.update(request.form['inntext'])
                        elif request.form.get('inntext'):
                                client_id.create()
                                client_id.update(request.form['inntext'])
                        else:
                                return render_template(html_file, res='Отсутсвует коммент!', code_client=request.form['auth'])
                        return render_template(html_file, res='done', code_client=request.form['auth'])

                if request.form.get('search'):
                        if client_id.exist:
                                result = client_id.search()
                                return render_template(html_file, from_bd=result,
                                                       res=request.form['search'] + ' Клиент ' +
                                                           request.form['auth'], code_client=request.form['auth'])
                        else:
                                return render_template(html_file, res='Такого клиента не существует!')

        except BaseException as e:
                return render_template(html_file, res=e)
