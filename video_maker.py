from flask import Flask, request
from google import genai
app = Flask(__name__)
client = genai.Client(api_key="AIzaSyAkfWKLXTSNAmJV7hVK7XAgBtAXfh_Xfb8")

@app.route("/video")
def video():
    user_input = request.form[("video_text")]
    operation = client.models.generate_videos(
        model="veo-3.1-generate-preview",
        prompt=prompt,
    )
    generated_video = operation.response.generated_videos[0]
    client.files.download(file=generated_video.video)
    generated_video.video.save(f"{user_input}.mp4")