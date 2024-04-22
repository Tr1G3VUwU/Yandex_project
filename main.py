from flask import Flask, render_template, send_file, make_response

app = Flask(__name__)


@app.route('/pdf')
def pdf():
    pdf_path = 'static/files/file.pdf'
    response = make_response(send_file(pdf_path, as_attachment=True))
    response.headers['Content-Disposition'] = 'inline; filename=file.pdf'
    return response


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
