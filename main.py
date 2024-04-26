from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/iri', methods=['POST', 'GET'])
def index():
    con = sqlite3.connect("static\Base_with_manga_and_novel\data.sqlite")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM Manga_DB""").fetchall()
    sorted_list = sorted(result, key=lambda x: x[-1])
    The_proposed_title_1 = {}
    The_proposed_title_1['link_1'] = sorted_list[0][6]
    The_proposed_title_1['Name_1'] = sorted_list[0][2]
    The_proposed_title_1['Authors_name_1'] = sorted_list[0][1]
    The_proposed_title_1['Description_of_the_title_1'] = sorted_list[0][4]
    The_proposed_title_1['estimation_1'] = sorted_list[0][3]
    The_proposed_title_1['Img_1'] = f'static\Base_with_manga_and_novel\{sorted_list[0][6]}\img_cover.png'
    The_proposed_title_2 = {}
    The_proposed_title_2['link_2'] = sorted_list[1][6]
    The_proposed_title_2['Name_2'] = sorted_list[1][2]
    The_proposed_title_2['Authors_name_2'] = sorted_list[1][1]
    The_proposed_title_2['Description_of_the_title_2'] = sorted_list[1][4]
    The_proposed_title_2['estimation_2'] = sorted_list[1][3]
    The_proposed_title_2['Img_2'] = f'static\Base_with_manga_and_novel\{sorted_list[1][6]}\img_cover.png'
    con.close()
    # Надо будет доделать текст для карусели
    # carousel_1 = {}
    # carousel_1['description_carousel_1'] = open('static\carousel_suggestion\first\description.txt', 'r').read()
    # carousel_1['heading_carousel_1'] = open('static\carousel_suggestion\first\heading.txt', 'r').read()
    # carousel_1['img_carousel_1'] = 'static\carousel_suggestion\first\img.png'
    # carousel_2 = {}
    # carousel_2['description_carousel_2'] = open('static\carousel_suggestion\two\description.txt', 'r').read()
    # carousel_2['heading_carousel_2'] = open('static\carousel_suggestion\two\heading.txt', 'r').read()
    # carousel_2['img_carousel_2'] = 'static\carousel_suggestion\two\img.png'
    # carousel_3 = {}
    # carousel_3['description_carousel_3'] = open('static\carousel_suggestion\tri\description.txt', 'r').read()
    # carousel_3['heading_carousel_3'] = open('static\carousel_suggestion\tri\heading.txt', 'r').read()
    # carousel_3['img_carousel_3'] = 'static\carousel_suggestion\tri\img.png'
    return render_template('index.html', **The_proposed_title_1, **The_proposed_title_2)


@app.route(f'/<manga_name>')
def bebra(manga_name):
    try:
        sqlite_connection = sqlite3.connect('static\Base_with_manga_and_novel\data.sqlite')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        result = cursor.execute(f"""SELECT * FROM Manga_DB WHERE Link = '{manga_name}'""").fetchall()
        c = 0
        for i in result:
            if i[5] == manga_name:
                break
            c += 1
        sql_update_query = f"""UPDATE Manga_DB SET Estimation = {int(result[c][3]) + 1} WHERE Link = '{manga_name}'"""
        cursor.execute(sql_update_query)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
    lists = ['002_1nZi.jpeg', '003_RrQF.jpeg']
    return render_template('Reading.html', listik=lists)


@app.route('/add_composition')
def ADD():
    if request.method == 'GET':
        return render_template('ADD.html')
    elif request.method == 'POST':
        print(request.form['Name_composition'])
        print(request.form['Name'])
        print(request.form['Author'])
        print(request.form['class'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form['zip'])
        return "Форма отправлена"


@app.route('/registr')
def Registr():
    pass


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
