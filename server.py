'''This runs the backend server to host the Emotion Detector App'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def index_route():
    '''The main route of the web app'''
    return render_template('index.html')

@app.route("/emotionDetector")
def analyze_emotion():
    '''The core route for detecting emotions'''
    # Get input
    text_to_analyze = request.args.get('textToAnalyze')

    # Invoke emotion detector
    response = emotion_detector(text_to_analyze)

    # Error Handling
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Prepare final response output
    final_output = f"For the given statement, the system response is "\
    f"'anger': {response['anger']}, "\
    f"'disgust': {response['disgust']}, "\
    f"'fear': {response['fear']}, "\
    f"'joy': {response['joy']} and "\
    f"'sadness': {response['sadness']}. "\
    f"The dominant emotion is <b>{response['dominant_emotion']}</b>."

    return final_output

if __name__ == "__main__":
    app.run()
