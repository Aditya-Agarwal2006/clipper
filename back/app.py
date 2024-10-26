from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({'message': 'No video file provided.'}), 400

    file = request.files['video']
    
    # Save the file somewhere (for simplicity, skipping processing for now)
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    # Dummy clips for now (you'd return the real processed clips)
    clips = [
        'http://localhost:5000/static/clip1.mp4',
        'http://localhost:5000/static/clip2.mp4'
    ]
    
    return jsonify({'message': 'Video processed successfully.', 'clips': clips}), 200

if __name__ == '__main__':
    app.run(debug=True)
