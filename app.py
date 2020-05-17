'''
'''

from flask import Flask,url_for
from flask import render_template
from pygments.formatters import HtmlFormatter
from flaskext.markdown import Markdown

import os
post =os.listdir('templates/blogPost/')

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title = 'Home')

@app.route('/blog')
def blog():
    readmeFile = open("templates/blogPost/markdownTest.md", "r")
    content = ""
    with open("templates/blogPost/markdownTest.md", "r") as f:
        content = f.read()

    # md_template = markdown.markdown(readmeFile.read(), extensions=["fenced_code",'meta'])
    Markdown(app,extensions=["fenced_code",'meta'])
    
    return render_template('blog.html', post=content)


@app.route('/project')
def project():
    return render_template('project.html',title = 'Projects')

if __name__ == '__main__':
    app.run(debug = True)    