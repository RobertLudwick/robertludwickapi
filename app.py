import os
import flask
from flask import request, send_from_directory, Flask



UPLOAD_DIRECTORY = "/api_files"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


app = Flask(__name__, static_folder='api_files')


@app.route("/uploads/<filename>")
def download_file(filename):
    print(filename)
    print(app.static_folder)
    return send_from_directory(app.static_folder,filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, port=8000)