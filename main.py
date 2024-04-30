import sqlite3
import os
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, redirect, session, request, url_for
from models.user import User, find_user
from shared.db import db
import zipfile
import difflib

app = Flask(__name__)
app.config["SECRET_KEY"] = "abS8gfjAh"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)

with app.app_context():
    db.create_all()

Ocenka = []

user = ''


# РЕГИСТРАЦИЯ____________________________________________________________________________________________________________
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if username and email and password:
            if find_user(email):
                return render_template("register.html", error="Электронная почта занята.")

            new_user = User(username, email, password)

            db.session.add(new_user)
            db.session.commit()
            return redirect("/login")

    return render_template("register.html")


# РЕГИСТРАЦИЯ____________________________________________________________________________________________________________

# ВХОД___________________________________________________________________________________________________________________
@app.route("/login", methods=["GET", "POST"])
def login():
    global user
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = find_user(email)
        if password == '' or email == '':
            return render_template("login.html", error="Неверная почта или пароль.")
        elif user and user.check_password(password):
            session["email"] = user.email
            return redirect('/iri')
        else:
            print(1)
            return render_template("login.html", error="Неверная почта или пароль.")
    print(2)
    return render_template("login.html")


# ВХОД___________________________________________________________________________________________________________________

# ГЛАВНОЕ МЕНЮ___________________________________________________________________________________________________________
@app.route('/iri', methods=['POST', 'GET'])
def index():
    global user
    if request.method == 'GET':
        if user != '':
            user_l = False
        else:
            user_l = True
        con = sqlite3.connect("static\Base_with_manga_and_novel\data.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM Manga_DB""").fetchall()
        sorted_list = sorted(result, key=lambda x: x[3], reverse=True)
        print(sorted_list)
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
        The_proposed_title_3 = {}
        The_proposed_title_3['link_3'] = sorted_list[2][6]
        The_proposed_title_3['Name_3'] = sorted_list[2][2]
        The_proposed_title_3['Authors_name_3'] = sorted_list[2][1]
        The_proposed_title_3['Description_of_the_title_3'] = sorted_list[2][4]
        The_proposed_title_3['estimation_3'] = sorted_list[2][3]
        The_proposed_title_3['Img_3'] = f'static\Base_with_manga_and_novel\{sorted_list[2][6]}\img_cover.png'
        The_proposed_title_4 = {}
        The_proposed_title_4['link_4'] = sorted_list[3][6]
        The_proposed_title_4['Name_4'] = sorted_list[3][2]
        The_proposed_title_4['Authors_name_4'] = sorted_list[3][1]
        The_proposed_title_4['Description_of_the_title_4'] = sorted_list[3][4]
        The_proposed_title_4['estimation_4'] = sorted_list[3][3]
        The_proposed_title_4['Img_4'] = f'static\Base_with_manga_and_novel\{sorted_list[3][6]}\img_cover.png'
        The_proposed_title_5 = {}
        The_proposed_title_5['link_5'] = sorted_list[4][6]
        The_proposed_title_5['Name_5'] = sorted_list[4][2]
        The_proposed_title_5['Authors_name_5'] = sorted_list[4][1]
        The_proposed_title_5['Description_of_the_title_5'] = sorted_list[4][4]
        The_proposed_title_5['estimation_5'] = sorted_list[4][3]
        The_proposed_title_5['Img_5'] = f'static\Base_with_manga_and_novel\{sorted_list[4][6]}\img_cover.png'
        The_proposed_title_6 = {}
        The_proposed_title_6['link_6'] = sorted_list[5][6]
        The_proposed_title_6['Name_6'] = sorted_list[5][2]
        The_proposed_title_6['Authors_name_6'] = sorted_list[5][1]
        The_proposed_title_6['Description_of_the_title_6'] = sorted_list[5][4]
        The_proposed_title_6['estimation_6'] = sorted_list[5][3]
        The_proposed_title_6['Img_6'] = f'static\Base_with_manga_and_novel\{sorted_list[5][6]}\img_cover.png'
        con.close()
        carousel_1 = {}
        carousel_1['description_carousel_1'] = open('static\carousel_suggestion\qirst\description.txt', 'r',
                                                    encoding='UTF-8').read()
        carousel_1['heading_carousel_1'] = open('static\carousel_suggestion\qirst\heading.txt', 'r',
                                                encoding='UTF-8').read()
        carousel_1['img_carousel_1'] = 'static\carousel_suggestion\qirst\img.png'
        carousel_2 = {}
        carousel_2['description_carousel_2'] = open('static\carousel_suggestion\qwo\description.txt', 'r',
                                                    encoding='UTF-8').read()
        carousel_2['heading_carousel_2'] = open('static\carousel_suggestion\qwo\heading.txt', 'r',
                                                encoding='UTF-8').read()
        carousel_2['img_carousel_2'] = 'static\carousel_suggestion\qwo\img.png'
        carousel_3 = {}
        carousel_3['description_carousel_3'] = open('static\carousel_suggestion\qri\description.txt', 'r',
                                                    encoding='UTF-8').read()
        carousel_3['heading_carousel_3'] = open('static\carousel_suggestion\qri\heading.txt', 'r',
                                                encoding='UTF-8').read()
        carousel_3['img_carousel_3'] = 'static\carousel_suggestion\qri\img.png'
        return render_template('index.html', **The_proposed_title_1, **The_proposed_title_2, **The_proposed_title_3,
                               **The_proposed_title_4, **The_proposed_title_5, **The_proposed_title_6, **carousel_1, **carousel_2, **carousel_3,
                               us=user_l, user=user)
    if request.method == 'POST':
        Search = request.form['Search']
        print(Search)
        Searching = []
        try:
            sqlite_connection = sqlite3.connect('static\Base_with_manga_and_novel\data.sqlite')
            cursor = sqlite_connection.cursor()
            print("Подключен к SQLite")
            result_name = cursor.execute("""SELECT Title_name FROM Manga_DB """).fetchall()
            result_link = cursor.execute("""SELECT Link FROM Manga_DB """).fetchall()
            print("Запись успешно обновлена")
            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")
        for x in result_name:
            diff = difflib.SequenceMatcher(None, (x[0]).lower(), Search.lower())
            similarity = diff.ratio()
            similarity_percentage = similarity * 100
            if similarity_percentage > 45:
                Searching.append([x[0], similarity_percentage, 'name'])
        for x in result_link:
            diff = difflib.SequenceMatcher(None, (x[0]).lower(), Search.lower())
            similarity = diff.ratio()
            similarity_percentage = similarity * 100
            if similarity_percentage > 45:
                Searching.append([x[0], similarity_percentage, 'link'])
        if Searching == []:
            return redirect('iri')
        Searching = sorted(Searching, key=lambda x: x[1], reverse=True)
        if Searching[0][2] == 'name':
            try:
                sqlite_connection = sqlite3.connect('static\Base_with_manga_and_novel\data.sqlite')
                cursor = sqlite_connection.cursor()
                print("Подключен к SQLite")
                Searching_link = cursor.execute(
                    f"""SELECT Link FROM Manga_DB WHERE Title_name = '{Searching[0][0]}'""").fetchall()
                print("Запись успешно обновлена")
                cursor.close()

            except sqlite3.Error as error:
                print("Ошибка при работе с SQLite", error)
            finally:
                if sqlite_connection:
                    sqlite_connection.close()
                    print("Соединение с SQLite закрыто")
            return redirect(f'{Searching_link[0][0]}/read')
        else:
            return redirect(f'{Searching[0][0]}/read')


