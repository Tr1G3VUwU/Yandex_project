from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def form_sample():
    return render_template('ADD.html')


app.run(port=8080, host='127.0.0.1')