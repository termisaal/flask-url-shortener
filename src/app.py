import os

from flask import Flask, redirect, render_template, request, send_from_directory

from database import Database
from utils import check_and_wrap_url

app = Flask(__name__)
db = Database()


def get_theme():
    return request.cookies.get('theme') or 'dark'


@app.before_request
def before_request():
    if request.path != '/':
        return redirect(request.path.removesuffix('/'))


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')


@app.route('/')
def index():
    return render_template('index.html', theme=get_theme())


@app.route('/<code>')
def redirect_to_url_by_code(code: str):
    if url := db.get_url_by_code(code):
        return redirect(url)
    else:
        return redirect('/')


@app.route('/~', methods=['GET', 'POST'])
def shorten_link():
    if url := request.args.get('url'):
        if url := check_and_wrap_url(url):
            return request.url_root + db.add_url(url)
        return 'Invalid URL'
    return 'Invalid request body'


if __name__ == '__main__':
    app.run()
