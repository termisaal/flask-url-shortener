from flask import Flask, redirect, request

from database import Database


app = Flask(__name__)
db = Database()


@app.route('/')
def index():
    return 'Main page'


@app.route('/<code>')
def redirect_to_url_by_code(code: str):
    if url := db.get_url_by_code(code):
        return redirect(url)
    else:
        return redirect('/')


@app.route('/~', methods=['GET', 'POST'])
def shorten_link():
    if url := request.args.get('url'):
        return 'https://termisaal.ru/' + db.add_url(url)
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run()
