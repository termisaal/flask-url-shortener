from flask import Flask, redirect, render_template, request

from database import Database
from utils import check_and_wrap_url

app = Flask(__name__)
db = Database()


@app.route('/')
def index():
    return render_template('index.html')


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
            return 'https://termisaal.ru/' + db.add_url(url)
    return 'Invalid request'


if __name__ == '__main__':
    app.run()
