Here’s a sleek, memorable project name and the complete codebase bundled for you:

**Project Name:** **VigilantVision**

You can download the entire codebase (with all files separate) here:

[Download VigilantVision.zip](sandbox:/mnt/data/VigilantVision.zip)

**What’s inside the ZIP:**

* **main.py** – Captures video, runs face & threat detection, draws bounding boxes.
* **face\_detector.py** – Uses OpenCV Haar cascades for face detection.
* **threat\_detector.py** – Utilizes a YOLOv5 custom model for threat detection.
* **utils.py** – Helper to ensure the models directory exists.
* **requirements.txt** – Lists Python dependencies.

**Next Steps:**

1. Unzip and navigate into the project directory.
2. Place your `haarcascade_frontalface_default.xml` and YOLOv5 weights (`.pt`) inside the `models/` folder.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:

   ```bash
   python main.py
   ```
5. Press **q** to exit the video window.



✅ Here's your complete **full-stack surveillance face and threat detection system**—ready to run:

🔗 [Download VigilantVision\_FullStack.zip](sandbox:/mnt/data/VigilantVision_FullStack.zip)

### ✅ Features You need to wrute:

* **Backend (Flask API)**: Accepts image input, performs face & threat detection, logs results in a **SQLite database**.
* **Frontend (HTML/JS)**: Lets you upload images and view the detection results.
* **Database (SQLite)**: Automatically created and updated with detection logs.
* **Pre-integrated Models**:

  * YOLOv5 via Ultralytics (auto-downloaded)
  * You must add `haarcascade_frontalface_default.xml` into the `models/` folder.

---

### ▶️ To Run the App:

#### 1. Backend Setup

```bash
cd backend
pip install -r ../requirements.txt
python app.py
```

#### 2. Frontend Setup

Just open `frontend/index.html` in your browser.

---

### 🧠 AI Models

* **Face Detection**: OpenCV Haarcascade.
* **Threat Detection**: YOLOv5s (weapons, persons, etc.).

---





