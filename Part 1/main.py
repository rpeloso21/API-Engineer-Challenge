import os
from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename


app = Flask(__name__)

def flatten_data(file):
    data = []
    keys = set()

    output_file = f"{os.path.splitext(file)[0]}_processed.txt"

    with open(file, "r") as file:
        for line in file:
            entries = line.strip().split("^^")
            row_dict = {}

            for entry in entries:
                if "=" in entry:
                    key, value = entry.split("=", 1) 
                    clean_value = value.replace("^", "").replace("=", "")
                    row_dict[key] = clean_value.strip()
                    keys.add(key)

            data.append(row_dict)

    with open(output_file, "w") as out:
        out.write("|".join(keys) + "\n")
        for row in data:
            out.write("|".join(row.get(key, "") for key in keys) + "\n")

    print(f"Processed data saved to: {output_file}")

    return output_file

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    filename = secure_filename(file.filename)
    uploaded_file_path = os.path.join('uploads', filename)
    os.makedirs('uploads', exist_ok=True)
    file.save(uploaded_file_path)

    processed_file = flatten_data(uploaded_file_path)

    return send_file(processed_file, as_attachment=True) 


if __name__ == "__main__":
    app.run(debug=True)