# ГЛАВНОЕ МЕНЮ___________________________________________________________________________________________________________
# ДОБАВЛЕНИЕ ТАЙТЛА______________________________________________________________________________________________________
@app.route('/add_composition', methods=['POST', 'GET'])
def ADD():
    if request.method == 'GET':
        return render_template('ADD.html')
    elif request.method == 'POST':
        Name_composition = request.form['Name_composition']
        Name = request.form['Name']
        Translator = request.form['Author']
        Link = request.form['Link']
        for x in Link:
            if x.lower() not in 'qwertyuiopasdfghjklzxcvbnm_'.lower():
                return redirect('ERROR')
        about = request.form['about']
        os.makedirs('static\Base_with_manga_and_novel/{}'.format(Link), exist_ok=True)
        app.config['UPLOAD_FOLDER'] = f'static\Base_with_manga_and_novel\{Link}'
        png_file = request.files['png_file']
        if 'png_file' not in request.files:
            return redirect('ERROR')
        zip_file = request.files['zip_file']
        if 'zip_file' not in request.files:
            return redirect('ERROR')
        # Получить безопасные имена файлов
        png_filename = secure_filename(png_file.filename)
        zip_filename = secure_filename(zip_file.filename)
        # Сохранить файлы в директорию
        png_file.save(os.path.join(app.config['UPLOAD_FOLDER'], png_filename))
        directory = f"static\Base_with_manga_and_novel\{Link}"
        Len_Chapters = ''
        for root, dirs, files in os.walk(directory):
            Len_Chapters = files
        os.rename(f"static\Base_with_manga_and_novel\{Link}\{Len_Chapters[0]}",
                  f"static\Base_with_manga_and_novel\{Link}\img_cover.png")
        zip_file.save(os.path.join(app.config['UPLOAD_FOLDER'], zip_filename))
        Len_Chapters = ''
        for root, dirs, files in os.walk(directory):
            Len_Chapters = files
        Len_Chapters = [i for i in Len_Chapters if i[-4:] == '.zip']

        os.rename(f"static\Base_with_manga_and_novel\{Link}\{Len_Chapters[0]}",
                  f"static\Base_with_manga_and_novel\{Link}\Chapters.zip")

        with zipfile.ZipFile(f"static\Base_with_manga_and_novel\{Link}\Chapters.zip", "r") as zip_ref:
            zip_ref.extractall(f'static\Base_with_manga_and_novel\{Link}')
        zip_ref.close()
        os.rename(f"static\Base_with_manga_and_novel\{Link}\{Len_Chapters[0][:-4]}",
                  f"static\Base_with_manga_and_novel\{Link}\Chapters")
        zip_file = f"static\Base_with_manga_and_novel\{Link}\Chapters.zip"
        os.remove(zip_file)
        directory = f"static\Base_with_manga_and_novel\{Link}\Chapters"
        Len_Chapters = 0
        for root, dirs, files in os.walk(directory):
            Len_Chapters += len(dirs)
        for i in range(Len_Chapters):
            for root, dirs, files in os.walk(f"static\Base_with_manga_and_novel\{Link}\Chapters\{i + 1}"):
                c = 0
                for x in files:
                    c += 1
                    print(f"static\Base_with_manga_and_novel\{Link}\Chapters\{i + 1}\{x}")
                    os.rename(f"static\Base_with_manga_and_novel\{Link}\Chapters\{i + 1}\{x}",
                              f"static\Base_with_manga_and_novel\{Link}\Chapters\{i + 1}\{c}.jpeg")
        try:
            sqlite_connection = sqlite3.connect('static\Base_with_manga_and_novel\data.sqlite')
            cursor = sqlite_connection.cursor()
            print("Подключен к SQLite")
            result = cursor.execute("""SELECT ID FROM Manga_DB""").fetchall()
            result_id_max = int(max([int(i[0]) for i in result]))
            print(result_id_max)
            print("Запись успешно обновлена")
            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")
        try:
            sqlite_connection = sqlite3.connect('static\Base_with_manga_and_novel\data.sqlite')
            cursor = sqlite_connection.cursor()
            print("Подключен к SQLite")
            sqlite_insert_query = f"""INSERT INTO Manga_DB
                                  (ID, Authors_name , Title_name, Estimation, Description_of_the_title, MANGA, Link, Translator, Estimates_of_the_number, Evaluations)
                                  VALUES
                                  (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

            data_tuple = (result_id_max + 1, Name, Name_composition, 0, about, Link, Link, Translator, 0, '0')
            cursor.execute(sqlite_insert_query, data_tuple)
            sqlite_connection.commit()
            print("Переменные Python успешно вставлены в таблицу sqlitedb_developers")

            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")
        return redirect('iri')


# ДОБАВЛЕНИЕ ТАЙТЛА______________________________________________________________________________________________________


# ОПИСАНИЕ ТАЙТЛА________________________________________________________________________________________________________
@app.route(f'/<manga_name>/read', methods=['POST', 'GET'])
def Read_title(manga_name):
    global user
    if request.method == 'GET':
        if user != '':
            user_l = False
            global Ocenka
            if manga_name not in Ocenka:
                Oce = True
            else:
                Oce = False
        else:
            user_l = True
            Oce = False

    if request.method == 'GET':
        sqlite_connection = sqlite3.connect('static\Base_with_manga_and_novel\data.sqlite')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        result = cursor.execute(f"""SELECT * FROM Manga_DB WHERE Link = '{manga_name}'""").fetchall()
        The_proposed_title = {}
        The_proposed_title['link'] = result[0][6]
        The_proposed_title['Name'] = result[0][2]
        The_proposed_title['Authors_name'] = result[0][1]
        The_proposed_title['Translator'] = result[0][7]
        The_proposed_title['Description_of_the_title'] = result[0][4]
        The_proposed_title['Img'] = f'\static\Base_with_manga_and_novel\{result[0][6]}\img_cover.png'
        The_proposed_title['kolvo'] = result[0][8]
        if The_proposed_title['kolvo'] != 0:
            The_proposed_title['Ocenka'] = round(
                sum([int(i) for i in (result[0][9]).split(', ') if i != '']) / result[0][8], 1)
        else:
            The_proposed_title['Ocenka'] = 'Пока нету оценок'
        cursor.close()
        directory = f"static\Base_with_manga_and_novel\{manga_name}\Chapters"
        Len_Chapters = 0
        for root, dirs, files in os.walk(directory):
            Len_Chapters += len(dirs)
        Len_Chapters = [str(i + 1) for i in range(Len_Chapters)]
        return render_template('Title.html', len=Len_Chapters, **The_proposed_title, oc=Oce, us=user_l)
    elif request.method == 'POST':
        print(request.form['class'])
        if request.form['class'] in '12345':
            Ocenka.append(manga_name)
        try:
            sqlite_connection = sqlite3.connect('static\Base_with_manga_and_novel\data.sqlite')
            cursor = sqlite_connection.cursor()
            print("Подключен к SQLite")
            result = cursor.execute(f"""SELECT * FROM Manga_DB WHERE Link = '{manga_name}'""").fetchall()
            sql_update_query = f"""UPDATE Manga_DB SET Estimates_of_the_number = {int(result[0][8]) + 1} WHERE Link = '{manga_name}'"""
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
        try:

            sqlite_connection = sqlite3.connect('static\Base_with_manga_and_novel\data.sqlite')
            cursor = sqlite_connection.cursor()
            print("Подключен к SQLite")
            result = cursor.execute(f"""SELECT * FROM Manga_DB WHERE Link = '{manga_name}'""").fetchall()
            sql_update_query = f"""UPDATE Manga_DB SET Evaluations = '{result[0][9]}, {request.form['class']}' WHERE Link = '{manga_name}'"""
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
        return redirect(f'/{manga_name}/read')


# ОПИСАНИЕ ТАЙТЛА________________________________________________________________________________________________________

# ЧТЕНИЕ ТАЙТЛА__________________________________________________________________________________________________________
@app.route(f'/<manga_name>/read/<chapters>', methods=['POST', 'GET'])
def bebra(manga_name, chapters):
    global user
    if request.method == 'GET':
        if user != '':
            user_l = False
        else:
            user_l = True
    if request.method == 'GET':
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
            sql_update_query = f"""UPDATE Manga_DB SET Estimation = {int(result[0][3]) + 1} WHERE Link = '{manga_name}'"""
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
        manga = 0
        directory = f"static\Base_with_manga_and_novel\{manga_name}\Chapters"
        Len_Chapters = 0
        for root, dirs, files in os.walk(directory):
            Len_Chapters += len(dirs)
        directory_ch = f"static\Base_with_manga_and_novel\{manga_name}\Chapters\{chapters}"
        for root, dirs, files in os.walk(directory_ch):
            manga += len(files)
        page = [str(i + 1) for i in range(manga)]
        Len_Chapters = [str(i + 1) for i in range(Len_Chapters)]
        return render_template('Reading.html', listik=page, len_manga=Len_Chapters, chapter=str(chapters),
                               name=manga_name, us=user_l)
    elif request.method == 'POST':
        Search = request.form['Search']
        if Search is not '':
            Searching = []
            try:
                sqlite_connection = sqlite3.connect('static\Base_with_manga_and_novel\data.sqlite')
                cursor = sqlite_connection.cursor()
                print("Подключен к SQLite")
                result_name = cursor.execute("""SELECT Title_name FROM Manga_DB """).fetchall()
                result_link = cursor.execute("""SELECT Link FROM Manga_DB """).fetchall()
                print("Запись успешно обновлена")
                cursor.close()

            except sqlite3.Error as error:
                print("Ошибка при работе с SQLite", error)
            finally:
                if sqlite_connection:
                    sqlite_connection.close()
                    print("Соединение с SQLite закрыто")
            for x in result_name:
                diff = difflib.SequenceMatcher(None, (x[0]).lower(), Search.lower())
                similarity = diff.ratio()
                similarity_percentage = similarity * 100
                if similarity_percentage > 45:
                    Searching.append([x[0], similarity_percentage, 'name'])
            for x in result_link:
                diff = difflib.SequenceMatcher(None, (x[0]).lower(), Search.lower())
                similarity = diff.ratio()
                similarity_percentage = similarity * 100
                if similarity_percentage > 45:
                    Searching.append([x[0], similarity_percentage, 'link'])
            if Searching == []:
                return redirect(f'/{manga_name}/read/{chapters}')

                Searching = sorted(Searching, key=lambda x: x[1], reverse=True)
            if Searching[0][2] == 'name':
                try:
                    sqlite_connection = sqlite3.connect('static\Base_with_manga_and_novel\data.sqlite')
                    cursor = sqlite_connection.cursor()
                    print("Подключен к SQLite")
                    Searching_link = cursor.execute(
                        f"""SELECT Link FROM Manga_DB WHERE Title_name = '{Searching[0][0]}'""").fetchall()
                    print("Запись успешно обновлена")
                    cursor.close()

                except sqlite3.Error as error:
                    print("Ошибка при работе с SQLite", error)
                finally:
                    if sqlite_connection:
                        sqlite_connection.close()
                        print("Соединение с SQLite закрыто")
                return redirect(f'/{Searching_link[0][0]}/read')
            elif Searching[0][2] == 'link':
                return redirect(f'/{Searching[0][0]}/read')


# ЧТЕНИЕ ТАЙТЛА__________________________________________________________________________________________________________
# ОШИБКА________________________________________________________________________________________________________________
@app.route('/ERROR')
def rorre():
    return render_template('ERROR.html')


print(user)


# ОШИБКА________________________________________________________________________________________________________________
# ВЫХОД_________________________________________________________________________________________________________________
@app.route('/exit')
def EXIT():
    global user
    user = ''
    return redirect('/iri')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
