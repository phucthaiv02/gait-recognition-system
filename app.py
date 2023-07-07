from flask import Flask, render_template, request, send_file
import json

app = Flask(__name__)

CURRENT_VIDEO = ""


@app.route('/')
def home():
    return render_template('index.html', image_name='images/bg.png')


@app.route('/', methods=['POST'])
def update_class():
    class_name = request.form['class_name']
    return class_name


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    def process():
        if 'video' in request.files:
            video = request.files['video']
            video_name = 'videos/' + video.filename

            ##
            # Chạy hàm xử lý video tại đây
            ##

            video.save('static/videos/' + video.filename)
            data_files = ['static/json/data1.json', 'static/json/data2.json',
                          'static/json/data3.json']
            return video_name, data_files
        else:
            return "", []

    video_name, data_files = process()
    objects = []
    for file in data_files:
        with open(file) as f:
            data = json.load(f)
        objects.append(data)
    if video_name != "":
        if objects != []:
            return render_template('index.html', video_name=video_name, objects=objects)
        return render_template('index.html', video_name=video_name)
    else:
        return render_template("index.html", image_name='images/bg.png')


@app.route('/upload', methods=['POST', 'GET'])
def add_data():
    if 'video' in request.files and 'name' in request.form:
        video = request.files['video']
        video_name = 'videos/' + video.filename
        push = True
        return render_template('upload.html', push=push, video_name=video_name)
    else:
        return render_template('upload.html', image_name="images/bg.png")


@app.route('/download')
def download_file():
    file_path = 'static\\videos\\probe4 (1).mp4'
    file_name = ''

    return send_file(file_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
