from flask import render_template
from testapp import app



@app.route('/')
@app.route('/index')
def index():
    return render_template('Test.html', title='test', username='Человек')
