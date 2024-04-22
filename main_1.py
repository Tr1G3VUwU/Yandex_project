from flask import Flask, render_template
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/iri', methods=['GET'])
def index():
    The_proposed_title_1 = {}
    The_proposed_title_1['link_1'] = os.path.basename("static\Base_with_manga_and_novel\jujutsu_kaisen")
    The_proposed_title_1['Name_1'] = (
        open('static\Base_with_manga_and_novel\jujutsu_kaisen\Title_name.txt', 'r', encoding="utf-8").readline())
    The_proposed_title_1['Authors_name_1'] = (
        open('static\Base_with_manga_and_novel\jujutsu_kaisen\Authors_name.txt', 'r', encoding="utf-8").readline())
    The_proposed_title_1['Description_of_the_title_1'] = (
        open('static\Base_with_manga_and_novel\jujutsu_kaisen\Description_of_the_title.txt', 'r',
             encoding="utf-8").readline())
    The_proposed_title_1['estimation_1'] = (
        open('static\Base_with_manga_and_novel\jujutsu_kaisen\estimation.txt', 'r', encoding="utf-8").readline())
    The_proposed_title_1['Img_1'] = 'static\Base_with_manga_and_novel\jujutsu_kaisen\img_cover.jpeg'
    return render_template('index.html', **The_proposed_title_1)


@app.route('/jujutsu_kaisen', methods=['GET'])
def bebra():
    lists = ['002_1nZi.jpeg', '003_RrQF.jpeg']
    return render_template('Reading.html', listik = lists)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
