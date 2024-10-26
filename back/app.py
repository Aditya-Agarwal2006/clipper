from flask import Flask, request, jsonify
import os
import whisper

app = Flask(__name__)

# Ensure upload directory exists
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load Whisper model once to save time on repeated requests
model = whisper.load_model("base")

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({'message': 'No video file provided.'}), 400

    file = request.files['video']
    
    # Save the file to the uploads directory
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Transcribe the saved video file
    transcription = transcribe_video(file_path)
    
    # Return the transcription along with dummy clips (replace this with real clips in the future)
    clips = [
        'http://localhost:5000/static/clip1.mp4',
        'http://localhost:5000/static/clip2.mp4'
    ]
    
    return jsonify({
        'message': 'Video processed successfully.',
        'transcription': transcription,
        'clips': clips
    }), 200

def transcribe_video(file_path):
    result = model.transcribe(file_path)
    segments = result['segments']  # Each segment includes text and timestamp
    transcription_with_timestamps = []

    # Extract timestamps and text for each segment
    for segment in segments:
        transcription_with_timestamps.append({
            'start': segment['start'],  # Start time in seconds
            'end': segment['end'],      # End time in seconds
            'text': segment['text']
        })

    return transcription_with_timestamps


if __name__ == '__main__':
    app.run(debug=True)
