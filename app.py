# from flask import Flask, render_template, request, jsonify
# import json
# import random
# import cv2
# from deepface import DeepFace

# app = Flask(__name__)

# # Load songs from JSON file
# def load_songs():
#     try:
#         with open('songs.json', 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return {}

# # Capture an image from the webcam
# def capture_image_from_webcam():
#     cam = cv2.VideoCapture(0)
#     cv2.namedWindow("Press Space to Capture Image")

#     while True:
#         ret, frame = cam.read()
#         if not ret:
#             print("Failed to grab frame")
#             break
#         cv2.imshow("Press Space to Capture Image", frame)

#         if cv2.waitKey(1) & 0xFF == ord(' '):
#             img_name = "captured_image.jpg"
#             cv2.imwrite(img_name, frame)
#             print(f"Image captured and saved as {img_name}")
#             break

#     cam.release()
#     cv2.destroyAllWindows()
#     return img_name

# # Detect emotion using DeepFace
# def detect_emotion(image_path):
#     analysis = DeepFace.analyze(img_path=image_path, actions=['emotion'])
#     if isinstance(analysis, list):
#         analysis = analysis[0]
#     return analysis['dominant_emotion']

# # Suggest a song based on emotion
# def suggest_song(emotion, songs):
#     song_list = songs.get(emotion, ["Shape of You by Ed Sheeran"])
#     song = random.choice(song_list)
#     search_url = f"https://www.google.com/search?q={song} site:youtube.com"
#     return song, search_url

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/start_capture', methods=['POST'])
# def start_capture():
#     image_path = capture_image_from_webcam()
#     dominant_emotion = detect_emotion(image_path)
#     songs = load_songs()
#     song_name, song_url = suggest_song(dominant_emotion, songs)
#     return jsonify({'emotion': dominant_emotion, 'songName': song_name, 'songUrl': song_url})

# @app.route('/restart', methods=['POST'])
# def restart():
#     return jsonify({'redirect': '/'})

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import json
import random
import cv2
from deepface import DeepFace

app = Flask(__name__)

# Load songs from JSON file
def load_songs():
    try:
        with open('songs.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Capture an image from the webcam
def capture_image_from_webcam():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Press Space to Capture Image")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow("Press Space to Capture Image", frame)

        if cv2.waitKey(1) & 0xFF == ord(' '):
            img_name = "captured_image.jpg"
            cv2.imwrite(img_name, frame)
            print(f"Image captured and saved as {img_name}")
            break

    cam.release()
    cv2.destroyAllWindows()
    return img_name

# Detect emotion using DeepFace
def detect_emotion(image_path):
    analysis = DeepFace.analyze(img_path=image_path, actions=['emotion'])
    if isinstance(analysis, list):
        analysis = analysis[0]
    return analysis['dominant_emotion']

# Suggest a song based on emotion
def suggest_song(emotion, songs):
    song_list = songs.get(emotion, ["Shape of You by Ed Sheeran"])
    song = random.choice(song_list)
    search_url = f"https://www.google.com/search?q={song} site:youtube.com"
    return song, search_url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_capture', methods=['POST'])
def start_capture():
    image_path = capture_image_from_webcam()
    dominant_emotion = detect_emotion(image_path)
    songs = load_songs()
    song_name, song_url = suggest_song(dominant_emotion, songs)
    return jsonify({'emotion': dominant_emotion, 'songName': song_name, 'songUrl': song_url})

@app.route('/restart', methods=['POST'])
def restart():
    return jsonify({'redirect': '/'})

if __name__ == "__main__":
    app.run(debug=True)
