'''
'''
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title = 'Home')

@app.route('/blog')
def blog():
    return render_template('blog.html',title = 'Blog')

@app.route('/project')
def project():
    return render_template('project.html',title = 'Projects')

if __name__ == '__main__':
    app.run(debug = True)    