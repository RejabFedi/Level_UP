from flask import Flask, render_template, request
from werkzeug import secure_filename


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return "File saved successfully"


app.run(host='localhost', port=5000)