
# import cv2
# import customtkinter as ctk
# from PIL import Image
# from tkinter import messagebox
# import os
# import time
# import tempfile
# import shutil

# # Window settings
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("blue")

# window = ctk.CTk()
# window.geometry("900x750")
# window.title("VISION | Camera Studio")
# window.resizable(False, False)

# # Camera
# camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# if not camera.isOpened():
#     messagebox.showerror("Camera Error", "Camera not found!")
#     window.destroy()
#     raise SystemExit

# # Variables
# current_filter = "Normal"
# captured_photo = None
# recording = False
# video_writer = None
# temp_video = None
# pending_video = None

# save_folder = os.path.join(
#     os.path.expanduser("~"), "Desktop", "Camera Studio"
# )

# # Header
# header = ctk.CTkFrame(window, height=75, corner_radius=0)
# header.pack(fill="x")

# ctk.CTkLabel(
#     header,
#     text="VISION  |  CAMERA STUDIO",
#     font=("Arial", 25, "bold")
# ).pack(side="left", padx=25, pady=18)

# ctk.CTkLabel(
#     header,
#     text="PHOTO  •  VIDEO  •  FILTERS",
#     font=("Arial", 13),
#     text_color="gray"
# ).pack(side="right", padx=25)

# # Camera preview
# preview = ctk.CTkLabel(
#     window,
#     text="Starting Camera...",
#     width=600,
#     height=350,
#     corner_radius=15
# )
# preview.pack(pady=20)

# # Filter function
# def apply_filter(frame):

#     if current_filter == "Black & White":
#         frame = cv2.cvtColor(
#             frame, cv2.COLOR_BGR2GRAY
#         )
#         frame = cv2.cvtColor(
#             frame, cv2.COLOR_GRAY2BGR
#         )

#     elif current_filter == "Sepia":
#         matrix = [
#             [0.272, 0.534, 0.131],
#             [0.349, 0.686, 0.168],
#             [0.393, 0.769, 0.189]
#         ]
#         frame = cv2.transform(frame, __import__("numpy").array(matrix))
#         frame = cv2.convertScaleAbs(frame)

#     elif current_filter == "Vintage":
#         frame = cv2.convertScaleAbs(
#             frame, alpha=0.8, beta=20
#         )

#     return frame

# # Update camera
# def update_camera():

#     global captured_photo

#     ret, frame = camera.read()

#     if ret:
#         frame = cv2.flip(frame, 1)
#         frame = apply_filter(frame)

#         if recording and video_writer:
#             video_writer.write(frame)

#         image = cv2.cvtColor(
#             frame, cv2.COLOR_BGR2RGB
#         )

#         image = Image.fromarray(image)
#         photo = ctk.CTkImage(
#             light_image=image,
#             dark_image=image,
#             size=(600, 350)
#         )

#         preview.configure(image=photo, text="")
#         preview.image = photo

#     window.after(15, update_camera)

# # Capture photo
# def capture_photo():

#     global captured_photo

#     ret, frame = camera.read()

#     if ret:
#         frame = cv2.flip(frame, 1)
#         captured_photo = apply_filter(frame.copy())

#         messagebox.showinfo(
#             "Photo Captured",
#             "Photo captured! Click Save Photo to keep it."
#         )

# # Save photo with permission
# def save_photo():

#     global captured_photo

#     if captured_photo is None:
#         messagebox.showwarning(
#             "No Photo", "Capture a photo first!"
#         )
#         return

#     if messagebox.askyesno(
#         "Save Permission",
#         "Do you want to save this photo?"
#     ):
#         os.makedirs(save_folder, exist_ok=True)

#         filename = time.strftime("Photo_%Y%m%d_%H%M%S.jpg")

#         path = os.path.join(save_folder, filename)

#         cv2.imwrite(path, captured_photo)

#         captured_photo = None

#         messagebox.showinfo(
#             "Saved", "Photo saved successfully!"
#         )

