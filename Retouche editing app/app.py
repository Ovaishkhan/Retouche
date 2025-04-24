from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/upload-page')
def upload_page():
    return render_template("upload.html")


# UPLOADS PHOTO FROM PC
@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return "No image uploaded", 400

    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    return redirect(url_for('editroom', image_file=filename))


@app.route('/editroom')
def editroom():
    image_file = request.args.get('image_file')
    return render_template('editroom.html', image_file=image_file)


if __name__ == '__main__':
    app.run(debug=True)
