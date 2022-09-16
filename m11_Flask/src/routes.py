from flask import render_template, request, flash, redirect, url_for, session, make_response
from werkzeug.utils import secure_filename
import pathlib
import uuid
from datetime import datetime, timedelta

from . import app
from src.libs.validation_file import allowed_file
from src.repository import users, pics
# from src import repository -> repository.users

@app.before_request
def before_func():
    auth = True if 'username' in session else False
    if not auth:
        token_user = request.cookies.get('username')
        if token_user:
            user = users.get_user_by_token(token_user)
            if user:
                session['username'] = {"username": user.username, "id": user.id}

@app.route('/healthcheck')
def healthcheck():
    return 'I am working'


@app.route('/', strict_slashes=False)
def index():
    auth = True if 'username' in session else False
    return render_template('pages/index.html', title='Cloud Pictures!', auth=auth)


@app.route('/pictures', strict_slashes=False)
def pictures():
    auth = True if 'username' in session else False
    if not auth:
        return redirect(request.url)
    pictures_user = pics.get_pictures_user(session['username']['id'])
    return render_template('pages/pictures.html', auth=auth, pictures=pictures_user)


@app.route('/registration', methods=['GET', 'POST'], strict_slashes=False)
def registration():
    auth = True if 'username' in session else False
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        nick = request.form.get('nick')
        user = users.create_user(email, password, nick)
        print(user)
        return redirect(url_for('login'))
    if auth:
        return redirect(url_for('index'))
    else:
        return render_template('pages/registration.html')


@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    auth = True if 'username' in session else False
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') == 'on' else False

        user = users.login(email, password)
        if user is None:
            return redirect(url_for('login'))
        session['username'] = {"username": user.username, "id": user.id}
        response = make_response(redirect(url_for('index')))
        if remember:
            # Треба створить token, та покласти його в cookie та БД
            token = str(uuid.uuid4())
            expire_data = datetime.now() + timedelta(days=60)
            response.set_cookie('username', token, expires=expire_data)
            users.set_token(user, token)

        return response
    if auth:
        return redirect(url_for('index'))
    else:
        return render_template('pages/login.html')


@app.route('/logout', strict_slashes=False)
def logout():
    auth = True if 'username' in session else False
    if not auth:
        return redirect(request.url)  # Відправляє туди звідки він прийшов
    session.pop('username')
    response = make_response(redirect(url_for('index')))
    response.set_cookie('username', '', expires=-1)

    return response


@app.route('/pictures/upload', methods=['GET', 'POST'], strict_slashes=False)
def pictures_upload():
    auth = True if 'username' in session else False
    if not auth:
        return redirect(request.url)
    if request.method == 'POST':
        description = request.form.get('description')
        print(description)
        if 'photo' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['photo']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(pathlib.Path(app.config['UPLOAD_FOLDER']) / filename)
            return redirect(url_for('pictures_upload'))
    return render_template('pages/upload.html', auth=auth)


@app.route('/pictures/edit/<id>', methods=['GET', 'POST'], strict_slashes=False)
def edit():
    auth = True if 'username' in session else False
    if not auth:
        return redirect(request.url)
    return render_template('pages/edit.html', auth=auth)


@app.route('/pictures/delete/<id>', methods=['POST'], strict_slashes=False)
def delete():
    auth = True if 'username' in session else False
    if not auth:
        return redirect(request.url)
    return render_template('pages/edit.html', auth=auth)