from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


# Cho phép phương thức POST
@app.route('/', methods=['GET', 'POST'])
def upload():
    video = request.files['video']
    filename = 'videos/' + video.filename
    video.save('static/videos/' + video.filename)
    return render_template("index.html", video_name=filename)


if __name__ == '__main__':
    app.run(debug=True)
