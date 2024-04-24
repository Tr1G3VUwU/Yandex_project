from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/iri', methods=['GET'])
def index():
    con = sqlite3.connect("static\Base_with_manga_and_novel\data.sqlite")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM Manga_DB""").fetchall()
    sorted_list = sorted(result, key=lambda x: x[-1])
    The_proposed_title_1 = {}
    The_proposed_title_1['link_1'] = sorted_list[0][5]
    The_proposed_title_1['Name_1'] = sorted_list[0][2]
    The_proposed_title_1['Authors_name_1'] = sorted_list[0][1]
    The_proposed_title_1['Description_of_the_title_1'] = sorted_list[0][4]
    The_proposed_title_1['estimation_1'] = sorted_list[0][3]
    The_proposed_title_1['Img_1'] = f'static\Base_with_manga_and_novel\{sorted_list[0][6]}\img_cover.jpeg'
    con.close()
    return render_template('index.html', **The_proposed_title_1)


@app.route('/jujutsu_kaisen', methods=['GET'])
def bebra():
    con = sqlite3.connect("static\Base_with_manga_and_novel\data.sqlite")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM Manga_DB""").fetchall()
    result = cur.execute(f"""UPDATE Manga_DB SET Estimation = {result[0][3] + 1} WHERE ID = 1""").fetchall()
    con.close()
    lists = ['002_1nZi.jpeg', '003_RrQF.jpeg']
    return render_template('Reading.html', listik = lists)


if __name__ == '__main__':
    app.run(debug=True)
