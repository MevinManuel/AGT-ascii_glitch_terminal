# 🧬 Glitch ASCII Art Generator

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-Web_App-lightgrey)
![OpenCV](https://img.shields.io/badge/OpenCV-Live_Cam-green)
![ASCII](https://img.shields.io/badge/ASCII-Glitch_Mode-purple)
![License](https://img.shields.io/badge/License-MIT-blue)

> A retro_matrix-inspired web app to generate stylized ASCII art from static images or live webcam feed — with glitch aesthetics, CRT effects, and customizable filters.

---

## 🌈 Demo Preview

<div align="center">
  <img src="assets/demo-upload.png" width="700" alt="Image to ASCII Upload Demo"/>
  <br><br>
  <img src="assets/demo-livecam.gif" width="700" alt="Live Webcam ASCII Art"/>
</div>

---

## ✨ Features

- 🎨 **Image-to-ASCII Converter**
  - Upload any image
  - Adjust contrast, sharpness, and ASCII width
  - Enable/disable CRT distortion effect
  - Output downloadable `.txt` art file

- 📸 **Live Cam ASCII Mode**
  - Real-time ASCII transformation of your webcam feed using OpenCV
  - Retro terminal-style monochrome preview

- 🌗 **Custom Options**
  - ASCII width control
  - Inversion toggle (light/dark)
  - CRT intensity slider for glitch enthusiasts

---

## 🛠 Tech Stack <br>

| Frontend         | Backend           | Others            | <br>
|------------------|-------------------|-------------------| <br>
| HTML, CSS (Retro) | Flask (Python)    | OpenCV, Pillow    | <br>
| Vanilla JS       | PIL for image ops | ASCII Mapping / Filters | <br>

---

## 📂 Folder Structure <br>

glitch-ascii/
├── app.py
├── text_dither_art.py
├── templates/
│ └── index.html
├── static/
│ └── style.css
├── uploads/
├── output/
└── assets/


---

## 🚀 How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/glitch-ascii-art.git
cd glitch-ascii-art
```

2. Install requirements

pip install -r requirements.txt
<br>

3. Run the Flask web app

python app.py
Open your browser and go to http://localhost:5000
<br>



⚙️ Customization Parameters <br>
| Parameter       | Type   | Description                           |
| --------------- | ------ | ------------------------------------- |
| `width`         | Number | Output character width (default: 300) |
| `invert`        | Bool   | Invert brightness to flip ASCII scale |
| `contrast`      | Float  | Contrast enhancement (default: 1.8)   |
| `sharpness`     | Float  | Sharpness level (default: 1.5)        |
| `crt`           | Bool   | Enable CRT glitch line distortion     |
| `crt_intensity` | Float  | Strength of CRT effect (default: 1.0) |


🧠 How It Works
For images:

Convert to grayscale

Resize based on terminal width

Enhance contrast & sharpness

Map brightness levels to ASCII characters

(Optional) Apply CRT glitch effect

For webcam:

Use OpenCV to grab frames

Transform to ASCII in real-time

Display in live terminal stream

💡 Ideas to Extend
🧬 AI/ML-based ASCII generator using Vision Transformers

🌐 Deploy on Vercel + FastAPI or Render

📜 License
MIT License. Feel free to fork and remix this project!

👨‍💻 Author
Made with glitchy love by Your Mevin Manuel