# # Start video recording
# def start_recording():

#     global recording, video_writer, temp_video

#     ret, frame = camera.read()

#     if not ret:
#         return

#     height, width = frame.shape[:2]

#     temp_video = tempfile.mktemp(suffix=".mp4")

#     fourcc = cv2.VideoWriter_fourcc(*"mp4v")

#     video_writer = cv2.VideoWriter(
#         temp_video, fourcc, 20, (width, height)
#     )

#     if not video_writer.isOpened():
#         video_writer = None
#         messagebox.showerror(
#             "Error", "Could not start video recording."
#         )
#         return

#     recording = True
#     record_button.configure(text="STOP RECORDING")

# # Stop video recording
# def stop_recording():

#     global recording, video_writer, pending_video

#     recording = False

#     if video_writer:
#         video_writer.release()
#         video_writer = None

#     pending_video = temp_video

#     record_button.configure(text="START RECORDING")

#     messagebox.showinfo(
#         "Recording Complete",
#         "Video is ready. Click Save Video to keep it."
#     )

# # Record button
# def toggle_recording():

#     if recording:
#         stop_recording()
#     else:
#         start_recording()

# # Save video with permission
# def save_video():

#     global pending_video

#     if not pending_video or not os.path.exists(pending_video):
#         messagebox.showwarning(
#             "No Video", "Record a video first!"
#         )
#         return

#     if messagebox.askyesno(
#         "Save Permission",
#         "Do you want to save this video?"
#     ):
#         os.makedirs(save_folder, exist_ok=True)

#         filename = time.strftime("Video_%Y%m%d_%H%M%S.mp4")

#         path = os.path.join(save_folder, filename)

#         shutil.move(pending_video, path)
#         pending_video = None

#         messagebox.showinfo(
#             "Saved", "Video saved successfully!"
#         )

# # Filter selection
# def change_filter(choice):
#     global current_filter
#     current_filter = choice

# # Controls
# controls = ctk.CTkFrame(window, corner_radius=15)
# controls.pack(pady=10, padx=25, fill="x")

# ctk.CTkLabel(
#     controls,
#     text="CAMERA CONTROLS",
#     font=("Arial", 17, "bold")
# ).pack(pady=12)

# filter_menu = ctk.CTkOptionMenu(
#     controls,
#     values=[
#         "Normal",
#         "Black & White",
#         "Sepia",
#         "Vintage"
#     ],
#     command=change_filter
# )
# filter_menu.pack(pady=8)

# photo_button = ctk.CTkButton(
#     controls,
#     text="CAPTURE PHOTO",
#     command=capture_photo,
#     width=180
# )
# photo_button.pack(side="left", padx=15, pady=15)

# save_photo_button = ctk.CTkButton(
#     controls,
#     text="SAVE PHOTO",
#     command=save_photo,
#     width=150
# )
# save_photo_button.pack(side="left", padx=10)

# record_button = ctk.CTkButton(
#     controls,
#     text="START RECORDING",
#     command=toggle_recording,
#     fg_color="#C0392B",
#     hover_color="#922B21",
#     width=180
# )
# record_button.pack(side="left", padx=10)

# save_video_button = ctk.CTkButton(
#     controls,
#     text="SAVE VIDEO",
#     command=save_video,
#     width=150
# )
# save_video_button.pack(side="left", padx=10)

# # Start camera preview
# def close_app():

#     global recording

#     recording = False

#     if video_writer:
#         video_writer.release()

#     camera.release()

#     if pending_video and os.path.exists(pending_video):
#         os.remove(pending_video)

#     if temp_video and os.path.exists(temp_video):
#         os.remove(temp_video)

#     window.destroy()

# window.protocol("WM_DELETE_WINDOW", close_app)

# update_camera()

# window.mainloop()




import cv2
import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
import os
import time
import tempfile
import shutil
import numpy as np

