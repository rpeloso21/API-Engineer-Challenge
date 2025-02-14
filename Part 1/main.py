import os
from flask import Flask, request, jsonify, render_template, send_file
from werkzeug.utils import secure_filename


app = Flask(__name__)

def flatten_data(input_file):
    data = []
    keys = []

    output_file = os.path.join("processed", f"{os.path.splitext(os.path.basename(input_file))[0]}_processed.txt")
    
    try:
        os.makedirs("processed", exist_ok=True)

        with open(input_file, "r") as file:
            for line in file:
                entries = line.strip().split("^^")
                row_dict = {}

                for entry in entries:
                    if "=" in entry:
                        key, value = entry.split("=", 1) 
                        clean_value = value.replace("^", "").replace("=", "")
                        row_dict[key] = clean_value.strip()
                        
                        if key not in keys:
                            keys.append(key)

                data.append(row_dict)

        with open(output_file, "w") as out:
            out.write("|".join(keys) + "\n")
            for row in data:
                out.write("|".join(row.get(key, "") for key in keys) + "\n")

        print(f"Processed data saved to: {output_file}")

        return output_file
    
    except FileNotFoundError:
        print(f"Error: File not found -> {input_file}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    try:
        filename = secure_filename(file.filename)
        uploaded_file_path = os.path.join('uploads', filename)
        os.makedirs('uploads', exist_ok=True)
        file.save(uploaded_file_path)

        processed_file = flatten_data(uploaded_file_path)

        if not processed_file:
            return jsonify({"error": "File processing failed"}), 500

        return send_file(os.path.abspath(processed_file), as_attachment=True)
    
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
