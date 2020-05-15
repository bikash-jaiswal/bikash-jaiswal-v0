'''
'''
import markdown
import markdown.extensions.fenced_code
import markdown.extensions.codehilite
from flask import Flask,url_for
from flask import render_template
from pygments.formatters import HtmlFormatter

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title = 'Home')

@app.route('/blog')
def blog():
    readmeFile = open("templates/blogPost/markdownTest.md", "r")
    md_template = markdown.markdown(readmeFile.read(), extensions=["fenced_code"])
    # return render_template('blog.html',title = 'Blog')

    # Generate Css for syntax highlighting
    formatter = HtmlFormatter(style="default",full=True,cssclass="codehilite")
    css_string = formatter.get_style_defs()
    md_css_string = "<style>" + css_string + "</style>"
    
    md_template = md_css_string + md_template
    return md_template


@app.route('/project')
def project():
    return render_template('project.html',title = 'Projects')

if __name__ == '__main__':
    app.run(debug = True)    