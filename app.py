from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_path = os.path.join(OUTPUT_FOLDER, "no_bg_" + file.filename)

        file.save(input_path)

        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)

        return send_file(output_path, as_attachment=True)

    return '''
    <h2>Background Removal App</h2>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="image" required>
        <input type="submit" value="Upload & Remove Background">
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
