
from python1 import app
import os
from flask import render_template,request,redirect, url_for
from werkzeug.utils import secure_filename
import time

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'HI'


@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home.html')


@app.route("/upload",methods=["GET","POST"])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return('no files')
        

        uploaded_files = request.files.getlist("file")
        names= []

        print(type(uploaded_files[0]))
        for file in uploaded_files:
            file.save(f"C:/Users/SHASHANK/Documents/flask/appln/python1/templates/uploads/{secure_filename(file.filename)}")
            names.append(file.filename)

        
        return redirect(url_for('process'))


@app.route("/process")
def process():
    path = os.getcwd()
    path = path +'\\python1\\templates\\uploads'
    names = os.listdir(path)
    flag =1

    for file in os.listdir(path):
        if file.endswith(".txt"):
            #logic
            time.sleep(5)
        
        print('done')


    flag =0

    return render_template('process.html',items=names,flag =flag)

