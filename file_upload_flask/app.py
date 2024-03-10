from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        uploaded_file.save('file_upload_flask/uploaded_files/'+uploaded_file.filename)
        return 'Файл сохранён!'
    return render_template('upload.html')

app.run(debug=True)