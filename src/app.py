from flask import Flask, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'main page'


@app.route('/<shortened_url>')
def redirect_to_url(shortened_url):
    return redirect(shortened_url)


@app.route('/~', methods=['GET', 'POST'])
def shorten_link():
    if url := request.args.get('url'):
        return url
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run()
