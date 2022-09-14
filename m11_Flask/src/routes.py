from flask import render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import pathlib
from . import app
from src.libs.validation_file import allowed_file
from src.repository import users


@app.route('/healthcheck')
def healthcheck():
    return 'I am working'


@app.route('/', strict_slashes=False)
def index():
    return render_template('pages/index.html', title='Cloud Pictures!')


@app.route('/pictures', strict_slashes=False)
def pictures():
    return render_template('pages/pictures.html')


@app.route('/registration', methods=['GET', 'POST'], strict_slashes=False)
def registration():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        nick = request.form.get('nick')
        user = users.create_user(email, password, nick)
        print(user)
        return redirect(url_for('login'))
    return render_template('pages/registration.html')


@app.route('/login', strict_slashes=False)
def login():
    return render_template('pages/login.html')


@app.route('/pictures/upload', methods=['GET', 'POST'], strict_slashes=False)
def pictures_upload():
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
    return render_template('pages/upload.html')


@app.route('/edit', strict_slashes=False)
def edit():
    return render_template('pages/edit.html')

