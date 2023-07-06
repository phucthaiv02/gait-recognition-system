from flask import Flask, render_template, request, send_file

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def upload():
    video = request.files['video']
    filename = 'videos/' + video.filename
    video.save('static/videos/' + video.filename)
    return render_template("index.html", video_name=filename)


@app.route('/download')
def download_file():
    file_path = 'static\\videos\\probe4 (1).mp4'
    file_name = ''

    return send_file(file_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
