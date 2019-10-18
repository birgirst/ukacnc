from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return make_response('hello world!', 200)


@app.route('/_/health')
def health():
    return make_response('', 200)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)
