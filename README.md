# 📸 Vision | Camera Studio

## 📌 Project Overview

**Vision | Camera Studio** is a Python-based webcam application developed using OpenCV and CustomTkinter. It allows users to capture photos, record videos, and apply different visual filters in real time.

The application provides a simple and user-friendly graphical interface where users can manage their camera activities.

## ✨ Features

- 📷 **Live Camera Preview:** Displays real-time webcam footage.
- 📸 **Capture Photo:** Capture images directly from the webcam.
- 💾 **Save Photo:** Save captured photos to your Desktop.
- 🎥 **Video Recording:** Start and stop webcam video recording.
- 💾 **Save Video:** Save recorded videos to your computer.
- 🎨 **Multiple Camera Filters:**
  - Normal
  - Black & White
  - Sepia
  - Vintage
- 🖥️ **GUI Interface:** Modern dark-themed interface using CustomTkinter.
- 🔄 **Real-Time Processing:** Applies selected filters to the live camera preview and recordings.

## 🛠️ Technologies Used

- **Python** – Main programming language.
- **OpenCV (cv2)** – Camera access, image processing, and video recording.
- **CustomTkinter** – Graphical user interface.
- **Pillow (PIL)** – Image conversion and display.
- **NumPy** – Image filter calculations.
- **OS** – Folder creation and file management.
- **Time** – Photo and video filenames with timestamps.
- **Tempfile** – Temporary video storage.
- **Shutil** – Moving recorded videos to the save folder.

## 📂 Project Structure

```text
Vision-Camera-Studio/
│
├── CameraStudio.py
│
└── README.md
```

## ⚙️ Installation

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

### Step 2: Install Required Libraries

Open the VS Code terminal or PowerShell and run:

```bash
pip install opencv-python customtkinter pillow numpy
```

### Step 3: Run the Application

Run the following command:

```bash
python CameraStudio.py
```

## 🚀 How to Use

1. Run the Python application.
2. Allow the application to access your webcam.
3. View the live camera preview.
4. Select a filter from the dropdown menu.
5. Click **CAPTURE PHOTO** to take a picture.
6. Click **SAVE PHOTO** to save the captured image.
7. Click **START RECORDING** to record a video.
8. Click **STOP RECORDING** when finished.
9. Click **SAVE VIDEO** to save your recorded video.

## 📁 Output Location

All saved photos and videos are stored automatically in a folder named:

```text
Desktop/
   └── Camera Studio/
         ├── Photo_YYYYMMDD_HHMMSS.jpg
         └── Video_YYYYMMDD_HHMMSS.mp4
```

## 💡 Applications in Real Life

This project demonstrates concepts that can be useful in:

- Webcam-based photo applications.
- Video recording software.
- Virtual camera applications.
- Image processing systems.
- Video conferencing applications.
- Digital photography tools.

## 🎯 Learning Outcomes

Through this project, I learned:

- How to access a webcam using OpenCV.
- How to build a desktop GUI using CustomTkinter.
- How to capture and save images.
- How to record and save videos.
- How to apply image filters using OpenCV and NumPy.
- How to manage files and folders using Python.
- How to combine multiple Python libraries into one application.

## 👩‍💻 Developer

**Developed using Python, OpenCV, and CustomTkinter.**

---

⭐ If you like this project, don't forget to give it a star on GitHub!
