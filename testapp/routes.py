from flask import render_template
from testapp import app


bdposts = [1, 2, 3, 4, 5, 6]

@app.route('/')
@app.route('/index')
def index():
    return render_template('Test.html', bdposts=bdposts)