# --------------------------------
# WINDOW SETTINGS
# --------------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.geometry("850x700")
window.title("VISION | Camera Studio")

# --------------------------------
# CAMERA SETTINGS
# --------------------------------

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not camera.isOpened():
    messagebox.showerror("Camera Error", "Camera not found!")
    window.destroy()
    raise SystemExit

# --------------------------------
# VARIABLES
# --------------------------------

current_filter = "Normal"
captured_photo = None

recording = False
video_writer = None

temp_video = None
pending_video = None

save_folder = os.path.join(
    os.path.expanduser("~"),
    "Desktop",
    "Camera Studio"
)

# --------------------------------
# HEADER
# --------------------------------

header = ctk.CTkFrame(
    window,
    height=65,
    corner_radius=0
)

header.pack(fill="x")

ctk.CTkLabel(
    header,
    text="VISION | CAMERA STUDIO",
    font=("Arial", 22, "bold")
).pack(side="left", padx=20, pady=15)

ctk.CTkLabel(
    header,
    text="PHOTO  •  VIDEO  •  FILTERS",
    font=("Arial", 12),
    text_color="gray"
).pack(side="right", padx=20)

# --------------------------------
# CAMERA PREVIEW FRAME
# --------------------------------

preview = ctk.CTkLabel(
    window,
    text="Starting Camera...",
    width=450,
    height=338,
    corner_radius=15
)

preview.pack(pady=15)

# --------------------------------
# FILTER FUNCTION
# --------------------------------

def apply_filter(frame):

    if current_filter == "Black & White":

        frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        frame = cv2.cvtColor(
            frame,
            cv2.COLOR_GRAY2BGR
        )

    elif current_filter == "Sepia":

        matrix = np.array([
            [0.272, 0.534, 0.131],
            [0.349, 0.686, 0.168],
            [0.393, 0.769, 0.189]
        ])

        frame = cv2.transform(frame, matrix)
        frame = cv2.convertScaleAbs(frame)

    elif current_filter == "Vintage":

        frame = cv2.convertScaleAbs(
            frame,
            alpha=0.8,
            beta=20
        )

    return frame

# --------------------------------
# UPDATE CAMERA
# --------------------------------

def update_camera():

    ret, frame = camera.read()

    if ret:

        frame = cv2.flip(frame, 1)

        frame = apply_filter(frame)

        if recording and video_writer:
            video_writer.write(frame)

        image = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        image = Image.fromarray(image)

        photo = ctk.CTkImage(
            light_image=image,
            dark_image=image,
            size=(450, 338)
        )

        preview.configure(
            image=photo,
            text=""
        )

        preview.image = photo

    if window.winfo_exists():
        window.after(30, update_camera)

# --------------------------------
# CAPTURE PHOTO
# --------------------------------

def capture_photo():

    global captured_photo

    ret, frame = camera.read()

    if ret:

        frame = cv2.flip(frame, 1)

        captured_photo = apply_filter(frame.copy())

        messagebox.showinfo(
            "Photo Captured",
            "Photo captured successfully!"
        )

# --------------------------------
# SAVE PHOTO
# --------------------------------

def save_photo():

    global captured_photo

    if captured_photo is None:

        messagebox.showwarning(
            "No Photo",
            "Please capture a photo first!"
        )

        return

    permission = messagebox.askyesno(
        "Save Permission",
        "Do you want to save this photo?"
    )

    if permission:

        os.makedirs(save_folder, exist_ok=True)

        filename = time.strftime(
            "Photo_%Y%m%d_%H%M%S.jpg"
        )

        path = os.path.join(
            save_folder,
            filename
        )

        cv2.imwrite(path, captured_photo)

        captured_photo = None

        messagebox.showinfo(
            "Saved",
            "Photo saved successfully!"
        )

# --------------------------------
# START VIDEO RECORDING
# --------------------------------

