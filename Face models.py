# # Import necessary libraries
# from deepface import DeepFace
# import cv2
# from googleapiclient.discovery import build

# # YouTube API setup
# YOUTUBE_API_KEY = 'AIzaSyCmTUZnBpZVde5eE301YmBW_Br_MD7Tcq0'
# youtube = build('youtube', 'v3', developerKey=AIzaSyCmTUZnBpZVde5eE301YmBW_Br_MD7Tcq0)

# # Step 1: Capture an image from the webcam
# def capture_image_from_webcam():
#     # Open webcam using OpenCV
#     cam = cv2.VideoCapture(0)
#     cv2.namedWindow("Press Space to Capture Image")

#     while True:
#         ret, frame = cam.read()
#         if not ret:
#             print("Failed to grab frame")
#             break
#         cv2.imshow("Press Space to Capture Image", frame)

#         # Capture image when spacebar is pressed
#         if cv2.waitKey(1) & 0xFF == ord(' '):
#             img_name = "captured_image.jpg"
#             cv2.imwrite(img_name, frame)
#             print(f"Image captured and saved as {img_name}")
#             break

#     cam.release()  # Release the webcam
#     cv2.destroyAllWindows()
#     return img_name  # Return the captured image path

# # Step 2: Detect emotion using DeepFace
# def detect_emotion(image_path):
#     # Analyze the image using DeepFace to detect emotions
#     analysis = DeepFace.analyze(img_path=image_path, actions=['emotion'])
    
#     # Check if the result is a list (i.e., multiple faces detected)
#     if isinstance(analysis, list):
#         analysis = analysis[0]  # Get the first face's emotion analysis
    
#     # Return the dominant emotion from the analysis
#     return analysis['dominant_emotion']

# # Step 3: Suggest a song based on the detected emotion
# def get_youtube_link(song_name):
#     request = youtube.search().list(
#         q=song_name,
#         part='snippet',
#         type='video',
#         maxResults=1
#     )
#     response = request.execute()
#     video_id = response['items'][0]['id']['videoId']
#     return f"https://www.youtube.com/watch?v={video_id}"

# def suggest_song(emotion):
#     # Mapping emotions to specific songs (can be customized)
#     song_recommendations = {
#         "happy": "Happy by Pharrell Williams",
#         "sad": "Someone Like You by Adele",
#         "angry": "Break Stuff by Limp Bizkit",
#         "neutral": "Here Comes the Sun by The Beatles",
#         "fear": "Don't Panic by Coldplay",
#         "surprise": "Surprise Yourself by Jack Garratt",
#         "disgust": "Bad Guy by Billie Eilish"
#     }
#     song = song_recommendations.get(emotion, "Shape of You by Ed Sheeran")
#     youtube_link = get_youtube_link(song)
#     return youtube_link

# # Main function that ties everything together
# def main():
#     # Capture image from webcam
#     image_path = capture_image_from_webcam()
    
#     # Detect the dominant emotion
#     dominant_emotion = detect_emotion(image_path)
#     print(f"Dominant emotion detected: {dominant_emotion}")
    
#     # Suggest a song and get YouTube link
#     song_link = suggest_song(dominant_emotion)
#     print(f"Suggested song link: {song_link}")

# # Run the program
# if __name__ == "__main__":
#     main()


import json
import random
import webbrowser
from deepface import DeepFace
import cv2

# Step 1: Capture an image from the webcam
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

# Step 2: Detect emotion using DeepFace
def detect_emotion(image_path):
    analysis = DeepFace.analyze(img_path=image_path, actions=['emotion'])
    if isinstance(analysis, list):
        analysis = analysis[0]
    return analysis['dominant_emotion']

# Step 3: Search for the song on Google and get the URL
def search_on_google(song_name):
    query = f"{song_name} site:youtube.com"
    search_url = f"https://www.google.com/search?q={query}"
    return search_url

def suggest_song(emotion, songs):
    song_list = songs.get(emotion, ["Shape of You by Ed Sheeran"])
    song = random.choice(song_list)
    search_url = search_on_google(song)
    return search_url

# Load songs from JSON file
def load_songs():
    with open('songs.json', 'r') as file:
        return json.load(file)

# Main function that ties everything together
def main():
    songs = load_songs()
    image_path = capture_image_from_webcam()
    dominant_emotion = detect_emotion(image_path)
    print(f"Dominant emotion detected: {dominant_emotion}")
    
    search_url = suggest_song(dominant_emotion, songs)
    print(f"Search URL: {search_url}")
    
    # Open the search URL in the default web browser
    webbrowser.open(search_url)

if __name__ == "__main__":
    main()
