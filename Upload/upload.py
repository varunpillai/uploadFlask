from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, ALL

app = Flask(__name__)

files = UploadSet('files', ALL)

app.config['UPLOADED_FILES_DEST'] = 'uploads'
configure_uploads(app, files)

@app.route('/')
@app.route('/index')
def index():
    return render_template('upload.html')
    
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'projlist' in request.files:
        filename = files.save(request.files['projlist'])

    return render_template('upload.html')

if __name__ == '__main__':
	app.run(debug=True, port=5555)