def start_recording():

    global recording, video_writer, temp_video

    ret, frame = camera.read()

    if not ret:
        return

    height, width = frame.shape[:2]

    temp_video = tempfile.mktemp(suffix=".mp4")

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    video_writer = cv2.VideoWriter(
        temp_video,
        fourcc,
        20,
        (width, height)
    )

    if not video_writer.isOpened():

        video_writer = None

        messagebox.showerror(
            "Error",
            "Could not start video recording!"
        )

        return

    recording = True

    record_button.configure(
        text="STOP RECORDING"
    )

# --------------------------------
# STOP VIDEO RECORDING
# --------------------------------

def stop_recording():

    global recording, video_writer, pending_video

    recording = False

    if video_writer:

        video_writer.release()
        video_writer = None

    pending_video = temp_video

    record_button.configure(
        text="START RECORDING"
    )

    messagebox.showinfo(
        "Recording Complete",
        "Video is ready! Click SAVE VIDEO."
    )

# --------------------------------
# RECORD BUTTON
# --------------------------------

def toggle_recording():

    if recording:
        stop_recording()

    else:
        start_recording()

# --------------------------------
# SAVE VIDEO
# --------------------------------

def save_video():

    global pending_video

    if not pending_video or not os.path.exists(pending_video):

        messagebox.showwarning(
            "No Video",
            "Please record a video first!"
        )

        return

    permission = messagebox.askyesno(
        "Save Permission",
        "Do you want to save this video?"
    )

    if permission:

        os.makedirs(save_folder, exist_ok=True)

        filename = time.strftime(
            "Video_%Y%m%d_%H%M%S.mp4"
        )

        path = os.path.join(
            save_folder,
            filename
        )

        shutil.move(pending_video, path)

        pending_video = None

        messagebox.showinfo(
            "Saved",
            "Video saved successfully!"
        )

# --------------------------------
# CHANGE FILTER
# --------------------------------

def change_filter(choice):

    global current_filter

    current_filter = choice

# --------------------------------
# CONTROL PANEL
# --------------------------------

controls = ctk.CTkFrame(
    window,
    corner_radius=15
)

controls.pack(
    pady=10,
    padx=20,
    fill="x"
)

ctk.CTkLabel(
    controls,
    text="CAMERA CONTROLS",
    font=("Arial", 16, "bold")
).pack(pady=10)

filter_menu = ctk.CTkOptionMenu(
    controls,
    values=[
        "Normal",
        "Black & White",
        "Sepia",
        "Vintage"
    ],
    command=change_filter
)

filter_menu.pack(pady=8)

photo_button = ctk.CTkButton(
    controls,
    text="CAPTURE PHOTO",
    command=capture_photo,
    width=150
)

photo_button.pack(
    side="left",
    padx=10,
    pady=15
)

save_photo_button = ctk.CTkButton(
    controls,
    text="SAVE PHOTO",
    command=save_photo,
    width=120
)

save_photo_button.pack(
    side="left",
    padx=10
)

record_button = ctk.CTkButton(
    controls,
    text="START RECORDING",
    command=toggle_recording,
    fg_color="#C0392B",
    hover_color="#922B21",
    width=150
)

record_button.pack(
    side="left",
    padx=10
)

save_video_button = ctk.CTkButton(
    controls,
    text="SAVE VIDEO",
    command=save_video,
    width=120
)

save_video_button.pack(
    side="left",
    padx=10
)

# --------------------------------
# CLOSE APPLICATION
# --------------------------------

def close_app():

    global recording, video_writer

    recording = False

    if video_writer:
        video_writer.release()

    camera.release()

    if pending_video and os.path.exists(pending_video):
        os.remove(pending_video)

    if temp_video and os.path.exists(temp_video):
        os.remove(temp_video)

    window.destroy()

window.protocol(
    "WM_DELETE_WINDOW",
    close_app
)

# --------------------------------
# START APPLICATION
# --------------------------------

update_camera()

window.mainloop()

