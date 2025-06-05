from flask import Flask, render_template, request, send_file, jsonify
from PIL import Image, ImageEnhance
import numpy as np
import os
import uuid
from text_dither_art import detailed_text_dither, apply_crt_effect

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "image" not in request.files:
            return "No image uploaded", 400
        
        img = request.files["image"]
        if img.filename == "":
            return "No image selected", 400

        # Save uploaded image
        filename = str(uuid.uuid4()) + ".png"
        path = os.path.join(UPLOAD_FOLDER, filename)
        img.save(path)

        # Get processing parameters from form
        output_width = int(request.form.get("width", 300))
        invert = request.form.get("invert", "false").lower() == "true"
        contrast = float(request.form.get("contrast", 1.8))
        sharpness = float(request.form.get("sharpness", 1.5))
        apply_crt = request.form.get("crt", "false").lower() == "true"
        crt_intensity = float(request.form.get("crt_intensity", 1.0))

        # Generate text art
        text_art = detailed_text_dither(
            path,
            output_width=output_width,
            invert=invert,
            contrast=contrast,
            sharpness=sharpness
        )

        if apply_crt:
            text_art = apply_crt_effect(text_art, crt_intensity)

        # Save the result
        output_path = os.path.join(OUTPUT_FOLDER, filename.replace(".png", ".txt"))
        with open(output_path, "w", encoding='utf-8') as f:
            f.write(text_art)

        # Return both the file and the text content
        return jsonify({
            'download_url': f'/download/{filename.replace(".png", ".txt")}',
            'text_art': text_art
        })

    return render_template("index.html")

@app.route("/download/<filename>")
def download_file(filename):
    return send_file(
        os.path.join(OUTPUT_FOLDER, filename),
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)
