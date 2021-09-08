from datetime import datetime
from flask import Flask, send_file, request
from model import detect_face_mask

app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def predict():
    file = request.files['image']
    current_time = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    filename = current_time + '-' + file.filename
    detect_face_mask(filename, file)
    return send_file(filename, mimetype='image/{}'.format(filename.split('.')[-1]))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")